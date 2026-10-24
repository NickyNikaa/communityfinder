# -*- coding: utf-8 -*-
import json,html,os,shutil,datetime,collections,sys,glob,re
ROOT=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,ROOT)
from static_data import CITIES as CITYTXT
from content import CATINFO, ARTICLES
DOMAIN='https://findedeineleute.de'
CF_EMAIL='nicky.nikaaa@gmail.com'
TODAY=datetime.date.today().isoformat()
try: LASTRUN=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'data','state.json'),encoding='utf8')).get('last_run','')
except Exception: LASTRUN=''
OUT=os.environ.get('OUT',os.path.join(os.path.dirname(ROOT),'dist'))
if os.path.exists(OUT): shutil.rmtree(OUT)
os.makedirs(OUT)
shutil.copytree(ROOT+'/assets',OUT+'/assets')
E=html.escape
data=json.load(open(ROOT+'/data/data.json',encoding='utf8'))
# Recherchierte Treffzeiten (data/wann_extra.json) einarbeiten; parkrun startet bundesweit um 9 Uhr
try: _WX=json.load(open(ROOT+'/data/wann_extra.json',encoding='utf8'))
except Exception: _WX={}
for _e in data:
    _x=_WX.get(_e['n']+'|'+_e['t'])
    if _x and not _e.get('w'):
        _e['w']=_x['w']
        if _x.get('a') and not _e.get('a'): _e['a']=_x['a']
    if 'parkrun' in _e['n'].lower() and _e.get('w')=='Samstags': _e['w']='Samstags 9 Uhr'
cities=[l.split('|') for l in CITYTXT.splitlines()]   # (name, slug)
SLUG={n:s for n,s in cities}
CATS=[('sport','Sport & Fitness'),('outdoor','Outdoor & Natur'),('wellbeing','Wellbeing'),('tanz','Tanz'),('musik','Musik & Chor'),('kunst','Kunst & Handwerk'),('foto','Foto & Film'),('spiele','Brett- & Rollenspiele'),('gaming','Gaming & E-Sport'),('lernen','Bücher & Lernen'),('sprachen','Sprachen & Austausch'),('essen','Essen & Trinken'),('business','Business & Karriere'),('tech','Tech & Code'),('leute','Neue Leute'),('queer','Queer'),('frauen','Frauen'),('familie','Eltern & Familie'),('tiere','Tiere'),('mobil','Mobilität & Rad'),('reisen','Reisen'),('engagement','Umwelt & Engagement'),('studium','Studium')]
PLAT={'website':'Website','instagram':'Instagram','facebook':'Facebook','meetup':'Meetup','discord':'Discord','telegram':'Telegram','whatsapp':'WhatsApp','reddit':'Reddit','slack':'Slack','signal':'Signal','forum':'Forum','sonstige':'Weitere'}
CAT=dict(CATS)
by_city=collections.defaultdict(list)
for e in data: by_city[e['t']].append(e)
N=len(data)
def w(path,content):
    full=os.path.join(OUT,path)
    os.makedirs(os.path.dirname(full),exist_ok=True)
    open(full,'w',encoding='utf8').write(content)

NAV=[('/entdecken/','Entdecken','entdecken'),('/online/','Online','online'),('/staedte/','Städte','staedte'),('/ratgeber/','Ratgeber','ratgeber'),('/kalender/','Kalender','kalender'),('/aktuell/','Aktuell','aktuell'),('/kontakt/','Kontakt','kontakt')]
def layout(key,path,title,desc,body,extra_head='',noindex=False,jsonld=None):
    url=DOMAIN+path
    nav=''.join('<a class="nl" href="%s"%s>%s</a>'%(h,' aria-current="page"' if k==key else '',t) for h,t,k in NAV)
    topc=''.join('<li><a href="/%s/">%s</a></li>'%(SLUG[n],E(n)) for n,_ in cities[:8])
    ld=''
    if jsonld: ld='<script type="application/ld+json">%s</script>'%json.dumps(jsonld,ensure_ascii=False)
    return f'''<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<link rel="canonical" href="{url}">
{'<meta name="robots" content="noindex,follow">' if noindex else '<meta name="robots" content="index,follow,max-image-preview:large">'}
<meta property="og:type" content="website">
<meta property="og:site_name" content="FindeDeineLeute.de">
<meta property="og:locale" content="de_DE">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{DOMAIN}/assets/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{DOMAIN}/assets/og.png">
<meta name="theme-color" content="#ffffff">
<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
<link rel="alternate" type="application/rss+xml" title="Aktuelles von FindeDeineLeute.de" href="/aktuell/feed.xml">
<link rel="preload" href="/assets/fonts/inter-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/styles.css">
{extra_head}{ld}
</head>
<body>
<a class="skip" href="#main">Zum Inhalt springen</a>
<div class="wrap">
<header class="top"><div class="bar">
<a class="brand" href="/" aria-label="FindeDeineLeute.de, zur Startseite"><svg class="logo-mark" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 96 96"><defs><linearGradient id="lm" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#d6336c"/><stop offset=".55" stop-color="#a77cf0"/><stop offset="1" stop-color="#62b9f2"/></linearGradient></defs><circle cx="41" cy="41" r="30" fill="none" stroke="url(#lm)" stroke-width="8"/><path d="M63 63l21 21" stroke="#d6336c" stroke-width="10" stroke-linecap="round"/><circle cx="41" cy="32" r="9.5" fill="#d6336c" opacity="0.92"/><circle cx="50" cy="41" r="9.5" fill="#a77cf0" opacity="0.92"/><circle cx="41" cy="50" r="9.5" fill="#8fd3f4" opacity="0.92"/><circle cx="32" cy="41" r="9.5" fill="#f6a5c8" opacity="0.92"/></svg><span>FindeDeineLeute<i>.de</i></span></a>
<button class="menu-btn" id="menuBtn" aria-expanded="false" aria-controls="mainNav">Menü</button>
<nav class="main" id="mainNav" aria-label="Hauptnavigation">{nav}<a class="saved-link" href="/merkliste/" aria-label="Meine Merkliste">{HEART}<span id="savedCount" aria-live="polite"></span></a><a class="btn primary sm" href="/kontakt/">Anfrage senden</a></nav>
</div></header>
<main id="main">
{body}
</main>
<footer>
<div><b style="font-family:var(--f-display);font-size:18px;font-weight:500;color:var(--ink)">FindeDeineLeute.de</b><p style="margin-top:10px;max-width:34ch">Das Verzeichnis für Communities in allen deutschen Großstädten und online.</p></div>
<div class="cols">
<div><h4>Entdecken</h4><ul><li><a href="/entdecken/">Alle Communities</a></li><li><a href="/staedte/">Alle Städte</a></li><li><a href="/online/">Online-Communities</a></li><li><a href="/ratgeber/">Ratgeber</a></li><li><a href="/aktuell/">Aktuell</a></li><li><a href="/kalender/">Kalender</a></li><li><a href="/merkliste/">Merkliste</a></li><li><a href="/auswertung/">Auswertung</a></li></ul></div>
<div><h4>Städte</h4><ul>{topc}</ul></div>
<div><h4>Mehr</h4><ul><li><a href="/ueber-uns/">Über uns</a></li><li><a href="/newsletter/">Newsletter</a></li><li><a href="/ki/">KI &amp; AI</a></li><li><a href="/presse/">Presse</a></li><li><a href="/kontakt/">Kontakt</a></li><li><a href="/impressum/">Impressum</a></li><li><a href="/datenschutz/">Datenschutz</a></li><li><button type="button" class="linkbtn" data-consent-open>Cookie-Einstellungen</button></li></ul></div>
</div>
<div class="legal">© {datetime.date.today().year} FindeDeineLeute.de. Die Einträge stammen aus öffentlich zugänglichen Verzeichnissen und verlinken auf die jeweiligen Communities.</div>
</footer>
</div>
<script src="/assets/config.js"></script>
<script src="/assets/app.js" defer></script>
<script src="/assets/consent.js" defer></script>
</body>
</html>
'''


import zlib
WD=[('montag',0),('dienstag',1),('mittwoch',2),('donnerstag',3),('freitag',4),('samstag',5),('sonntag',6)]
WDRE=re.compile(r'(montag|dienstag|mittwoch|donnerstag|freitag|samstag|sonntag)s?',re.I)
ORD={'erste':1,'zweite':2,'dritte':3,'vierte':4,'letzte':-1}
def parse_when(w):
    """Wandelt Texte wie 'Letzter Freitag, 18 Uhr' oder 'Samstags' in Termine um: [{d,o,t}]. Unklares wird übersprungen."""
    if not w: return []
    low=w.lower()
    if re.search(r'monatlich|alle \d+ wochen|alle zwei wochen|zweiwöchentlich|etwa|meist|flexibel|regelm|pro jahr|mehrere|siehe',low) and not re.search(r'\d\.\s|letzte',low): return []
    ms=list(WDRE.finditer(w))
    if not ms: return []
    out=[]
    for i,m in enumerate(ms):
        start=ms[i-1].end() if i else 0
        end=ms[i+1].start() if i+1<len(ms) else len(w)
        before=w[start:m.start()]; after=w[m.end():end]
        ords=[int(x) for x in re.findall(r'(\d)\.',before)]
        for k,v in ORD.items():
            if re.search(k+r'[rn]?\b',before.lower()): ords.append(v)
        t=''
        mt=re.search(r'(\d{1,2})(?::(\d\d))?(?=\s*(?:Uhr|bis))',after) or re.search(r'\b(\d{1,2}):(\d\d)\b',after) or re.search(r'(\d{1,2})(?::(\d\d))?(?=\s*Uhr)',before)
        if mt: t='%02d:%s'%(int(mt.group(1)),mt.group(2) or '00')
        out.append({'d':[v for k,v in WD if m.group(1).lower()==k][0],'o':sorted(set(ords)),'t':t})
    for i in range(len(out)-2,-1,-1):
        if not out[i]['t'] and out[i+1]['t'] and not re.search(r'\d',w[ms[i].end():ms[i+1].start()]): out[i]['t']=out[i+1]['t']
    if 'darauf' in low: out=[o for o in out if o['o']]
    return out
def stable_key(e):
    return format(zlib.crc32((e['n']+'|'+e['t']).encode('utf8')) & 0xffffffff,'x')

CALIT=[]
for e in data:
    sc=parse_when(e.get('w',''))
    if sc and e['t'] in SLUG:
        CALIT.append({'k':stable_key(e),'n':e['n'],'t':e['t'],'c':e['c'],'w':e['w'],'l':e['l'],'sc':sc,'slug':SLUG[e['t']],'a':'' if e['s']=='criticalmass.de' else e['a']})
CAL_BY_CITY=collections.defaultdict(list)
for _x in CALIT: CAL_BY_CITY[_x['t']].append(_x)

