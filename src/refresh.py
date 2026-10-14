# -*- coding: utf-8 -*-
"""
Zweiwöchentliche Datenpflege für FindeDeineLeute.de

Prüft alle verlinkten Communities und schreibt das Ergebnis nach data/state.json:
  ok       Datum der letzten erfolgreichen Prüfung
  fails    Anzahl aufeinanderfolgender harter Fehler (404, 410, Domain weg, Einladung ungültig)
  members  Mitgliederzahl, falls die Plattform sie öffentlich ausgibt
build.py blendet Einträge nach 3 harten Fehlern in Folge (also nach ca. 6 Wochen) aus.

Regeln, die hier fest eingebaut sind:
  * Eigener User-Agent mit Kontaktadresse, ein Request pro Sekunde und Host.
  * robots.txt wird für jede Webseite beachtet. Was verboten ist, wird nicht abgerufen.
  * Instagram, Facebook, WhatsApp und Signal werden NICHT abgerufen (Nutzungsbedingungen
    verbieten automatisierten Abruf). Diese Links bleiben ungeprüft und werden über
    Hinweise aus der Community und manuelle Stichproben gepflegt.
  * Discord: nur die offizielle, öffentliche Einladungs-API (Name und Mitgliederzahl).
  * Reddit: nur über die offizielle API mit eigenen Zugangsdaten (REDDIT_CLIENT_ID und
    REDDIT_CLIENT_SECRET als GitHub-Secrets). Ohne Zugangsdaten werden Subreddits übersprungen.
  * Telegram: nur die öffentliche Vorschauseite eines öffentlichen Kanals oder einer Gruppe.
"""
import json, os, re, sys, time, datetime, threading, socket, base64
import urllib.request, urllib.error, urllib.robotparser
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.dirname(os.path.abspath(__file__))
STATE = ROOT + '/data/state.json'
DATA = ROOT + '/data/data.json'
UA = 'FindeDeineLeuteBot/1.0 (+https://findedeineleute.de/ueber-uns/; nicky.nikaaa@gmail.com)'
TODAY = datetime.date.today().isoformat()
TIMEOUT = 15
SKIP_HOSTS = ('instagram.com', 'facebook.com', 'fb.com', 'chat.whatsapp.com', 'whatsapp.com', 'signal.group', 'signal.me')

state = {'last_run': TODAY, 'links': {}}
try:
    state = json.load(open(STATE, encoding='utf8'))
    state['last_run'] = TODAY
    state.setdefault('links', {})
except Exception:
    pass

_host_lock = {}
_host_last = {}
_glock = threading.Lock()
_robots = {}


def host_wait(host):
    with _glock:
        lk = _host_lock.setdefault(host, threading.Lock())
    with lk:
        d = time.time() - _host_last.get(host, 0)
        if d < 1.0:
            time.sleep(1.0 - d)
        _host_last[host] = time.time()


def allowed(url):
    p = urlparse(url)
    base = '%s://%s' % (p.scheme, p.netloc)
    with _glock:
        rp = _robots.get(base)
    if rp is None:
        rp = urllib.robotparser.RobotFileParser()
        try:
            host_wait(p.netloc)
            req = urllib.request.Request(base + '/robots.txt', headers={'User-Agent': UA})
            raw = urllib.request.urlopen(req, timeout=TIMEOUT).read().decode('utf8', 'replace')
            rp.parse(raw.splitlines())
        except urllib.error.HTTPError as e:
            # 4xx bei robots.txt bedeutet: keine Einschränkung. 5xx: vorsichtshalber nicht abrufen.
            if 400 <= e.code < 500:
                rp.parse([])
            else:
                rp.parse(['User-agent: *', 'Disallow: /'])
        except Exception:
            rp.parse(['User-agent: *', 'Disallow: /'])
        with _glock:
            _robots[base] = rp
    return rp.can_fetch(UA, url)


def fetch(url, headers=None, limit=200000):
    host_wait(urlparse(url).netloc)
    h = {'User-Agent': UA, 'Accept-Language': 'de'}
    if headers:
        h.update(headers)
    req = urllib.request.Request(url, headers=h)
    r = urllib.request.urlopen(req, timeout=TIMEOUT)
    return r.status, r.geturl(), r.read(limit).decode('utf8', 'replace')


HARD = (404, 410)


def check_web(url):
    """Rückgabe: ('ok'|'dead'|'unknown', members|None)"""
    if not allowed(url):
        return 'unknown', None
    try:
        st, final, body = fetch(url)
        low = body.lower()[:6000]
        if any(k in low for k in ('domain steht zum verkauf', 'this domain is for sale', 'domain is parked', 'buy this domain')):
            return 'dead', None
        return 'ok', None
    except urllib.error.HTTPError as e:
        return ('dead' if e.code in HARD else 'unknown'), None
    except urllib.error.URLError as e:
        if isinstance(e.reason, socket.gaierror):
            return 'dead', None  # Domain existiert nicht mehr
        return 'unknown', None
    except Exception:
        return 'unknown', None


