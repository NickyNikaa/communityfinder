# -*- coding: utf-8 -*-
import json,html,os,shutil,datetime,collections,sys
ROOT=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,ROOT)
from static_data import CITIES as CITYTXT
DOMAIN='https://findedeineleute.de'
TODAY=datetime.date.today().isoformat()
try: LASTRUN=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'data','state.json'),encoding='utf8')).get('last_run','')
except Exception: LASTRUN=''
OUT=os.environ.get('OUT',os.path.join(os.path.dirname(ROOT),'dist'))
if os.path.exists(OUT): shutil.rmtree(OUT)
os.makedirs(OUT)
shutil.copytree(ROOT+'/assets',OUT+'/assets')
E=html.escape
data=json.load(open(ROOT+'/data/data.json',encoding='utf8'))
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

NAV=[('/','Start','start'),('/entdecken/','Entdecken','entdecken'),('/online/','Online','online'),('/staedte/','Städte','staedte'),('/ueber-uns/','Über uns','ueber-uns'),('/kontakt/','Kontakt','kontakt')]
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
<link rel="preload" href="/assets/fonts/archivo-latin-300-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/styles.css">
{extra_head}{ld}
</head>
<body>
<a class="skip" href="#main">Zum Inhalt springen</a>
<div class="wrap">
<header class="top"><div class="bar">
<a class="brand" href="/" aria-label="FindeDeineLeute.de, zur Startseite">FindeDeineLeute.de</a>
<button class="menu-btn" id="menuBtn" aria-expanded="false" aria-controls="mainNav">Menü</button>
<nav class="main" id="mainNav" aria-label="Hauptnavigation">{nav}<a class="btn primary sm" href="/kontakt/">Anfrage senden</a></nav>
</div></header>
<main id="main">
{body}
</main>
<footer>
<div><b style="font-family:var(--f-display);font-size:18px;font-weight:500;color:var(--ink)">FindeDeineLeute.de</b><p style="margin-top:10px;max-width:34ch">Das Verzeichnis für Communities in allen deutschen Großstädten und online.</p></div>
<div class="cols">
<div><h4>Entdecken</h4><ul><li><a href="/entdecken/">Alle Communities</a></li><li><a href="/staedte/">Alle Städte</a></li><li><a href="/online/">Online-Communities</a></li></ul></div>
<div><h4>Städte</h4><ul>{topc}</ul></div>
<div><h4>Mehr</h4><ul><li><a href="/ueber-uns/">Über uns</a></li><li><a href="/kontakt/">Kontakt</a></li><li><a href="/impressum/">Impressum</a></li><li><a href="/datenschutz/">Datenschutz</a></li></ul></div>
</div>
<div class="legal">© {datetime.date.today().year} FindeDeineLeute.de. Die Einträge stammen aus öffentlich zugänglichen Verzeichnissen und verlinken auf die jeweiligen Communities.</div>
</footer>
</div>
<script src="/assets/config.js"></script>
<script src="/assets/app.js" defer></script>
</body>
</html>
'''

def card(c):
    href='/%s/#c%d'%(SLUG.get(c['t'],''),c['i']) if c['t'] in SLUG else (c['l'] or '#')
    place='Online' if c['t']=='Online' else c['t']+(' · '+c['a'] if c['a'] and c['s']!='criticalmass.de' else '')
    pl='<span>%s</span>'%E(PLAT.get(c.get('p'),'')) if c.get('p') and c['p']!='website' else ''
    note=E(' · '.join(x for x in [c['w'],('Quelle: '+c['s'].split(',')[0]) if c['s'] else ''] if x))
    return ('<article class="card"><div class="tag"><span>'+('Online' if c['f']=='online' else 'Vor Ort')+'</span><span>'+E(CAT[c['c']])+'</span>'+pl+'</div><h3><a href="'+href+'">'+E(c['n'])+'</a></h3><div class="sub">'+E(place)+'</div><p class="d">'+E(c['x'])+'</p><div class="note">'+note+'</div></article>')
byname={e['n']:e for e in data}
def pick(names): return [byname[n] for n in names if n in byname]

# ---------- START ----------
onl_all=[e for e in data if e['f']=='online']
opts=''.join('<option value="%s">%s</option>'%(E(n),E(n)) for n,_ in cities)
stack=''.join('<div class="mini"><div><b>%s</b><span class="s">%s · %s</span></div></div>'%(E(c['n']),E(c['t']),E(CAT[c['c']])) for c in pick(['Hasenheide parkrun','Chaosdorf Düsseldorf','Urban Sketchers Hamburg']))
feat=''.join(card(c) for c in pick(['Critical Mass Hamburg','Urban Sketchers Köln','Entropia Karlsruhe','Netzwerk Leipziger Gemeinschaftsgärten']))
cg=''.join('<a class="cityb" href="/%s/"><span>%s</span><i>%d</i></a>'%(s,E(n),len(by_city[n])) for n,s in cities[:16])
chips=''.join('<a class="chip" href="/entdecken/?kategorie=%s">%s</a>'%(i,E(CAT[i])) for i in ['sport','outdoor','kunst','tech','spiele','engagement','queer'])
onchips=''.join('<a class="chip" href="/online/?plattform=%s">%s <i>%d</i></a>'%(k,PLAT[k],n) for k,n in collections.Counter(e.get('p') for e in onl_all).most_common() if k in PLAT)
start=f'''<div class="hero">
<div>
<span class="eyebrow">Community Hub für Deutschland</span>
<h1>Finde Menschen, die deine <em>Leidenschaft</em> teilen.</h1>
<p class="lead">FindeDeineLeute.de ist das Verzeichnis für Communities in allen deutschen Großstädten und online. Ob Run Club, Hackerspace oder Gartennetzwerk: Such dir aus, wo du dazugehören willst.</p>
<form class="search" action="/entdecken/" method="get" role="search">
<input name="q" type="search" placeholder="Thema, z. B. Laufen" aria-label="Community suchen">
<select name="stadt" class="select" aria-label="Stadt wählen"><option value="">Alle Städte</option>{opts}</select>
<button class="btn primary" type="submit">Suchen</button>
</form>
<p class="note" style="margin-top:18px">{N-len(onl_all):,} Communities in {len(cities)} Städten und {len(onl_all)} Online-Gruppen</p>
<div class="chips" style="margin-top:26px">{chips}</div>
</div>
<div class="stack" aria-label="Beispiele aus dem Verzeichnis">{stack}</div>
</div>
<section class="section"><div class="section-head"><div><span class="eyebrow">Gerade beliebt</span><h2>Communities zum Reinschnuppern</h2></div><a class="btn ghost" href="/entdecken/">Alle ansehen</a></div><div class="grid">{feat}</div></section>
<section class="section"><div class="section-head"><div><span class="eyebrow">Online</span><h2>Communities ohne Ortsgrenze</h2></div><a class="btn ghost" href="/online/">Alle Online-Communities</a></div><div class="chips">{onchips}</div></section>
<section class="section"><div class="section-head"><div><span class="eyebrow">Städte</span><h2>Die größten Städte</h2></div><a class="btn ghost" href="/staedte/">Alle {len(cities)} Städte</a></div><div class="citygrid">{cg}</div></section>
<section class="section"><div class="section-head"><div><span class="eyebrow">So funktioniert es</span><h2>In drei Schritten dabei</h2></div></div>
<div class="steps"><div class="step"><h3>Suchen</h3><p>Wähle deine Stadt, ein Thema oder Online. Die Suche durchsucht Namen, Beschreibungen und Themen.</p></div><div class="step"><h3>Reinschnuppern</h3><p>Jeder Eintrag verlinkt auf die Community selbst und nennt die Quelle. Dort siehst du aktuelle Termine und kannst Kontakt aufnehmen.</p></div><div class="step"><h3>Dabeibleiben</h3><p>Gefällt es dir, wirst du Teil der Gruppe. Passt es nicht, probierst du die nächste aus.</p></div></div></section>
<section class="section"><div class="band"><div><h2>Du leitest eine Community?</h2><p>Trag deine Gruppe bei FindeDeineLeute.de ein und werde von Menschen gefunden, die genau dein Thema suchen. Schick uns eine kurze Anfrage, wir melden uns bei dir.</p></div><a class="btn" href="/kontakt/?thema=eintragen">Anfrage senden</a></div></section>'''
org={"@context":"https://schema.org","@type":"Organization","name":"FindeDeineLeute.de","url":DOMAIN+"/","logo":DOMAIN+"/assets/favicon.svg"}
wsite={"@context":"https://schema.org","@type":"WebSite","name":"FindeDeineLeute.de","url":DOMAIN+"/","inLanguage":"de","potentialAction":{"@type":"SearchAction","target":DOMAIN+"/entdecken/?q={search_term_string}","query-input":"required name=search_term_string"}}
w('index.html',layout('start','/','FindeDeineLeute.de | Communities in deiner Stadt und online finden',f'Finde Communities in allen {len(cities)} deutschen Großstädten und online: Run Clubs, Hackerspaces, Gartennetzwerke, Zeichengruppen und mehr.',start,jsonld=[wsite,org]))

# ---------- ENTDECKEN ----------
entd='''<div class="pagehead"><span class="eyebrow">Verzeichnis</span><h1 class="page-title">Communities entdecken</h1><p class="page-sub">Suche nach Themen oder wähle deine Stadt. Alle Filter wirken sofort, du musst nichts bestätigen. Kategorien kannst du kombinieren.</p></div>
<div class="filters"><div class="frow">
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
<p class="note" style="margin-top:28px">Die Einträge stammen aus öffentlich zugänglichen Quellen, wo möglich nennen wir die Quelle beim Eintrag. Alle zwei Wochen prüfen wir die Links automatisch und blenden Einträge aus, die nicht mehr erreichbar sind. Termine und Angaben können sich ändern, bitte prüfe sie vor dem Besuch bei der Community.</p>
<div class="overlay" id="overlay" hidden><div class="modal" role="dialog" aria-modal="true" aria-labelledby="mTitle" id="modal"></div></div>'''
w('entdecken/index.html',layout('entdecken','/entdecken/','Communities entdecken | FindeDeineLeute.de','Durchsuche Communities in allen deutschen Großstädten und online nach Thema, Stadt und Kategorie.',entd))

# ---------- STÄDTE ----------
alls=''.join('<a href="/%s/"><span>%s</span><i>%d</i></a>'%(s,E(n),len(by_city[n])) for n,s in cities)
w('staedte/index.html',layout('staedte','/staedte/','Alle Städte | FindeDeineLeute.de',f'Communities in allen {len(cities)} deutschen Großstädten mit mehr als 100.000 Einwohnern.',
 f'<div class="pagehead"><span class="eyebrow">Städte</span><h1 class="page-title">Communities nach Stadt</h1><p class="page-sub">Wähle deine Stadt. Die Zahl zeigt, wie viele Communities im Verzeichnis stehen. Aufgeführt sind alle deutschen Städte mit mehr als 100.000 Einwohnern, sortiert nach Größe.</p></div><div class="cities-all">{alls}</div><div style="height:48px"></div>'))

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
            rows+='<li class="row" id="c%d"><div class="rb"><h3>%s</h3>%s<p class="d">%s</p>%s</div><div class="ra">%s</div></li>'%(
                e['i'],E(e['n']),('<div class="sub">%s</div>'%E(sub)) if sub else '',E(e['x']),('<p class="note">Quelle: %s</p>'%E(e['s'])) if e['s'] else '',
                ('<a class="btn ghost sm" href="%s" target="_blank" rel="noopener noreferrer" aria-label="%s: Zur Community">Zur Community</a>'%(E(e['l']),E(e['n']))) if e['l'] else '')
        secs+='<section class="csec" id="k-%s"><h2>%s</h2><ul class="rows">%s</ul></section>'%(cid,E(CAT[cid]),rows)
    intro=city_intro(city,items)
    others=''.join('<a class="cityb" href="/%s/"><span>%s</span><i>%d</i></a>'%(s,E(n),len(by_city[n])) for n,s in cities if n!=city)[:0]
    near=[(n,s) for n,s in cities[:14] if n!=city][:12]
    others=''.join('<a class="cityb" href="/%s/"><span>%s</span><i>%d</i></a>'%(s,E(n),len(by_city[n])) for n,s in near)
    body=f'''<nav class="crumbs" aria-label="Brotkrumen"><a href="/">Start</a><span>/</span><a href="/staedte/">Städte</a><span>/</span><span>{E(city)}</span></nav>