HEART='<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21s-7.5-4.6-9.6-9.2C1 8.6 2.8 5 6.2 5c2 0 3.4 1.1 4.1 2.3L12 9.6l1.7-2.3C14.4 6.1 15.8 5 17.8 5c3.4 0 5.2 3.6 3.8 6.8C19.5 16.4 12 21 12 21Z"/></svg>'
def savebtn(e):
    return '<button type="button" class="save" data-save="%s" aria-pressed="false" aria-label="%s merken">%s</button>'%(stable_key(e),E(e['n']),HEART)
def card(c):
    href='/%s/#c%d'%(SLUG.get(c['t'],''),c['i']) if c['t'] in SLUG else (c['l'] or '#')
    place='Online' if c['t']=='Online' else c['t']+(' · '+c['a'] if c['a'] and c['s']!='criticalmass.de' else '')
    pl='<span>%s</span>'%E(PLAT.get(c.get('p'),'')) if c.get('p') and c['p']!='website' else ''
    note=E(c['w'])
    return ('<article class="card">'+savebtn(c)+'<div class="tag"><span>'+('Online' if c['f']=='online' else 'Vor Ort')+'</span><span>'+E(CAT[c['c']])+'</span>'+pl+'</div><h3><a href="'+href+'">'+E(c['n'])+'</a></h3><div class="sub">'+E(place)+'</div><p class="d">'+E(c['x'])+'</p><div class="note">'+note+'</div></article>')
byname={e['n']:e for e in data}
def pick(names): return [byname[n] for n in names if n in byname]

# ---------- START ----------
onl_all=[e for e in data if e['f']=='online']
_ak=lambda n:n.lower().replace('ä','a').replace('ö','o').replace('ü','u').replace('ß','ss'); opts=''.join('<option value="%s">%s</option>'%(E(n),E(n)) for n,_ in sorted(cities,key=lambda c:_ak(c[0])))
stack=''.join('<div class="mini"><div><b>%s</b><span class="s">%s · %s</span></div></div>'%(E(c['n']),E(c['t']),E(CAT[c['c']])) for c in pick(['Hasenheide parkrun','Chaosdorf Düsseldorf','Urban Sketchers Hamburg']))
_f=pick(['Critical Mass Hamburg','Urban Sketchers Köln','Entropia Karlsruhe','Netzwerk Leipziger Gemeinschaftsgärten'])
_seen={c['c'] for c in _f}
for _cat in ['musik','tanz','spiele','wellbeing','lernen','foto','essen','leute','queer','outdoor']:
    if len(_f)>=9: break
    if _cat in _seen: continue
    _c=[e for e in data if e['c']==_cat and e['f']!='online' and len(e.get('x',''))>70 and e['t'] in SLUG]
    if _c: _f.append(_c[0]); _seen.add(_cat)
feat=''.join(card(c).replace('<article class="card"','<article class="card c%d"'%(i%4),1) for i,c in enumerate(_f))
mq=''.join('<a href="/%s/"><b>%s</b><i>%d</i></a>'%(s,E(n),len(by_city[n])) for n,s in cities[:24])
cg=''.join('<a class="cityb" href="/%s/"><span>%s</span><i>%d</i></a>'%(s,E(n),len(by_city[n])) for n,s in cities[:15])
KI_RE=re.compile(r'\b(ki|ai|künstliche intelligenz|machine learning|maschinelles lernen|data science|chatgpt|llms?|deep learning|openai|mlops|prompt\w*|generative)\b',re.I)
_kin=len([e for e in data if KI_RE.search(e['n']+' '+e['x']+' '+e.get('g',''))])
chips='<a class="chip topic" href="/ki/">KI &amp; AI <i>%d</i></a>'%_kin+''.join('<a class="chip" href="/entdecken/?kategorie=%s">%s</a>'%(i,E(CAT[i])) for i in ['sport','outdoor','wellbeing','tanz','musik','kunst','foto','spiele','gaming','lernen','sprachen','essen','business','tech','leute','queer','frauen','familie','tiere','mobil','reisen','engagement','studium'] if i in CAT)
rg=''.join('<article class="card"><div class="tag"><span>Ratgeber</span></div><h3><a href="/ratgeber/%s/">%s</a></h3><p class="d">%s</p></article>'%(a['slug'],E(a['title']),E(a['desc'])) for a in ARTICLES[:4])
onchips=''.join('<a class="chip" href="/online/?plattform=%s">%s <i>%d</i></a>'%(k,PLAT[k],n) for k,n in collections.Counter(e.get('p') for e in onl_all).most_common() if k in PLAT)
start=f'''<div class="hero"><div class="blobs" aria-hidden="true"><i></i><i></i><i></i></div>
<a class="badge" href="/entdecken/"><span class="live" aria-hidden="true"></span><b data-count="{N}">{format(N,',').replace(',','.')}</b> <span>Communities in {len(cities)} Städten<span class="hm"> und online</span></span></a>
<h1>Finde Menschen, die deine <em>Leidenschaft</em> teilen.</h1>
<p class="lead">Das Verzeichnis für Communities in allen deutschen Großstädten und online. Ob Run Club, Hackerspace oder Gartennetzwerk: Such dir aus, wo du dazugehören willst.</p>
<form class="search" action="/entdecken/" method="get" role="search">
<input name="q" type="search" placeholder="Wonach suchst du? z. B. Laufen" aria-label="Community suchen">
<select name="stadt" class="select" aria-label="Stadt wählen"><option value="">Alle Städte</option>{opts}</select>
<button class="btn primary" type="submit">Suchen</button>
</form>
<div class="chips">{chips}</div>
<div class="stack" aria-label="Beispiele aus dem Verzeichnis">{stack}</div>
</div>

<section class="section reveal"><div class="section-head"><div><span class="eyebrow live-eyebrow"><span class="live" aria-hidden="true"></span>Gerade beliebt</span><h2>Communities zum Reinschnuppern</h2></div><div class="rail-nav"><button type="button" class="rail-btn" data-dir="-1" aria-label="Zurück">&#8592;</button><button type="button" class="rail-btn" data-dir="1" aria-label="Weiter">&#8594;</button><a class="btn ghost" href="/entdecken/">Alle ansehen</a></div></div><div class="rail" id="rail">{feat}</div></section>
<section class="section reveal"><div class="section-head"><div><span class="eyebrow">Online</span><h2>Communities ohne Ortsgrenze</h2></div><a class="btn ghost" href="/online/">Alle Online-Communities</a></div><div class="chips">{onchips}</div></section>
<section class="section reveal"><div class="section-head"><div><span class="eyebrow">Städte</span><h2>Die größten Städte</h2></div><a class="btn ghost" href="/staedte/">Alle {len(cities)} Städte</a></div><div class="citygrid">{cg}</div></section>
<section class="section reveal"><div class="section-head"><div><span class="eyebrow">So funktioniert es</span><h2>In drei Schritten dabei</h2></div></div>
<div class="steps"><div class="step"><h3>Suchen</h3><p>Wähle deine Stadt, ein Thema oder Online. Die Suche durchsucht Namen, Beschreibungen und Themen.</p></div><div class="step"><h3>Reinschnuppern</h3><p>Jeder Eintrag verlinkt auf die Community selbst. Dort siehst du aktuelle Termine und kannst Kontakt aufnehmen.</p></div><div class="step"><h3>Dabeibleiben</h3><p>Gefällt es dir, wirst du Teil der Gruppe. Passt es nicht, probierst du die nächste aus.</p></div></div></section>
<section class="section reveal"><div class="section-head"><div><span class="eyebrow">Ratgeber</span><h2>Tipps für den Einstieg</h2></div><a class="btn ghost" href="/ratgeber/">Alle Beiträge</a></div><div class="grid">{rg}</div></section>
<section class="section reveal"><div class="band"><div><h2>Du leitest eine Community?</h2><p>Trag deine Gruppe bei FindeDeineLeute.de ein und werde von Menschen gefunden, die genau dein Thema suchen. Schick uns eine kurze Anfrage, wir melden uns bei dir.</p></div><a class="btn" href="/kontakt/?thema=eintragen">Anfrage senden</a></div></section>'''
org={"@context":"https://schema.org","@type":"Organization","name":"FindeDeineLeute.de","url":DOMAIN+"/","logo":DOMAIN+"/assets/favicon.svg"}
wsite={"@context":"https://schema.org","@type":"WebSite","name":"FindeDeineLeute.de","url":DOMAIN+"/","inLanguage":"de","potentialAction":{"@type":"SearchAction","target":DOMAIN+"/entdecken/?q={search_term_string}","query-input":"required name=search_term_string"}}
w('index.html',layout('start','/','FindeDeineLeute.de | Communities in deiner Stadt und online finden',f'Finde Communities in allen {len(cities)} deutschen Großstädten und online: Run Clubs, Hackerspaces, Gartennetzwerke, Zeichengruppen und mehr.',start,jsonld=[wsite,org]))

# ---------- ENTDECKEN ----------
entd='''<div class="pagehead"><span class="eyebrow">Verzeichnis</span><h1 class="page-title">Communities entdecken</h1><p class="page-sub">Suche nach Themen oder wähle deine Stadt. Alle Filter wirken sofort, du musst nichts bestätigen. Kategorien kannst du kombinieren.</p></div>
<div class="filters" id="filters"><button type="button" class="ftoggle" id="fToggle" aria-expanded="false">Filter anzeigen</button><div class="frow">
<div class="field"><label for="q">Suche</label><input class="input" id="q" type="search" placeholder="Name, Thema oder Ort"></div>
<div class="field"><label for="city">Stadt</label><select class="select" id="city"><option value="">Alle Städte</option></select></div>
<div class="field"><label for="sort">Sortierung</label><select class="select" id="sort"><option value="rec">Empfohlen</option><option value="az">Name A bis Z</option></select></div>
<div class="field"><label for="plat">Plattform</label><select class="select" id="plat"><option value="">Alle Plattformen</option></select></div>
<div class="field"><label id="fmtL">Format</label><div class="seg" role="group" aria-labelledby="fmtL" id="fmt"><button data-v="" aria-pressed="true">Alle</button><button data-v="ort" aria-pressed="false">Vor Ort</button><button data-v="online" aria-pressed="false">Online</button></div></div>
</div><div class="chips" id="catChips" role="group" aria-label="Kategorien"></div></div>
<div class="result-bar"><b id="count" aria-live="polite">Lade Verzeichnis …</b><span style="display:flex;gap:14px;align-items:center;flex-wrap:wrap"><a class="btn ghost sm" id="cityLink" href="#" hidden></a><button class="btn ghost sm" id="reset" type="button">Filter zurücksetzen</button></span></div>
<div class="grid" id="grid" data-mode="all"></div>
<noscript><p class="lede">Für die Suche brauchst du JavaScript. Ohne JavaScript findest du alle Communities auf den <a href="/staedte/">Seiten der Städte</a>.</p></noscript>
<div style="display:flex;justify-content:center;margin-top:44px"><button class="btn ghost" type="button" id="more" hidden>Mehr anzeigen</button></div>
<p class="note" style="margin-top:28px">Die Einträge stammen aus öffentlich zugänglichen Quellen. Alle zwei Wochen prüfen wir die Links automatisch und blenden Einträge aus, die nicht mehr erreichbar sind. Termine und Angaben können sich ändern, bitte prüfe sie vor dem Besuch bei der Community.</p>
<div class="overlay" id="overlay" hidden><div class="modal" role="dialog" aria-modal="true" aria-labelledby="mTitle" id="modal"></div></div>'''
w('entdecken/index.html',layout('entdecken','/entdecken/','Communities entdecken | FindeDeineLeute.de','Durchsuche Communities in allen deutschen Großstädten und online nach Thema, Stadt und Kategorie.',entd))