def check_discord(url):
    m = re.search(r'(?:discord\.gg|discord(?:app)?\.com/invite)/([\w-]+)', url)
    if not m:
        return check_web(url)
    try:
        st, final, body = fetch('https://discord.com/api/v10/invites/%s?with_counts=true' % m.group(1))
        j = json.loads(body)
        return 'ok', j.get('approximate_member_count')
    except urllib.error.HTTPError as e:
        return ('dead' if e.code == 404 else 'unknown'), None
    except Exception:
        return 'unknown', None


_reddit_tok = {'t': None, 'exp': 0}


def reddit_token():
    cid, sec = os.environ.get('REDDIT_CLIENT_ID'), os.environ.get('REDDIT_CLIENT_SECRET')
    if not cid or not sec:
        return None
    if _reddit_tok['t'] and time.time() < _reddit_tok['exp']:
        return _reddit_tok['t']
    req = urllib.request.Request('https://www.reddit.com/api/v1/access_token', data=b'grant_type=client_credentials',
                                 headers={'User-Agent': UA, 'Authorization': 'Basic ' + base64.b64encode((cid + ':' + sec).encode()).decode()})
    j = json.loads(urllib.request.urlopen(req, timeout=TIMEOUT).read())
    _reddit_tok.update(t=j['access_token'], exp=time.time() + j.get('expires_in', 3600) - 60)
    return _reddit_tok['t']


def check_reddit(url):
    m = re.search(r'reddit\.com/r/([\w]+)', url)
    tok = None
    try:
        tok = reddit_token()
    except Exception:
        pass
    if not m or not tok:
        return 'unknown', None
    try:
        st, final, body = fetch('https://oauth.reddit.com/r/%s/about' % m.group(1), {'Authorization': 'bearer ' + tok})
        d = json.loads(body).get('data', {})
        if d.get('over18') and False:
            return 'ok', None
        return 'ok', d.get('subscribers')
    except urllib.error.HTTPError as e:
        return ('dead' if e.code in (404, 403) else 'unknown'), None
    except Exception:
        return 'unknown', None


def check_telegram(url):
    if not allowed(url):
        return 'unknown', None
    try:
        st, final, body = fetch(url)
        if 'tgme_page_title' not in body:
            return 'dead', None
        m = re.search(r'tgme_page_extra">([\d\s]+)\s*(?:members|subscribers|Mitglieder|Abonnenten)', body)
        return 'ok', int(re.sub(r'\s', '', m.group(1))) if m else None
    except urllib.error.HTTPError as e:
        return ('dead' if e.code in HARD else 'unknown'), None
    except Exception:
        return 'unknown', None


def check(url):
    host = (urlparse(url).hostname or '').lower().replace('www.', '')
    if any(host == h or host.endswith('.' + h) for h in SKIP_HOSTS):
        return 'skip', None
    if host in ('discord.gg',) or host.endswith('discord.com'):
        return check_discord(url)
    if host.endswith('reddit.com'):
        return check_reddit(url)
    if host == 't.me':
        return check_telegram(url)
    return check_web(url)


def work(url):
    try:
        return url, check(url)
    except Exception:
        return url, ('unknown', None)


def main():
    items = json.load(open(DATA, encoding='utf8'))
    urls = sorted({e['l'] for e in items if e.get('l')})
    if os.environ.get('LIMIT'):
        import random; random.seed(1); urls = random.sample(urls, int(os.environ['LIMIT']))
    print('Links:', len(urls))
    stats = {'ok': 0, 'dead': 0, 'unknown': 0, 'skip': 0}
    dead_now = []
    with ThreadPoolExecutor(max_workers=12) as ex:
        for url, (res, members) in ex.map(work, urls):
            stats[res] += 1
            s = state['links'].setdefault(url, {})
            if res == 'ok':
                s['ok'] = TODAY
                s['fails'] = 0
                if members:
                    s['members'] = members
            elif res == 'dead':
                s['fails'] = s.get('fails', 0) + 1
                dead_now.append((url, s['fails']))
    state['stats'] = stats
    json.dump(state, open(STATE, 'w', encoding='utf8'), ensure_ascii=False, indent=1, sort_keys=True)
    print(stats)
    if dead_now:
        print('Nicht mehr erreichbar (Fehler in Folge):')
        for u, n in dead_now:
            print(' ', n, u)


if __name__ == '__main__':
    sys.exit(main())