<div class="pagehead" style="padding-top:24px"><h1 class="page-title" style="margin-top:0">Communities in {E(city)}</h1><p class="lede">{E(intro[0])}</p>{('<p class="lede">%s</p>'%E(intro[1])) if intro[1] else ''}<div class="catnav" aria-label="Kategorien in {E(city)}">{nav}</div></div>
{secs}
<section class="section" style="border-bottom:0"><div class="band"><div><h2>Deine Community fehlt in {E(city)}?</h2><p>Trag sie ein, damit andere sie finden.</p></div><a class="btn" href="/kontakt/?thema=eintragen">Anfrage senden</a></div></section>
<section class="section" style="border-bottom:0;padding-top:0"><div class="section-head"><div><span class="eyebrow">Weitere Städte</span></div><a class="btn ghost sm" href="/staedte/">Alle Städte</a></div><div class="citygrid">{others}</div></section>'''
    desc=f'{len(items)} Communities in {city}: {", ".join(CAT[c] for c in list(cats)[:3])} und mehr. Finde Gruppen und Gleichgesinnte in deiner Stadt.'
    ld=[{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Start","item":DOMAIN+"/"},{"@type":"ListItem","position":2,"name":"Städte","item":DOMAIN+"/staedte/"},{"@type":"ListItem","position":3,"name":city,"item":f"{DOMAIN}/{slug}/"}]},
        {"@context":"https://schema.org","@type":"ItemList","name":f"Communities in {city}","numberOfItems":len(items),"itemListElement":[{"@type":"ListItem","position":k+1,"name":e['n'],**({"url":e['l']} if e['l'] else {})} for k,e in enumerate(items[:50])]}]
    w(f'{slug}/index.html',layout('staedte',f'/{slug}/',f'Communities in {city} | FindeDeineLeute.de',desc,body,jsonld=ld))

# ---------- ONLINE ----------
on=sorted([e for e in data if e['f']=='online'],key=lambda e:(-e['q'],e['n'].lower()))
pc=collections.Counter(e.get('p') for e in on)
static=''.join('<li class="row"><div class="rb"><h3>%s</h3><p class="d">%s</p><p class="note">%s%s</p></div><div class="ra">%s</div></li>'%(E(e['n']),E(e['x']),E(PLAT.get(e.get('p'),'')),(' · Quelle: '+E(e['s'])) if e['s'] else '',('<a class="btn ghost sm" href="%s" target="_blank" rel="noopener noreferrer">Zur Community</a>'%E(e['l'])) if e['l'] else '') for e in on[:200])
onbody=f'''<div class="pagehead"><span class="eyebrow">Online</span><h1 class="page-title">Online-Communities</h1><p class="page-sub">{len(on)} Gruppen, Server und Foren, an denen du von überall teilnehmen kannst: Discord, Reddit, Telegram, Foren und mehr. Alle Filter wirken sofort.</p></div>
<div class="filters"><div class="frow online">
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
<div class="value"><h3>Transparente Quellen</h3><p>Die Einträge stammen aus öffentlichen Verzeichnissen und den Seiten der Gruppen selbst, etwa von socialrunclubs.de, ccc.de, criticalmass.de, Meetup, Reddit oder Discord.</p></div>
<div class="value"><h3>Alle zwei Wochen geprüft</h3><p>Wir prüfen die Links regelmäßig automatisch und blenden Gruppen aus, die nicht mehr erreichbar sind. Instagram und Facebook rufen wir dabei nicht automatisiert ab.</p></div>
<div class="value"><h3>Für alle Interessen</h3><p>Sport, Kunst, Technik, Engagement, Wellbeing: Wenn Menschen etwas verbindet, gehört es hierher.</p></div>
<div style="display:flex;gap:10px;flex-wrap:wrap;margin-top:24px"><a class="btn primary" href="/entdecken/">Communities entdecken</a><a class="btn ghost" href="/kontakt/?thema=eintragen">Community eintragen</a></div>
</div></div>'''
w('ueber-uns/index.html',layout('ueber-uns','/ueber-uns/','Über uns | FindeDeineLeute.de','FindeDeineLeute.de bringt Menschen mit Communities in ihrer Stadt und online zusammen.',about))

# ---------- KONTAKT ----------
kont='''<div class="contact"><div><span class="eyebrow">Anfrage</span><h1 class="page-title">Schreib uns.</h1>
<p class="page-sub">Fragen zum Verzeichnis, Feedback, eine Community eintragen oder eine Kooperation: Schick uns eine Anfrage. Wir antworten per E-Mail oder rufen dich zurück, ganz wie du möchtest.</p>
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
<p>E-Mail: <a href="mailto:nicoleemrich@outlook.com">nicoleemrich@outlook.com</a></p>
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
<p>Verantwortlich für die Datenverarbeitung auf dieser Website ist:<br>Nicole Emrich, Ammerndorfer Straße 22, 90513 Zirndorf<br>E-Mail: <a href="mailto:nicoleemrich@outlook.com">nicoleemrich@outlook.com</a></p>
<h2>2. Grundsätzliches</h2>
<p>Der Schutz deiner personenbezogenen Daten ist mir wichtig. FindeDeineLeute.de kommt ohne Nutzerkonten, ohne Cookies und ohne Tracking- oder Analyse-Tools aus. Es werden nur die Daten verarbeitet, die technisch zum Ausliefern und Anzeigen der Seite nötig sind.</p>
<h2>3. Hosting und Server-Logfiles</h2>
<p>Diese Website wird über GitHub Pages bereitgestellt, einen Dienst der GitHub, Inc. (88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, USA). Beim Aufruf der Seite verarbeitet GitHub aus technischen Gründen automatisch Zugriffsdaten, darunter deine IP-Adresse, Datum und Uhrzeit des Zugriffs sowie die angeforderte Datei. Rechtsgrundlage ist Art. 6 Abs. 1 lit. f DSGVO (berechtigtes Interesse an einer sicheren und funktionsfähigen Bereitstellung der Website).</p>
<h2>4. Schriften</h2>
<p>Die verwendete Schrift Archivo wird von diesem Server selbst ausgeliefert. Beim Aufruf der Seite wird dafür keine Verbindung zu Google oder anderen Schriftdiensten aufgebaut.</p>
<h2>5. Kontaktaufnahme und Rückrufwunsch</h2>
<p>Wenn du das Anfrageformular nutzt, werden deine Eingaben nicht an einen Server von FindeDeineLeute.de gesendet. Stattdessen öffnet sich dein E-Mail-Programm mit einer vorbereiteten Nachricht, die du selbst absendest. Die Nachricht und die darin enthaltenen Angaben (Name, E-Mail-Adresse, Thema, Nachricht und, falls du einen Rückruf wünschst, Telefonnummer und gewünschte Erreichbarkeit) verarbeite ich ausschließlich, um deine Anfrage zu beantworten oder dich zurückzurufen. Rechtsgrundlage ist Art. 6 Abs. 1 lit. b DSGVO bzw. lit. f DSGVO. Die Daten werden gelöscht, sobald die Anfrage erledigt ist und keine gesetzlichen Aufbewahrungspflichten bestehen. Für den Versand gelten die Datenschutzbestimmungen deines E-Mail-Anbieters.</p>
<h2>6. Externe Links</h2>
<p>FindeDeineLeute.de verlinkt auf externe Seiten der aufgeführten Communities und Quellen. Sobald du einen solchen Link anklickst, verlässt du diese Website. Für die Datenverarbeitung auf den Zielseiten gelten deren eigene Datenschutzbestimmungen.</p>
<h2>7. Cookies, Tracking, Analyse</h2>
<p>Diese Website setzt keine Cookies, verwendet keine Analyse-, Tracking- oder Werbe-Tools und bindet keine Social-Media-Plugins ein.</p>
<h2>8. Übermittlung in Drittländer</h2>
<p>GitHub hat seinen Sitz in den USA. Eine Datenübermittlung dorthin erfolgt nur, soweit sie für die Auslieferung der Seiteninhalte erforderlich ist. Der Anbieter stützt sich dabei in der Regel auf geeignete Garantien, zum Beispiel EU-Standardvertragsklauseln oder das EU-US Data Privacy Framework.</p>
<h2>9. Deine Rechte</h2>
<p>Dir stehen nach der DSGVO folgende Rechte zu: Auskunft (Art. 15), Berichtigung (Art. 16), Löschung (Art. 17), Einschränkung der Verarbeitung (Art. 18), Datenübertragbarkeit (Art. 20) sowie Widerspruch gegen die Verarbeitung (Art. 21). Wende dich dazu an die oben genannte verantwortliche Stelle. Außerdem hast du das Recht, dich bei einer Datenschutz-Aufsichtsbehörde zu beschweren, zum Beispiel beim Bayerischen Landesamt für Datenschutzaufsicht (BayLDA).</p>
<h2>10. Aktualität</h2>
<p>Diese Datenschutzerklärung wird angepasst, sobald sich an der Datenverarbeitung etwas ändert, zum Beispiel durch neue Funktionen oder Dienste.</p></div>'''
w('datenschutz/index.html',layout('','/datenschutz/','Datenschutz | FindeDeineLeute.de','Datenschutzerklärung von FindeDeineLeute.de',ds,noindex=True))

# ---------- 404 ----------
w('404.html',layout('','/404.html','Seite nicht gefunden | FindeDeineLeute.de','Diese Seite gibt es nicht.','<div class="pagehead"><h1 class="page-title">Seite nicht gefunden</h1><p class="page-sub">Diese Adresse gibt es nicht. Vielleicht hilft dir die Suche weiter.</p><div style="display:flex;gap:10px;margin-top:28px;flex-wrap:wrap"><a class="btn primary" href="/entdecken/">Communities entdecken</a><a class="btn ghost" href="/staedte/">Alle Städte</a></div></div>',noindex=True))

# ---------- Daten, Sitemap, robots, CNAME ----------
w('communities.json',json.dumps({"updated":LASTRUN or TODAY,"cities":cities,"items":data},ensure_ascii=False,separators=(',',':')))
urls=['/','/entdecken/','/staedte/','/online/']+['/%s/'%s for _,s in cities]+['/ueber-uns/','/kontakt/']
sm='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join('<url><loc>%s%s</loc><lastmod>%s</lastmod></url>\n'%(DOMAIN,u,TODAY) for u in urls)+'</urlset>\n'
w('sitemap.xml',sm)
w('robots.txt','User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n'%DOMAIN)
w('CNAME','findedeineleute.de\n')
w('.nojekyll','')
print('pages',len(urls)+3,'items',N)