# ---------- STÄDTE ----------
alls=''.join('<a href="/%s/" data-a="%s" data-n="%s" data-o="%d"><span>%s</span><i>%d</i></a>'%(s,E(_ak(n)),E(n.lower()+' '+_ak(n)+' '+n.lower().replace('ä','ae').replace('ö','oe').replace('ü','ue').replace('ß','ss')),i,E(n),len(by_city[n])) for i,(n,s) in sorted(enumerate(cities),key=lambda t:_ak(t[1][0])))
CITYTOOLS='''<style>.citytools{display:flex;flex-wrap:wrap;gap:12px;align-items:center;margin:0 0 20px}.citytools input{flex:1 1 260px;max-width:420px;padding:12px 16px;border:1px solid #cfc8e6;border-radius:12px;font:inherit}.citytools .chip[aria-pressed=true]{background:#c2185b;color:#fff;border-color:#c2185b}.citytools .info{flex-basis:100%;margin:0;font-size:.9rem;opacity:.75}</style><div class="citytools"><input type="search" id="cityQ" placeholder="Stadt suchen, z. B. München" aria-label="Stadt suchen" autocomplete="off"><button type="button" class="chip" data-sort="az" aria-pressed="true">A bis Z</button><button type="button" class="chip" data-sort="size" aria-pressed="false">Nach Größe</button><p class="info" id="cityInfo" aria-live="polite"></p></div><script>document.addEventListener("DOMContentLoaded",function(){var box=document.getElementById("citiesAll");if(!box)return;var q=document.getElementById("cityQ"),info=document.getElementById("cityInfo"),btns=document.querySelectorAll("[data-sort]"),items=Array.prototype.slice.call(box.children),mode="az";function render(){var qv=q.value.trim().toLowerCase(),shown=0;items.sort(function(a,b){if(mode==="az"){return a.getAttribute("data-a")<b.getAttribute("data-a")?-1:1}return a.getAttribute("data-o")-b.getAttribute("data-o")});items.forEach(function(el){box.appendChild(el);var ok=!qv||el.getAttribute("data-n").indexOf(qv)>-1;el.style.display=ok?"":"none";if(ok)shown++});info.textContent=shown?(shown+" von "+items.length+" Städten"):"Keine Stadt gefunden. Prüfe die Schreibweise."}q.addEventListener("input",render);q.addEventListener("keydown",function(e){if(e.key==="Enter"){var f=items.filter(function(el){return el.style.display!=="none"})[0];if(f)location.href=f.getAttribute("href")}});Array.prototype.forEach.call(btns,function(b){b.addEventListener("click",function(){mode=b.getAttribute("data-sort");Array.prototype.forEach.call(btns,function(x){x.setAttribute("aria-pressed",x===b?"true":"false")});render()})});render()});</script>'''
w('staedte/index.html',layout('staedte','/staedte/','Alle Städte | FindeDeineLeute.de',f'Communities in allen {len(cities)} deutschen Großstädten mit mehr als 100.000 Einwohnern.',
 f'<div class="pagehead"><span class="eyebrow">Städte</span><h1 class="page-title">Communities nach Stadt</h1><p class="page-sub">Wähle deine Stadt. Die Zahl zeigt, wie viele Communities im Verzeichnis stehen. Aufgeführt sind alle deutschen Städte mit mehr als 100.000 Einwohnern. Suche direkt nach deiner Stadt oder sortiere die Liste.</p></div>'+CITYTOOLS+f'<div class="cities-all" id="citiesAll">{alls}</div><div style="height:48px"></div>'))


# ---------- AKTUELL: Beiträge ----------
TYPEL={'neu':'Neu im Verzeichnis','veranstaltung':'Veranstaltung','news':'Neuigkeit','thema':'Thema','spotlight':'Spotlight'}
def fdate(d):
    y,m,dd=d.split('-');mon=['Januar','Februar','März','April','Mai','Juni','Juli','August','September','Oktober','November','Dezember'][int(m)-1]
    return '%d. %s %s'%(int(dd),mon,y)
def md_basic(t):
    out=[]
    for blk in t.strip().split('\n\n'):
        blk=blk.strip()
        if blk.startswith('## '): out.append('<h2>%s</h2>'%E(blk[3:]))
        else:
            h=E(blk)
            h=re.sub(r'\[([^\]]+)\]\(((?:/|https?://)[^)]*)\)',lambda m:'<a href="%s"%s>%s</a>'%(m.group(2).replace('&amp;','&'),' target="_blank" rel="noopener noreferrer"' if m.group(2).startswith('http') else '',m.group(1)),h)
            out.append('<p>%s</p>'%h)
    return '\n'.join(out)
POSTS=[]
# manuelle Beiträge
for fn in sorted(glob.glob(os.path.join(ROOT,'content','posts','*.md'))):
    raw=open(fn,encoding='utf8').read()
    m=re.match(r'---\s*\n(.*?)\n---\s*\n(.*)',raw,re.S)
    if not m: continue
    meta={}
    for ln in m.group(1).splitlines():
        if ':' in ln:
            k,v=ln.split(':',1);meta[k.strip()]=v.strip()
    stadt=meta.get('stadt','')
    if stadt and stadt!='Online' and stadt not in SLUG: continue
    slug=re.sub(r'^\d{4}-\d{2}-\d{2}-','',os.path.basename(fn)[:-3])
    POSTS.append(dict(slug=slug,title=meta.get('titel',slug),date=meta.get('datum',TODAY),city=stadt,type=meta.get('typ','news'),desc=meta.get('beschreibung',''),html=md_basic(m.group(2)),link=meta.get('link',''),ev=(meta.get('event_start',''),meta.get('event_ort',''))))
# automatische Beiträge: neu aufgenommene Gruppen
newgrp=collections.defaultdict(list)
for e in data:
    if e.get('fs','')>='2026-10-01': newgrp[(e['t'],e['fs'])].append(e)
for (city,d),l in sorted(newgrp.items()):
    if len(l)<4: continue
    l=sorted(l,key=lambda e:(-e['q'],e['n'].lower()))
    shown=l[:8]
    if city=='Online':
        title='Neue Online-Communities im Verzeichnis (%d Gruppen)'%len(l); slug='neu-online-'+d
        intro='Neu aufgenommen wurden %d Online-Communities, darunter %s.'%(len(l),', '.join(e['n'] for e in shown[:3]))
    else:
        title='Neu in %s: %d Gruppen im Verzeichnis'%(city,len(l)); slug='neu-in-%s-%s'%(SLUG[city],d)
        intro='In %s sind %d neue Gruppen dazugekommen, darunter %s.'%(city,len(l),', '.join(e['n'] for e in shown[:3]))
    html='<p class="lede">%s</p>'%E(intro)
    for e in shown:
        pl=PLAT.get(e.get('p'),'')
        html+='<h2>%s</h2><p>%s</p><p class="note">%s%s%s</p>'%(E(e['n']),E(e['x']),E(CAT[e['c']]),(' · '+E(pl)) if pl and pl!='Website' else '',(' · '+E(e['w'])) if e['w'] else '')
        if e['l']: html+='<p><a href="%s" target="_blank" rel="noopener noreferrer">Zur Community</a></p>'%E(e['l'])
    if len(l)>len(shown): html+='<p>Dazu kommen %d weitere Gruppen, die du auf der Seite %s findest.</p>'%(len(l)-len(shown),('<a href="/%s/">Communities in %s</a>'%(SLUG[city],E(city))) if city!='Online' else '<a href="/online/">Online-Communities</a>')
    POSTS.append(dict(slug=slug,title=title,date=d,city=city,type='neu',desc=intro,html=html,link='',ev=('','')))
POSTS.sort(key=lambda p:(p['date'],p['slug']),reverse=True)
POSTCITY=collections.defaultdict(list)
for p in POSTS:
    if p['city'] and p['city']!='Online': POSTCITY[p['city']].append(p)
def post_card(p):
    where=p['city'] if p['city'] else 'Bundesweit'
    return '<article class="card"><div class="tag"><span>%s</span><span>%s</span></div><h3><a href="/aktuell/%s/">%s</a></h3><div class="sub">%s</div><p class="d">%s</p></article>'%(E(TYPEL.get(p['type'],'Beitrag')),E(fdate(p['date'])),p['slug'],E(p['title']),E(where),E(p['desc']))

# ---------- STADTSEITEN ----------
def city_intro(city,items):
    cats=collections.Counter(e['c'] for e in items)
    top=cats.most_common(1)[0]
    s1=f'{city} hat aktuell {len(items)} Einträge im Verzeichnis, verteilt auf {len(cats)} Kategorien.'
    s2=f'Am größten ist die Kategorie {CAT[top[0]]} mit {top[1]} {"Eintrag" if top[1]==1 else "Einträgen"}.'
    cm=[e for e in items if e['n'].startswith('Critical Mass')]
    s3=''
    if cm: s3=f'Die Critical Mass {city} trifft sich {cm[0]["w"][:1].lower()+cm[0]["w"][1:]}, Treffpunkt ist {cm[0]["a"]}.'
    runs=[e for e in items if 'run club' in e['g'] or 'parkrun' in e['g']]
    s4=f'Dazu kommen {len(runs)} Run Clubs und parkrun-Läufe.' if len(runs)>=3 else ''
    return [s1+' '+s2,(s3+' '+s4).strip()]
MINCOMBO=3
COMBO={}
for e in data:
    COMBO.setdefault((e['t'],e['c']),[]).append(e)
HAS={k for k,v in COMBO.items() if len(v)>=MINCOMBO and k[0] in SLUG}
for city,slug in cities:
    items=sorted(by_city[city],key=lambda e:(-e['q'],e['n'].lower()))
    cats=collections.OrderedDict()
    for cid,_ in CATS:
        l=[e for e in items if e['c']==cid]
        if l: cats[cid]=l
    nav=''.join('<a href="#k-%s">%s <i>%d</i></a>'%(cid,E(CAT[cid]),len(l)) for cid,l in cats.items())
    secs=''
    for cid,l in cats.items():
        rows=''
        for e in l:
            sub=' · '.join(x for x in [e['a'] if e['a'] and e['s']!='criticalmass.de' else '',e['w']] if x)
            rows+='<li class="row" id="c%d"><div class="rb"><h3>%s</h3>%s<p class="d">%s</p></div><div class="ra">%s%s</div></li>'%(
                e['i'],E(e['n']),('<div class="sub">%s</div>'%E(sub)) if sub else '',E(e['x']),
                ('<a class="btn ghost sm" href="%s" target="_blank" rel="noopener noreferrer" aria-label="%s: Zur Community">Zur Community</a>'%(E(e['l']),E(e['n']))) if e['l'] else '',savebtn(e))
        more=('<p class="note" style="margin:-8px 0 18px"><a href="/%s/%s/">Alle %d Gruppen für %s in %s ansehen</a></p>'%(slug,cid,len(l),E(CATINFO[cid][0]),E(city))) if (city,cid) in HAS else ''
        secs+='<section class="csec" id="k-%s"><h2>%s</h2>%s<ul class="rows">%s</ul></section>'%(cid,E(CAT[cid]),more,rows)
    intro=city_intro(city,items)
    _wk=CAL_BY_CITY.get(city,[])
    weekbox=('<section class="csec weekbox" id="woche" data-city="%s" hidden><h2>Diese Woche in %s</h2><div class="weeklist" id="weekList"></div><p class="note" style="margin-top:14px"><a href="/kalender/?stadt=%s">Ganzen Kalender für %s ansehen</a></p><script type="application/json" id="weekData">%s</script></section>'%(E(city),E(city),slug,E(city),json.dumps(_wk,ensure_ascii=False,separators=(',',':')).replace('</','<\\/'))) if _wk else ''
    cp=POSTCITY.get(city,[])
    newsbox=('<section class="csec" id="aktuell"><h2>Aktuelles aus %s</h2><ul class="rows">%s</ul><p class="note" style="margin-top:14px"><a href="/%s/aktuell/">Alle Beiträge aus %s</a></p></section>'%(E(city),''.join('<li class="row"><div class="rb"><h3><a href="/aktuell/%s/">%s</a></h3><div class="sub">%s</div></div></li>'%(p['slug'],E(p['title']),E(fdate(p['date']))) for p in cp[:3]),slug,E(city))) if cp else ''
    others=''.join('<a class="cityb" href="/%s/"><span>%s</span><i>%d</i></a>'%(s,E(n),len(by_city[n])) for n,s in cities if n!=city)[:0]
    near=[(n,s) for n,s in cities[:14] if n!=city][:12]
    others=''.join('<a class="cityb" href="/%s/"><span>%s</span><i>%d</i></a>'%(s,E(n),len(by_city[n])) for n,s in near)
    body=f'''<nav class="crumbs" aria-label="Brotkrumen"><a href="/">Start</a><span>/</span><a href="/staedte/">Städte</a><span>/</span><span>{E(city)}</span></nav>
<div class="pagehead" style="padding-top:24px"><h1 class="page-title" style="margin-top:0">Communities in {E(city)}</h1><p class="lede">{E(intro[0])}</p>{('<p class="lede">%s</p>'%E(intro[1])) if intro[1] else ''}<div class="catnav" aria-label="Kategorien in {E(city)}">{nav}</div></div>
{weekbox}{newsbox}{secs}
<section class="section" style="border-bottom:0"><div class="band"><div><h2>Deine Community fehlt in {E(city)}?</h2><p>Trag sie ein, damit andere sie finden.</p></div><a class="btn" href="/kontakt/?thema=eintragen">Anfrage senden</a></div></section>
<section class="section" style="border-bottom:0;padding-top:0"><div class="section-head"><div><span class="eyebrow">Weitere Städte</span></div><a class="btn ghost sm" href="/staedte/">Alle Städte</a></div><div class="citygrid">{others}</div></section>'''
    desc=f'{len(items)} Communities in {city}: {", ".join(CAT[c] for c in list(cats)[:3])} und mehr. Finde Gruppen und Gleichgesinnte in deiner Stadt.'
    ld=[{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Start","item":DOMAIN+"/"},{"@type":"ListItem","position":2,"name":"Städte","item":DOMAIN+"/staedte/"},{"@type":"ListItem","position":3,"name":city,"item":f"{DOMAIN}/{slug}/"}]},
        {"@context":"https://schema.org","@type":"ItemList","name":f"Communities in {city}","numberOfItems":len(items),"itemListElement":[{"@type":"ListItem","position":k+1,"name":e['n'],**({"url":e['l']} if e['l'] else {})} for k,e in enumerate(items[:50])]}]
    w(f'{slug}/index.html',layout('staedte',f'/{slug}/',f'Communities in {city} | FindeDeineLeute.de',desc,body,jsonld=ld))


# ---------- STADT x THEMA ----------
def row_html(e):
    sub=' · '.join(x for x in [e['a'] if e['a'] and e['s']!='criticalmass.de' else '',e['w']] if x)
    return '<li class="row"><div class="rb"><h3>%s</h3>%s<p class="d">%s</p></div><div class="ra">%s%s</div></li>'%(
        E(e['n']),('<div class="sub">%s</div>'%E(sub)) if sub else '',E(e['x']),
        ('<a class="btn ghost sm" href="%s" target="_blank" rel="noopener noreferrer" aria-label="%s: Zur Community">Zur Community</a>'%(E(e['l']),E(e['n']))) if e['l'] else '',savebtn(e))
def join_de(xs):
    xs=list(xs)
    return xs[0] if len(xs)==1 else ', '.join(xs[:-1])+' und '+xs[-1]
combo_pages=[]
for city,slug in cities:
    for cid,_ in CATS:
        if (city,cid) not in HAS: continue
        info=CATINFO[cid]; label=info[0]
        l=sorted(COMBO[(city,cid)],key=lambda e:(-e['q'],e['n'].lower()))
        n=len(l)
        names=[e['n'] for e in l[:3]]
        pcnt=collections.Counter(e.get('p') for e in l if e.get('p'))
        plats=[PLAT[k] for k,_ in pcnt.most_common(3) if k in PLAT]
        onl=[e for e in data if e['f']=='online' and e['c']==cid]
        p1=f'In {city} findest du {n} Gruppen und Communities aus dem Bereich {label}, darunter {join_de(names)}.'
        p2=info[1]
        extra=[]
        if plats: extra.append(E(f'Die Gruppen in {city} sind vor allem über {join_de(plats)} zu erreichen.'))
        rh=[e for e in l if e['w'] and len(e['w'])<48][:2]
        if rh: extra.append(E('Zum Rhythmus: '+' '.join('%s (%s).'%(e['n'],e['w'].rstrip('.')) for e in rh)))
        if onl: extra.append(E(f'Wenn du zusätzlich online Anschluss suchst, schau in die {len(onl)} ')+'<a href="/online/?kategorie=%s">Online-Communities</a>'%cid+E(' zum Thema.'))
        extra_html=' '.join(extra)
        qa=[(info[3],info[4]),(f'Wie viele Gruppen für {label} gibt es in {city}?',f'Im Verzeichnis stehen aktuell {n} Einträge. Wir prüfen die Links alle zwei Wochen und ergänzen laufend neue Gruppen.')]
        faq=''.join('<details><summary>%s</summary><p>%s</p></details>'%(E(q),E(a)) for q,a in qa)
        otherc=[c for c,_ in CATS if c!=cid and (city,c) in HAS]
        rel=''.join('<a class="chip" href="/%s/%s/">%s</a>'%(slug,c,E(CATINFO[c][0])) for c in otherc)
        oc=[(cn,cs) for cn,cs in cities if cn!=city and (cn,cid) in HAS][:12]
        ocg=''.join('<a class="cityb" href="/%s/%s/"><span>%s</span><i>%d</i></a>'%(cs,cid,E(cn),len(COMBO[(cn,cid)])) for cn,cs in oc)
        body=f'''<nav class="crumbs" aria-label="Brotkrumen"><a href="/">Start</a><span>/</span><a href="/staedte/">Städte</a><span>/</span><a href="/{slug}/">{E(city)}</a><span>/</span><span>{E(label)}</span></nav>
<div class="pagehead" style="padding-top:24px"><h1 class="page-title" style="margin-top:0">{E(label)} in {E(city)}</h1><p class="lede">{E(p1)}</p><p class="lede">{E(p2)}</p>{('<p class="lede">%s</p>'%extra_html) if extra_html else ''}</div>
<section class="csec"><h2>So gelingt der Einstieg</h2><p class="lede" style="max-width:62ch">{E(info[2])}</p></section>
<section class="csec"><h2>Alle Gruppen ({n})</h2><ul class="rows">{''.join(row_html(e) for e in l)}</ul></section>
<section class="csec"><h2>Häufige Fragen</h2><div class="faq">{faq}</div></section>
<section class="section" style="border-bottom:0"><div class="section-head"><div><span class="eyebrow">Mehr in {E(city)}</span><h2>Weitere Themen</h2></div><a class="btn ghost sm" href="/{slug}/">Alle Communities in {E(city)}</a></div><div class="chips">{rel}</div></section>
{('<section class="section" style="border-bottom:0;padding-top:0"><div class="section-head"><div><span class="eyebrow">Andere Städte</span><h2>%s in weiteren Städten</h2></div></div><div class="citygrid">%s</div></section>'%(E(label),ocg)) if ocg else ''}
<section class="section" style="border-bottom:0;padding-top:0"><div class="band"><div><h2>Deine Gruppe fehlt?</h2><p>Trag sie ein, damit andere sie finden.</p></div><a class="btn" href="/kontakt/?thema=eintragen">Anfrage senden</a></div></section>'''
        ld=[{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Start","item":DOMAIN+"/"},{"@type":"ListItem","position":2,"name":city,"item":f"{DOMAIN}/{slug}/"},{"@type":"ListItem","position":3,"name":label,"item":f"{DOMAIN}/{slug}/{cid}/"}]},
            {"@context":"https://schema.org","@type":"ItemList","name":f"{label} in {city}","numberOfItems":n,"itemListElement":[{"@type":"ListItem","position":k+1,"name":e['n'],**({"url":e['l']} if e['l'] else {})} for k,e in enumerate(l[:50])]},
            {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in qa]}]
        desc=f'{n} Gruppen für {label} in {city}: {", ".join(names)} und mehr. Mit Einsteigertipps und Links zu allen Treffen.'
        path=f'/{slug}/{cid}/'
        w(f'{slug}/{cid}/index.html',layout('staedte',path,f'{label} in {city}: {n} Gruppen und Communities | FindeDeineLeute.de',desc,body,jsonld=ld))
        combo_pages.append(path)

# ---------- RATGEBER ----------
import re as _re
def md(t):
    out=[]
    for blk in t.strip().split('\n\n'):
        blk=blk.strip()
        if blk.startswith('## '): out.append('<h2>%s</h2>'%E(blk[3:]))
        else:
            h=E(blk)
            h=_re.sub(r'\[([^\]]+)\]\(((?:/|https?://)[^)]*)\)',lambda m:'<a href="%s"%s>%s</a>'%(m.group(2).replace('&amp;','&'),' target="_blank" rel="noopener noreferrer"' if m.group(2).startswith('http') else '',m.group(1)),h)
            out.append('<p>%s</p>'%h)
    return '\n'.join(out)
def fdate(d):
    y,m,dd=d.split('-');mon=['Januar','Februar','März','April','Mai','Juni','Juli','August','September','Oktober','November','Dezember'][int(m)-1]
    return '%d. %s %s'%(int(dd),mon,y)
cards=''.join('<article class="card"><div class="tag"><span>Ratgeber</span><span>%s</span></div><h3><a href="/ratgeber/%s/">%s</a></h3><p class="d">%s</p><div class="note">Lesen</div></article>'%(fdate(a['date']),a['slug'],E(a['title']),E(a['desc'])) for a in ARTICLES)
w('ratgeber/index.html',layout('ratgeber','/ratgeber/','Ratgeber: Leute kennenlernen und Communities finden | FindeDeineLeute.de','Praktische Tipps für alle, die neue Leute kennenlernen, eine Gruppe finden oder selbst eine Community starten möchten.',
 f'<div class="pagehead"><span class="eyebrow">Ratgeber</span><h1 class="page-title">Leute kennenlernen, Gruppen finden</h1><p class="page-sub">Kurze, praktische Beiträge für den Einstieg: vom ersten Treffen bis zur eigenen Community.</p></div><div class="grid">{cards}</div><div style="height:48px"></div>'))
for a in ARTICLES:
    path='/ratgeber/%s/'%a['slug']
    others=''.join('<li><a href="/ratgeber/%s/">%s</a></li>'%(b['slug'],E(b['title'])) for b in ARTICLES if b is not a)[:]
    body=f'''<nav class="crumbs" aria-label="Brotkrumen"><a href="/">Start</a><span>/</span><a href="/ratgeber/">Ratgeber</a><span>/</span><span>{E(a['title'])}</span></nav>
<article class="legalwrap prose-l"><p class="note">{fdate(a['date'])}</p><h1 class="page-title">{E(a['title'])}</h1><p class="lede">{E(a['lead'])}</p>
{md(a['body'])}
<h2>Weiterlesen</h2><ul>{others}</ul>
<div class="band" style="margin-top:40px"><div><h2>Gruppe in deiner Stadt finden</h2><p>Wähle deine Stadt und stöbere durch alle Gruppen.</p></div><a class="btn" href="/staedte/">Städte ansehen</a></div></article>'''
    ld=[{"@context":"https://schema.org","@type":"Article","headline":a['title'],"description":a['desc'],"datePublished":a['date'],"dateModified":a['date'],"inLanguage":"de","mainEntityOfPage":DOMAIN+path,"author":{"@type":"Organization","name":"FindeDeineLeute.de"},"publisher":{"@type":"Organization","name":"FindeDeineLeute.de","logo":{"@type":"ImageObject","url":DOMAIN+"/assets/favicon.svg"}}}]
    w('ratgeber/%s/index.html'%a['slug'],layout('ratgeber',path,a['title']+' | FindeDeineLeute.de',a['desc'],body,jsonld=ld))


# ---------- AKTUELL: Seiten ----------
def feed_item(p):
    return '<item><title>%s</title><link>%s/aktuell/%s/</link><guid>%s/aktuell/%s/</guid><pubDate>%s</pubDate><description>%s</description></item>'%(E(p['title']),DOMAIN,p['slug'],DOMAIN,p['slug'],datetime.datetime.strptime(p['date'],'%Y-%m-%d').strftime('%a, %d %b %Y 08:00:00 +0000'),E(p['desc']))
aktuell_pages=[]
chips_c=''.join('<a class="chip" href="/%s/aktuell/">%s <i>%d</i></a>'%(SLUG[c],E(c),len(v)) for c,v in sorted(POSTCITY.items(),key=lambda kv:-len(kv[1])))
if POSTS:
    lst=''.join(post_card(p) for p in POSTS[:60])
else:
    lst='<p class="lede">Hier erscheinen bald die ersten Beiträge.</p>'
w('aktuell/index.html',layout('aktuell','/aktuell/','Aktuell: Neues aus den Communities deiner Stadt | FindeDeineLeute.de','Neue Gruppen, Veranstaltungen und Themen aus den Communities deutscher Städte und online.',
 f'<div class="pagehead"><span class="eyebrow">Aktuell</span><h1 class="page-title">Neues aus den Communities</h1><p class="page-sub">Neue Gruppen, Veranstaltungen und Themen aus deiner Stadt und online.</p>{("<div class=%schips%s style=%smargin-top:22px%s>%s</div>"%(chr(34),chr(34),chr(34),chr(34),chips_c)) if chips_c else ""}</div><div class="grid">{lst}</div><div style="height:48px"></div>'))
aktuell_pages.append('/aktuell/')
w('aktuell/feed.xml','<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0"><channel><title>FindeDeineLeute.de Aktuell</title><link>%s/aktuell/</link><description>Neue Gruppen, Veranstaltungen und Themen aus den Communities</description><language>de</language>%s</channel></rss>\n'%(DOMAIN,''.join(feed_item(p) for p in POSTS[:30])))
for p in POSTS:
    path='/aktuell/%s/'%p['slug']
    cityl=('<a href="/%s/">%s</a>'%(SLUG[p['city']],E(p['city']))) if p['city'] in SLUG else ('<a href="/online/">Online</a>' if p['city']=='Online' else 'Bundesweit')
    ev=''
    if p['ev'][0] or p['ev'][1]: ev='<p class="note">%s%s</p>'%((('Beginn: '+E(p['ev'][0].replace('T',', ')+' Uhr')) if p['ev'][0] else ''),(' · Ort: '+E(p['ev'][1])) if p['ev'][1] else '')
    ext=('<p><a class="btn ghost" href="%s" target="_blank" rel="noopener noreferrer">Mehr dazu</a></p>'%E(p['link'])) if p['link'] else ''
    relc=('<p class="note"><a href="/%s/">Alle Communities in %s</a> · <a href="/%s/aktuell/">Mehr aus %s</a></p>'%(SLUG[p['city']],E(p['city']),SLUG[p['city']],E(p['city']))) if p['city'] in SLUG else ''
    body=f'''<nav class="crumbs" aria-label="Brotkrumen"><a href="/">Start</a><span>/</span><a href="/aktuell/">Aktuell</a><span>/</span><span>{E(p['title'])}</span></nav>
<article class="legalwrap prose-l"><p class="note">{E(TYPEL.get(p['type'],'Beitrag'))} · {fdate(p['date'])} · {cityl}</p><h1 class="page-title">{E(p['title'])}</h1>
{ev}{p['html']}{ext}{relc}
<div class="band" style="margin-top:40px"><div><h2>Deine Community fehlt?</h2><p>Trag sie ein, damit andere sie finden.</p></div><a class="btn" href="/kontakt/?thema=eintragen">Anfrage senden</a></div></article>'''
    ld={"@context":"https://schema.org","@type":"Article","headline":p['title'],"description":p['desc'],"datePublished":p['date'],"dateModified":p['date'],"inLanguage":"de","mainEntityOfPage":DOMAIN+path,"author":{"@type":"Organization","name":"FindeDeineLeute.de"},"publisher":{"@type":"Organization","name":"FindeDeineLeute.de","logo":{"@type":"ImageObject","url":DOMAIN+"/assets/favicon.svg"}}}
    lds=[ld]
    if p['type']=='veranstaltung' and p['ev'][0]:
        lds.append({"@context":"https://schema.org","@type":"Event","name":p['title'],"startDate":p['ev'][0],"eventAttendanceMode":"https://schema.org/OfflineEventAttendanceMode","eventStatus":"https://schema.org/EventScheduled","location":{"@type":"Place","name":p['ev'][1] or p['city'],"address":p['city'] or 'Deutschland'},"description":p['desc'],"url":DOMAIN+path})
    w('aktuell/%s/index.html'%p['slug'],layout('aktuell',path,p['title']+' | FindeDeineLeute.de',p['desc'][:300],body,jsonld=lds))
    aktuell_pages.append(path)
for city,lst_ in POSTCITY.items():
    s=SLUG[city]
    w('%s/aktuell/index.html'%s,layout('aktuell','/%s/aktuell/'%s,'Aktuell in %s: Neues aus den Communities | FindeDeineLeute.de'%city,'Neue Gruppen, Veranstaltungen und Themen aus %s.'%city,
      '<nav class="crumbs" aria-label="Brotkrumen"><a href="/">Start</a><span>/</span><a href="/%s/">%s</a><span>/</span><span>Aktuell</span></nav><div class="pagehead" style="padding-top:24px"><h1 class="page-title" style="margin-top:0">Aktuell in %s</h1><p class="page-sub">Neue Gruppen, Veranstaltungen und Themen aus %s.</p></div><div class="grid">%s</div><div style="height:48px"></div>'%(s,E(city),E(city),E(city),''.join(post_card(p) for p in lst_))))
    aktuell_pages.append('/%s/aktuell/'%s)

# ---------- KI & AI ----------
KI_RE=re.compile(r'\b(ki|ai|künstliche intelligenz|machine learning|maschinelles lernen|data science|chatgpt|llms?|deep learning|openai|mlops|prompt\w*|generative)\b',re.I)
KI_ITEMS=sorted([e for e in data if KI_RE.search(e['n']+' '+e['x']+' '+e.get('g',''))],key=lambda e:(e['t']=='Online',e['t'],-e['q'],e['n'].lower()))
_kc=collections.OrderedDict()
for e in KI_ITEMS: _kc.setdefault(e['t'],[]).append(e)
kibody='<div class="pagehead"><span class="eyebrow">Thema</span><h1 class="page-title">KI &amp; AI Communities in Deutschland</h1><p class="page-sub">%d Gruppen, Meetups und Online-Communities rund um Künstliche Intelligenz, Machine Learning und Data Science in %d Städten und online. Zum Austauschen, Ausprobieren und Dazulernen.</p></div>'%(len(KI_ITEMS),len([k for k in _kc if k!='Online']))
kibody+='<p class="lede" style="max-width:720px">Du suchst gezielt etwas anderes? In der <a href="/entdecken/?q=KI">Suche</a> findest du KI-Gruppen auch zusammen mit Stadt und Format. Fehlt eine Gruppe? <a href="/kontakt/?thema=eintragen">Schick uns eine kurze Nachricht</a>.</p>'
for _t,_es in _kc.items():
    _h=('<a href="/%s/">%s</a>'%(SLUG[_t],E(_t))) if _t in SLUG else 'Online'
    kibody+='<section class="reveal" style="margin-top:40px"><h2 style="font-size:26px">%s <span class="note">%d</span></h2><ul class="rows">%s</ul></section>'%(_h,len(_es),''.join(row_html(e) for e in _es))
w('ki/index.html',layout('ki','/ki/','KI & AI Communities in Deutschland: Meetups, Stammtische, Online | FindeDeineLeute.de','%d Communities zu KI, Machine Learning und Data Science in deutschen Städten und online: Meetups, Stammtische, Discord und mehr.'%len(KI_ITEMS),kibody))

# ---------- ONLINE ----------
on=sorted([e for e in data if e['f']=='online'],key=lambda e:(-e['q'],e['n'].lower()))
pc=collections.Counter(e.get('p') for e in on)
static=''.join('<li class="row"><div class="rb"><h3>%s</h3><p class="d">%s</p><p class="note">%s</p></div><div class="ra">%s</div></li>'%(E(e['n']),E(e['x']),E(PLAT.get(e.get('p'),'')),('<a class="btn ghost sm" href="%s" target="_blank" rel="noopener noreferrer">Zur Community</a>'%E(e['l'])) if e['l'] else '') for e in on[:200])
onbody=f'''<div class="pagehead"><span class="eyebrow">Online</span><h1 class="page-title">Online-Communities</h1><p class="page-sub">{len(on)} Gruppen, Server und Foren, an denen du von überall teilnehmen kannst: Discord, Reddit, Telegram, Foren und mehr. Alle Filter wirken sofort.</p></div>
<div class="filters" id="filters"><button type="button" class="ftoggle" id="fToggle" aria-expanded="false">Filter anzeigen</button><div class="frow online">
<div class="field"><label for="q">Suche</label><input class="input" id="q" type="search" placeholder="Name oder Thema"></div>
<div class="field"><label for="sort">Sortierung</label><select class="select" id="sort"><option value="rec">Empfohlen</option><option value="az">Name A bis Z</option></select></div>
</div>
<div><p class="flabel">Plattform</p><div class="chips" id="platChips" role="group" aria-label="Plattform"></div></div>
<div><p class="flabel">Kategorie</p><div class="chips" id="catChips" role="group" aria-label="Kategorien"></div></div></div>
<div class="result-bar"><b id="count" aria-live="polite">Lade Verzeichnis …</b><span><button class="btn ghost sm" id="reset" type="button">Filter zurücksetzen</button></span></div>
<div class="grid" id="grid" data-mode="online"></div>
<noscript><ul class="rows">{static}</ul></noscript>
<div style="display:flex;justify-content:center;margin-top:44px"><button class="btn ghost" type="button" id="more" hidden>Mehr anzeigen</button></div>
<p class="note" style="margin-top:28px">Einladungslinks von Discord, Telegram und WhatsApp können ablaufen. Wir prüfen die Links regelmäßig. Fehlt eine Gruppe oder funktioniert ein Link nicht, schreib uns über die <a href="/kontakt/">Kontaktseite</a>.</p>
<div class="overlay" id="overlay" hidden><div class="modal" role="dialog" aria-modal="true" aria-labelledby="mTitle" id="modal"></div></div>'''
w('online/index.html',layout('online','/online/','Online-Communities: Discord, Reddit, Telegram und mehr | FindeDeineLeute.de',f'{len(on)} deutschsprachige Online-Communities auf Discord, Reddit, Telegram, in Foren und mehr, filterbar nach Plattform und Thema.',onbody))

# ---------- ÜBER UNS ----------
about='''<div class="split"><div class="prose"><span class="eyebrow">Über uns</span><h1 class="page-title">Wir bringen Gleichgesinnte zusammen.</h1>
<p>In jeder großen Stadt gibt es für fast jedes Interesse eine Gruppe. Das Problem ist, sie zu finden. Viele Communities leben in Chats, auf Aushängen oder von Mundpropaganda.</p>
<p>FindeDeineLeute.de sammelt sie an einem Ort, für alle 79 deutschen Städte mit mehr als 100.000 Einwohnern. Du siehst, wo sich Menschen treffen, und kommst mit einem Klick zur Community selbst. Wer lieber von zu Hause teilnimmt, findet Online-Gruppen gleich dazu.</p></div>
<div class="values">
<div class="value"><h3>Bestehende Gruppen</h3><p>Wir listen Communities, die es schon gibt: Run Clubs, Hackerspaces, Gartennetzwerke, Zeichengruppen, Radtouren und mehr.</p></div>
<div class="value"><h3>Alle Großstädte</h3><p>Von Berlin bis Kaiserslautern: Jede deutsche Stadt über 100.000 Einwohner hat ihre eigene Seite im Verzeichnis.</p></div>
<div class="value"><h3>Öffentlich recherchiert</h3><p>Die Einträge stammen aus öffentlich zugänglichen Informationen und den Seiten der Gruppen selbst.</p></div>
<div class="value"><h3>Alle zwei Wochen geprüft</h3><p>Wir prüfen die Links regelmäßig automatisch und blenden Gruppen aus, die nicht mehr erreichbar sind. Instagram und Facebook rufen wir dabei nicht automatisiert ab.</p></div>
<div class="value"><h3>Für alle Interessen</h3><p>Sport, Kunst, Technik, Engagement, Wellbeing: Wenn Menschen etwas verbindet, gehört es hierher.</p></div>
<div style="display:flex;gap:10px;flex-wrap:wrap;margin-top:24px"><a class="btn primary" href="/entdecken/">Communities entdecken</a><a class="btn ghost" href="/kontakt/?thema=eintragen">Community eintragen</a></div>
</div></div>'''
w('ueber-uns/index.html',layout('ueber-uns','/ueber-uns/','Über uns | FindeDeineLeute.de','FindeDeineLeute.de bringt Menschen mit Communities in ihrer Stadt und online zusammen.',about))

# ---------- KONTAKT ----------
kont='''<div class="contact"><div><span class="eyebrow">Anfrage</span><h1 class="page-title">Schreib uns.</h1>
<p class="page-sub">Fragen zum Verzeichnis, Feedback, eine Community eintragen oder eine Kooperation: Schick uns eine Anfrage. Wir antworten per E-Mail oder rufen dich zurück, ganz wie du möchtest.</p>
<a class="btn primary sm jump" href="#contactBox">Direkt zum Formular</a>
<div class="faq">
<details><summary>Ist die Nutzung kostenlos?</summary><p>Das Suchen und Finden von Communities ist für dich kostenlos. Einzelne Communities können Beiträge erheben, die du bei ihnen erfährst.</p></details>
<details><summary>Wie trage ich meine Community ein?</summary><p>Wähle im Formular das Thema "Meine Community eintragen" und beschreibe kurz deine Gruppe mit einem Link. Wir legen den Eintrag dann an und melden uns bei dir.</p></details>
<details><summary>Welche Städte deckt FindeDeineLeute.de ab?</summary><p>Alle 79 deutschen Großstädte mit mehr als 100.000 Einwohnern. Dazu kommen Online-Communities, die allen offen stehen.</p></details>
<details><summary>Sind die Angaben aktuell?</summary><p>Wir prüfen die Links alle zwei Wochen automatisch. Termine und Angaben können sich trotzdem ändern, bitte prüfe sie auf der verlinkten Seite der Community.</p></details>
</div></div>
<div class="formcard" id="contactBox"><form id="contactForm" class="stack-f" novalidate>
<div class="two"><div class="field"><label for="cName">Name</label><input class="input" id="cName" autocomplete="name"></div><div class="field"><label for="cMail">E-Mail</label><input class="input" id="cMail" type="email" autocomplete="email"></div></div>
<div class="field"><label for="cTopic">Worum geht es?</label><select class="select" id="cTopic"><option value="verzeichnis">Frage zum Verzeichnis</option><option value="feedback">Feedback oder Idee</option><option value="eintragen">Meine Community eintragen</option><option value="kooperation">Presse und Kooperationen</option></select></div>
<div class="field"><label id="cWayL">Wie sollen wir antworten?</label><div class="seg" role="group" aria-labelledby="cWayL" id="cWay"><button type="button" data-v="mail" aria-pressed="true">Per E-Mail</button><button type="button" data-v="call" aria-pressed="false">Rückruf</button></div></div>
<div id="callBox" hidden class="stack-f"><div class="two"><div class="field"><label for="cPhone">Telefonnummer</label><input class="input" id="cPhone" type="tel" autocomplete="tel" placeholder="z. B. 0151 12345678"></div><div class="field"><label for="cWhen">Wann erreichen wir dich?</label><select class="select" id="cWhen"><option>Vormittags</option><option>Mittags</option><option>Nachmittags</option><option>Abends</option><option>Egal, ich bin flexibel</option></select></div></div></div>
<div class="field"><label for="cMsg">Nachricht</label><textarea class="textarea" id="cMsg"></textarea></div>
<div class="err" id="cErr" role="alert"></div>
<button class="btn primary" type="submit">Anfrage vorbereiten</button>
<p class="note">Beim Absenden öffnet sich dein E-Mail-Programm mit der fertigen Anfrage. Bei einem Rückruf nutzen wir deine Telefonnummer ausschließlich dafür. Mehr dazu in der <a href="/datenschutz/">Datenschutzerklärung</a>.</p>
</form></div></div>'''
w('kontakt/index.html',layout('kontakt','/kontakt/','Anfrage und Kontakt | FindeDeineLeute.de','Schick uns eine Anfrage per E-Mail oder Rückruf: Fragen, Feedback, Community eintragen oder Kooperation.',kont))

# ---------- Weiterleitung alter Terminseite ----------
w('termin/index.html','<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="robots" content="noindex"><title>Weiterleitung</title><link rel="canonical" href="'+DOMAIN+'/kontakt/"><meta http-equiv="refresh" content="0; url=/kontakt/"></head><body><p><a href="/kontakt/">Weiter zur Anfrage</a></p></body></html>')

# ---------- RECHT ----------
imp='''<div class="legalwrap prose-l"><h1 class="page-title">Impressum</h1>
<p>Angaben gemäß § 5 DDG (Digitale-Dienste-Gesetz).</p>
<h2>Diensteanbieterin</h2>
<p>Nicole Emrich<br>Ammerndorfer Straße 22<br>90513 Zirndorf<br>Deutschland</p>
<h2>Kontakt</h2>
<p>E-Mail: <a href="mailto:nicky.nikaaa@gmail.com">nicky.nikaaa@gmail.com</a></p>
<h2>Verantwortlich für den Inhalt nach § 18 Abs. 2 MStV</h2>
<p>Nicole Emrich, Anschrift wie oben.</p>
<h2>Hinweis zum Angebot</h2>
<p>FindeDeineLeute.de ist ein Verzeichnis, das öffentlich verfügbare Informationen zu Communities in deutschen Städten und online zusammenstellt und auf die jeweiligen Angebote verlinkt. Die Einträge stammen aus verschiedenen öffentlichen Quellen. Für die Inhalte verlinkter externer Seiten sind ausschließlich deren Betreiber verantwortlich.</p>
<h2>Haftung für Inhalte</h2>
<p>Die Inhalte dieser Seiten wurden mit Sorgfalt zusammengestellt. Für Richtigkeit, Vollständigkeit und Aktualität der Angaben zu Terminen, Orten und Gruppen kann jedoch keine Gewähr übernommen werden. Als Diensteanbieterin bin ich gemäß § 7 Abs. 1 DDG für eigene Inhalte auf diesen Seiten nach den allgemeinen Gesetzen verantwortlich. Nach §§ 8 bis 10 DDG bin ich jedoch nicht verpflichtet, übermittelte oder gespeicherte fremde Informationen zu überwachen.</p>
<h2>Haftung für Links</h2>
<p>Dieses Angebot enthält Links zu externen Websites Dritter, auf deren Inhalte ich keinen Einfluss habe. Für diese fremden Inhalte ist stets der jeweilige Anbieter verantwortlich. Bei Bekanntwerden von Rechtsverletzungen werden entsprechende Links umgehend entfernt.</p>
<h2>Urheberrecht</h2>
<p>Namen, Marken und Logos der aufgeführten Communities und Quellen bleiben Eigentum der jeweiligen Rechteinhaber. Die Schrift Archivo wird unter der SIL Open Font License eingebunden.</p></div>'''
w('impressum/index.html',layout('','/impressum/','Impressum | FindeDeineLeute.de','Impressum von FindeDeineLeute.de',imp,noindex=True))
ds='''<div class="legalwrap prose-l"><h1 class="page-title">Datenschutzerklärung</h1>
<p>Stand: Oktober 2026</p>
<h2>1. Verantwortliche Stelle</h2>
<p>Verantwortlich für die Datenverarbeitung auf dieser Website ist:<br>Nicole Emrich, Ammerndorfer Straße 22, 90513 Zirndorf<br>E-Mail: <a href="mailto:nicky.nikaaa@gmail.com">nicky.nikaaa@gmail.com</a></p>
<h2>2. Grundsätzliches</h2>
<p>Der Schutz deiner personenbezogenen Daten ist mir wichtig. FindeDeineLeute.de kommt ohne Nutzerkonten, ohne Cookies und aktuell ohne Tracking- oder Analyse-Tools aus. Die Merkliste speichert deine Auswahl lokal in deinem Browser (siehe Abschnitt 5a). Es werden nur die Daten verarbeitet, die technisch zum Ausliefern und Anzeigen der Seite nötig sind.</p>
<h2>3. Hosting und Server-Logfiles</h2>
<p>Diese Website wird über GitHub Pages bereitgestellt, einen Dienst der GitHub, Inc. (88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, USA). Beim Aufruf der Seite verarbeitet GitHub aus technischen Gründen automatisch Zugriffsdaten, darunter deine IP-Adresse, Datum und Uhrzeit des Zugriffs sowie die angeforderte Datei. Rechtsgrundlage ist Art. 6 Abs. 1 lit. f DSGVO (berechtigtes Interesse an einer sicheren und funktionsfähigen Bereitstellung der Website).</p>
<h2>4. Schriften</h2>
<p>Die verwendete Schrift Inter wird von diesem Server selbst ausgeliefert. Beim Aufruf der Seite wird dafür keine Verbindung zu Google oder anderen Schriftdiensten aufgebaut.</p>
<h2>5. Kontaktaufnahme und Rückrufwunsch</h2>
<p>Wenn du das Anfrageformular nutzt, werden deine Eingaben nicht an einen Server von FindeDeineLeute.de gesendet. Stattdessen öffnet sich dein E-Mail-Programm mit einer vorbereiteten Nachricht, die du selbst absendest. Die Nachricht und die darin enthaltenen Angaben (Name, E-Mail-Adresse, Thema, Nachricht und, falls du einen Rückruf wünschst, Telefonnummer und gewünschte Erreichbarkeit) verarbeite ich ausschließlich, um deine Anfrage zu beantworten oder dich zurückzurufen. Rechtsgrundlage ist Art. 6 Abs. 1 lit. b DSGVO bzw. lit. f DSGVO. Die Daten werden gelöscht, sobald die Anfrage erledigt ist und keine gesetzlichen Aufbewahrungspflichten bestehen. Für den Versand gelten die Datenschutzbestimmungen deines E-Mail-Anbieters.</p>
<h2>5a. Merkliste und Kalender</h2>
<p>Wenn du bei einer Community auf das Herz tippst, speichert dein Browser diese Auswahl lokal im sogenannten Local Storage. Die Daten verlassen dein Gerät nicht und werden nicht an uns übertragen. Sie dienen ausschließlich dazu, die von dir gewünschte Funktion bereitzustellen (Rechtsgrundlage: Art. 6 Abs. 1 lit. f DSGVO in Verbindung mit § 25 Abs. 2 Nr. 2 TDDDG). Du kannst die Daten jederzeit löschen, indem du Einträge von der Merkliste entfernst oder den Browserspeicher leerst. Wenn du eine Merkliste als Link teilst, sind die ausgewählten Communities im Link enthalten. Der Kalender-Export erzeugt eine Datei direkt in deinem Browser, ohne Übertragung an uns.</p>
<h2>5b. Newsletter</h2>
<p>Wenn du dich zum Newsletter anmeldest, öffnet sich dein E-Mail-Programm mit einer vorbereiteten Nachricht. Wir verwenden deine E-Mail-Adresse und, falls angegeben, deine Stadt ausschließlich, um dir den Newsletter zu senden (Rechtsgrundlage: Einwilligung nach Art. 6 Abs. 1 lit. a DSGVO). Du kannst jederzeit per E-Mail an <a href="mailto:nicky.nikaaa@gmail.com">nicky.nikaaa@gmail.com</a> widerrufen. Wir tragen dich nach deiner Nachricht manuell in den Verteiler ein und bestätigen das per Antwort. Sobald wir einen Newsletter-Dienst einsetzen, ergänzen wir diese Erklärung um den Anbieter.</p>
<h2>6. Externe Links</h2>
<p>FindeDeineLeute.de verlinkt auf externe Seiten der aufgeführten Communities und Quellen. Sobald du einen solchen Link anklickst, verlässt du diese Website. Für die Datenverarbeitung auf den Zielseiten gelten deren eigene Datenschutzbestimmungen.</p>
<h2>7. Cookies, Tracking, Analyse</h2>
<p>Diese Website setzt keine Cookies (die lokal gespeicherte Merkliste ist kein Cookie), verwendet aktuell keine Analyse-, Tracking- oder Werbe-Tools und bindet keine Social-Media-Plugins ein.</p>
<p>Beim ersten Besuch zeigt die Seite ein Einwilligungs-Banner. Deine Auswahl wird lokal in deinem Browser gespeichert (Schlüssel „fdl_consent“, ohne Übertragung an einen Server) und dient nur dazu, deine Entscheidung zu merken. Sie ist technisch notwendig und erfordert keine Einwilligung (§ 25 Abs. 2 Nr. 2 TDDDG). Optionale Dienste wie eine anonyme Reichweitenmessung würden erst nach deiner Zustimmung aktiviert. Du kannst deine Auswahl jederzeit über „Cookie-Einstellungen“ im Footer ändern oder widerrufen.</p>
<h2>8. Übermittlung in Drittländer</h2>
<p>GitHub hat seinen Sitz in den USA. Eine Datenübermittlung dorthin erfolgt nur, soweit sie für die Auslieferung der Seiteninhalte erforderlich ist. Der Anbieter stützt sich dabei in der Regel auf geeignete Garantien, zum Beispiel EU-Standardvertragsklauseln oder das EU-US Data Privacy Framework.</p>
<h2>9. Deine Rechte</h2>
<p>Dir stehen nach der DSGVO folgende Rechte zu: Auskunft (Art. 15), Berichtigung (Art. 16), Löschung (Art. 17), Einschränkung der Verarbeitung (Art. 18), Datenübertragbarkeit (Art. 20) sowie Widerspruch gegen die Verarbeitung (Art. 21). Wende dich dazu an die oben genannte verantwortliche Stelle. Außerdem hast du das Recht, dich bei einer Datenschutz-Aufsichtsbehörde zu beschweren, zum Beispiel beim Bayerischen Landesamt für Datenschutzaufsicht (BayLDA).</p>
<h2>10. Aktualität</h2>
<p>Diese Datenschutzerklärung wird angepasst, sobald sich an der Datenverarbeitung etwas ändert, zum Beispiel durch neue Funktionen oder Dienste.</p></div>'''
w('datenschutz/index.html',layout('','/datenschutz/','Datenschutz | FindeDeineLeute.de','Datenschutzerklärung von FindeDeineLeute.de',ds,noindex=True))


# ---------- KALENDER ----------
cal_cities=sorted({x['t'] for x in CALIT},key=lambda n:[c for c,_ in cities].index(n))
cal_opts=''.join('<option value="%s">%s (%d)</option>'%(SLUG[n],E(n),len(CAL_BY_CITY[n])) for n in cal_cities)
kal=f"""<div class="pagehead"><span class="eyebrow">Kalender</span><h1 class="page-title">Diese Woche in deiner Stadt</h1>
<p class="page-sub">Regelmäßige Treffen aus dem Verzeichnis, sortiert nach Datum. Wähle deine Stadt und füge Termine mit einem Klick zu deinem Kalender hinzu.</p></div>
<div class="filters" style="margin-bottom:28px"><div class="frow cal"><div class="field"><label for="calCity">Stadt</label><select class="select" id="calCity"><option value="">Alle Städte</option>{cal_opts}</select></div>
<div class="field"><label id="calRL">Zeitraum</label><div class="seg" role="group" aria-labelledby="calRL" id="calRange"><button data-v="7" aria-pressed="true">7 Tage</button><button data-v="14" aria-pressed="false">14 Tage</button><button data-v="31" aria-pressed="false">Monat</button></div></div></div></div>
<div id="calBox" class="cal-box"><p class="note">Lade Termine …</p></div>
<noscript><p class="lede">Für den Kalender brauchst du JavaScript. Alle Gruppen mit ihren Zeiten findest du auf den <a href="/staedte/">Seiten der Städte</a>.</p></noscript>
<p class="note" style="margin-top:28px">Im Kalender stehen {len(CALIT)} Gruppen mit festen, wiederkehrenden Terminen in {len(cal_cities)} Städten. Nicht jede Gruppe veröffentlicht feste Zeiten, deshalb ist die Liste noch nicht vollständig. Termine können ausfallen oder sich verschieben, bitte prüfe sie vor dem Besuch bei der Community. Fehlt ein Termin? <a href="/kontakt/?thema=eintragen">Schick uns eine kurze Nachricht</a>.</p>"""
w('kalender/index.html',layout('kalender','/kalender/','Kalender: Communities und Treffen in deiner Stadt | FindeDeineLeute.de','Wiederkehrende Treffen aus deiner Stadt für die nächsten Tage: Run Clubs, Critical Mass, Stammtische und mehr. Mit Kalender-Export.',kal))

# ---------- MERKLISTE ----------
mk="""<div class="pagehead"><span class="eyebrow">Merkliste</span><h1 class="page-title">Deine gemerkten Communities</h1>
<p class="page-sub">Tippe bei einer Community auf das Herz, dann landet sie hier. Du kannst die Liste als Link teilen, zum Beispiel per WhatsApp an Freunde, die mitkommen sollen.</p></div>
<div id="mlBanner"></div><div id="mlBar" class="share-bar" hidden></div>
<div class="grid" id="mlGrid"><p class="note">Lade Merkliste …</p></div>
<p class="note" style="margin-top:28px">Deine Merkliste wird nur in deinem Browser gespeichert und nicht an uns übertragen. Wenn du den Browserspeicher löschst oder ein anderes Gerät nutzt, ist sie weg. Zum Mitnehmen kannst du sie als Link teilen.</p>"""
w('merkliste/index.html',layout('merkliste','/merkliste/','Merkliste | FindeDeineLeute.de','Deine gemerkten Communities, zum Teilen als Link.',mk,noindex=True))

# ---------- AUSWERTUNG ----------
_cnt=collections.Counter(e['t'] for e in data if e['t']!='Online')
_div={c:len({e['c'] for e in by_city[c]}) for c in by_city if c!='Online'}
_top=_cnt.most_common(10)
_topdiv=sorted(_div.items(),key=lambda kv:(-kv[1],-_cnt[kv[0]]))[:10]
_catlead=[]
for cid in CAT:
    cc=collections.Counter(e['t'] for e in data if e['c']==cid and e['t']!='Online')
    if cc:
        n,v=cc.most_common(1)[0]
        _catlead.append((cid,n,v,sum(cc.values())))
_catlead.sort(key=lambda x:-x[3])
def _li(a,b,c=''): return '<li class="row"><div class="rb"><h3>%s</h3></div><div class="ra"><span class="pill off">%s</span></div></li>'%(E(a),E(b))
auswertung=f"""<div class="pagehead"><span class="eyebrow">Auswertung</span><h1 class="page-title">Was es wo gibt: Communities in deutschen Großstädten</h1>
<p class="page-sub">Eine Auswertung der {format(len(data),',').replace(',','.')} Einträge im Verzeichnis von FindeDeineLeute.de. Stand {fdate(TODAY)}.</p></div>
<div class="prose-l" style="max-width:760px"><p class="lede"><b>Wichtig vorab:</b> Die Zahlen zeigen, was im Verzeichnis steht, nicht, wie viele Gruppen es in der Stadt wirklich gibt. Das Verzeichnis wächst, manche Städte sind bereits sehr gut abgedeckt, andere erst am Anfang. Die Auswertung ist deshalb ein Zwischenstand und kein Städte-Ranking.</p></div>
<section class="csec"><h2>Städte mit den meisten Einträgen</h2><ul class="rows">{''.join(_li(n,'%d Einträge'%v) for n,v in _top)}</ul></section>
<section class="csec"><h2>Städte mit den meisten verschiedenen Kategorien</h2><ul class="rows">{''.join(_li(n,'%d von %d Kategorien'%(v,len(CAT))) for n,v in _topdiv)}</ul></section>
<section class="csec"><h2>Wo es welche Art von Gruppe am häufigsten gibt</h2><ul class="rows">{''.join(_li(CAT[cid],'%s (%d von %d)'%(n,v,tot)) for cid,n,v,tot in _catlead)}</ul></section>
<section class="csec"><h2>Online-Communities</h2><p class="lede">{len(onl_all)} Gruppen sind unabhängig vom Ort erreichbar. Die häufigsten Plattformen: {', '.join('%s (%d)'%(PLAT[k],n) for k,n in collections.Counter(e.get('p') for e in onl_all).most_common(4) if k in PLAT)}.</p></section>
<p class="note" style="margin-top:28px">Quelle: eigenes Verzeichnis aus öffentlich zugänglichen Angaben, alle zwei Wochen automatisch auf Erreichbarkeit geprüft. Wer die Zahlen zitieren möchte, nennt bitte FindeDeineLeute.de und verlinkt auf diese Seite. Rückfragen und Daten für Journalistinnen und Journalisten gibt es im <a href="/presse/">Pressebereich</a>.</p>"""
w('auswertung/index.html',layout('auswertung','/auswertung/','Auswertung: Communities in deutschen Großstädten | FindeDeineLeute.de','Welche Arten von Gruppen es in welchen Großstädten gibt: Zwischenstand aus dem Verzeichnis von FindeDeineLeute.de.',auswertung))

# ---------- PRESSE ----------
presse=f"""<div class="pagehead"><span class="eyebrow">Presse</span><h1 class="page-title">Presse und Medien</h1>
<p class="page-sub">Alles, was du für einen Beitrag über FindeDeineLeute.de brauchst: Kurzbeschreibung, Zahlen, Logo und Ansprechpartnerin.</p></div>
<section class="csec"><h2>Kurzbeschreibung</h2><p class="lede">FindeDeineLeute.de ist ein kostenloses Verzeichnis für Gruppen und Communities in allen {len(cities)} deutschen Großstädten mit mehr als 100.000 Einwohnern sowie online. Wer neu in der Stadt ist, Gleichgesinnte sucht oder aus der Einsamkeit herauswill, findet Run Clubs, Hobbygruppen, Stammtische und Online-Gemeinschaften nach Stadt und Thema.</p>
<p class="lede">Das Verzeichnis ist unabhängig, werbefrei und ohne Nutzerkonto nutzbar. Die Links werden alle zwei Wochen automatisch geprüft.</p></section>
<section class="csec"><h2>Zahlen im Überblick</h2><ul class="rows"><li class="row"><div class="rb"><h3>{format(len(data),',').replace(',','.')} Einträge</h3><div class="sub">davon {len(onl_all)} Online-Communities</div></div></li><li class="row"><div class="rb"><h3>{len(cities)} Städte</h3><div class="sub">alle deutschen Großstädte über 100.000 Einwohner</div></div></li><li class="row"><div class="rb"><h3>{len(CAT)} Kategorien</h3><div class="sub">von Sport über Kunst bis Familie, Tiere und Reisen</div></div></li></ul>
<p class="note" style="margin-top:14px">Details und Einschränkungen stehen in der <a href="/auswertung/">Auswertung</a>.</p></section>
<section class="csec"><h2>Logo und Material</h2><p class="lede">Du darfst das Logo für redaktionelle Berichterstattung über FindeDeineLeute.de verwenden.</p>
<div class="actions" style="display:flex;gap:10px;flex-wrap:wrap;margin-top:16px"><a class="btn ghost" href="/assets/logo-symbol.svg" download>Logo-Symbol (SVG)</a><a class="btn ghost" href="/assets/logo-findedeineleute.png" download>Logo mit Schriftzug (PNG)</a><a class="btn ghost" href="/assets/og.png" download>Vorschaubild (PNG)</a></div></section>
<section class="csec"><h2>Ansprechpartnerin</h2><p class="lede">Nicole Emrich, Gründerin<br><a href="mailto:{CF_EMAIL}?subject=Presseanfrage%20FindeDeineLeute.de">{CF_EMAIL}</a></p>
<p class="note" style="margin-top:12px">Gerne liefern wir Zahlen für einzelne Städte, Hintergründe zum Thema Einsamkeit und Gesprächspartner.</p></section>"""
w('presse/index.html',layout('presse','/presse/','Presse | FindeDeineLeute.de','Pressebereich von FindeDeineLeute.de: Kurzbeschreibung, Zahlen, Logo und Kontakt.',presse))

# ---------- NEWSLETTER ----------
nl=f"""<div class="contact"><div><span class="eyebrow">Newsletter</span><h1 class="page-title">Neu in deiner Stadt</h1>
<p class="page-sub">Einmal im Monat: neue Gruppen, Termine und ein Tipp, wie du leichter Anschluss findest. Kein Spam, jederzeit abbestellbar.</p>
<div class="faq"><details><summary>Wie läuft die Anmeldung?</summary><p>Beim Absenden öffnet sich dein E-Mail-Programm mit einer fertigen Nachricht. Wir tragen dich dann ein und bestätigen das kurz per Antwort. Erst danach bekommst du den Newsletter.</p></details>
<details><summary>Welche Daten braucht ihr?</summary><p>Deine E-Mail-Adresse und, wenn du magst, deine Stadt, damit wir passende Tipps schicken. Mehr nicht. Details stehen in der <a href="/datenschutz/">Datenschutzerklärung</a>.</p></details>
<details><summary>Wie bestelle ich ab?</summary><p>Schreib uns eine kurze Nachricht an {CF_EMAIL}, wir streichen dich sofort aus dem Verteiler.</p></details></div></div>
<div class="formcard" id="nlBox"><form id="nlForm" class="stack-f" novalidate>
<div class="field"><label for="nlMail">E-Mail-Adresse</label><input class="input" id="nlMail" name="email" type="email" autocomplete="email" required></div>
<div class="field"><label for="nlCity">Deine Stadt (optional)</label><select class="select" id="nlCity"><option value="">Keine Angabe</option>{opts}</select></div>
<label class="check"><input type="checkbox" id="nlOk" required> <span>Ich möchte den Newsletter von FindeDeineLeute.de erhalten und habe die <a href="/datenschutz/">Datenschutzerklärung</a> gelesen.</span></label>
<p class="err" id="nlErr" role="alert"></p>
<button class="btn primary" type="submit">Anmelden</button></form></div></div>"""
w('newsletter/index.html',layout('newsletter','/newsletter/','Newsletter: Neu in deiner Stadt | FindeDeineLeute.de','Einmal im Monat neue Gruppen, Termine und Tipps für deine Stadt. Kostenlos und jederzeit abbestellbar.',nl))

# ---------- 404 ----------
w('404.html',layout('','/404.html','Seite nicht gefunden | FindeDeineLeute.de','Diese Seite gibt es nicht.','<div class="pagehead"><h1 class="page-title">Seite nicht gefunden</h1><p class="page-sub">Diese Adresse gibt es nicht. Vielleicht hilft dir die Suche weiter.</p><div style="display:flex;gap:10px;margin-top:28px;flex-wrap:wrap"><a class="btn primary" href="/entdecken/">Communities entdecken</a><a class="btn ghost" href="/staedte/">Alle Städte</a></div></div>',noindex=True))

# ---------- Daten, Sitemap, robots, CNAME ----------

pub=[]
_keys=set()
for e in data:
    d={k:v for k,v in e.items() if k!='s'}
    if e['s']=='criticalmass.de': d['a']=''
    d['k']=stable_key(e)
    assert d['k'] not in _keys,e['n']
    _keys.add(d['k'])
    pub.append(d)
w('calendar.json',json.dumps({'updated':LASTRUN or TODAY,'items':CALIT},ensure_ascii=False,separators=(',',':')))
w('communities.json',json.dumps({"updated":LASTRUN or TODAY,"cities":cities,"items":pub},ensure_ascii=False,separators=(',',':')))
urls=['/','/entdecken/','/staedte/','/online/','/ki/','/kalender/','/auswertung/','/presse/','/newsletter/','/ratgeber/']+['/ratgeber/%s/'%a['slug'] for a in ARTICLES]+combo_pages+aktuell_pages+['/%s/'%s for _,s in cities]+['/ueber-uns/','/kontakt/']
sm='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join('<url><loc>%s%s</loc><lastmod>%s</lastmod></url>\n'%(DOMAIN,u,TODAY) for u in urls)+'</urlset>\n'
w('sitemap.xml',sm)
w('robots.txt','User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n'%DOMAIN)
w('CNAME','findedeineleute.de\n')
w('.nojekyll','')
print('pages',len(urls)+3,'items',N)
