# Erzeugt Social-Media-Karussells (1080x1350) aus HTML via Playwright.
import os, base64, sys
from playwright.sync_api import sync_playwright
HERE=os.path.dirname(os.path.abspath(__file__))
FONT=os.path.join(HERE,'..','assets','fonts','inter-latin-wght-normal.woff2')
SYM=open(os.path.join(HERE,'..','assets','logo-symbol.svg')).read()
OUT=sys.argv[1] if len(sys.argv)>1 else os.path.join(HERE,'out')
os.makedirs(OUT,exist_ok=True)
BG=["radial-gradient(70% 50% at 0% 100%,rgba(214,51,108,.35),transparent 70%),radial-gradient(60% 50% at 100% 0%,rgba(143,211,244,.8),transparent 70%),radial-gradient(50% 40% at 80% 100%,rgba(167,124,240,.4),transparent 70%),#fcfbf8",
"radial-gradient(70% 50% at 100% 100%,rgba(143,211,244,.8),transparent 70%),radial-gradient(60% 50% at 0% 0%,rgba(246,165,200,.7),transparent 70%),#fcfbf8"]
CSS=f"""@font-face{{font-family:Inter;src:url(file://{os.path.abspath(FONT)});font-weight:100 900}}
*{{box-sizing:border-box}}body{{margin:0;width:1080px;height:1350px;font-family:Inter;color:#1c1b1a;padding:90px;display:flex;flex-direction:column;position:relative;overflow:hidden}}
.top{{display:flex;align-items:center;gap:14px;font:650 30px Inter;letter-spacing:-.02em}}.top svg{{width:52px;height:52px}}.top i{{font-style:normal;color:#d6336c}}
.main{{flex:1;display:flex;flex-direction:column;justify-content:center}}
h1{{font:750 104px/1.02 Inter;letter-spacing:-.04em;margin:0 0 36px}}h1 em{{font-style:normal;background:linear-gradient(90deg,#d6336c,#a77cf0);-webkit-background-clip:text;color:transparent}}
h2{{font:700 70px/1.08 Inter;letter-spacing:-.03em;margin:0 0 28px}}
p{{font:450 44px/1.4 Inter;color:#4a4642;margin:0}}.tag{{display:inline-block;align-self:flex-start;background:#fff;border:2px solid #e9e6df;border-radius:99px;padding:12px 28px;font:600 30px Inter;color:#d6336c;margin-bottom:34px}}
.num{{font:800 220px/1 Inter;letter-spacing:-.05em;background:linear-gradient(90deg,#d6336c,#8fd3f4);-webkit-background-clip:text;color:transparent;margin-bottom:10px}}
.foot{{display:flex;justify-content:space-between;font:600 28px Inter;color:#66625d}}.card{{background:#fff;border:2px solid #e9e6df;border-radius:36px;padding:44px;margin-top:20px}}.card b{{font:700 46px Inter;display:block;margin-bottom:10px}}.card span{{font:450 36px/1.35 Inter;color:#66625d}}
.cta{{font:700 64px Inter;background:#1c1b1a;color:#fff;border-radius:99px;padding:30px 60px;align-self:flex-start;margin-top:40px}}"""
def page(i,n,body):
    return f"<html><head><style>{CSS}</style></head><body style='background:{BG[i%2]}'><div class=top>{SYM}<span>FindeDeineLeute<i>.de</i></span></div><div class=main>{body}</div><div class=foot><span>findedeineleute.de</span><span>{i+1}/{n}</span></div></body></html>"
def cta(l1,l2): return f"<h1>{l1}</h1><p>{l2}</p><div class=cta>findedeineleute.de</div>"
SETS={
"A_berlin_anfaenger":[
 "<span class=tag>Berlin</span><h1>Sport in Berlin, <em>ohne Vorkenntnisse</em></h1><p>4 Gruppen, die Anfänger wirklich willkommen heißen.</p>",
 "<span class=tag>1</span><h2>Bear City Roller Derby</h2><p>Anfängerkurse und offene Schnuppertage. Schutzausrüstung kannst du dir leihen.</p>",
 "<span class=tag>2</span><h2>Touch Rugby, Berlin Irish RFC</h2><p>Gemischt, ohne Kontakt, alle willkommen. Mittwochs im Jahn-Sportpark, sonntags auf dem Tempelhofer Feld.</p>",
 "<span class=tag>3</span><h2>Park Frisbee</h2><p>Offene Ultimate-Runden für alle Spielstärken im Treptower Park und Mauerpark. Danach oft ein gemeinsames Getränk.</p>",
 "<span class=tag>4</span><h2>Beachvolleyball Beginners</h2><p>Lockere Runden speziell für Einsteiger und Wiedereinsteiger.</p>",
 cta("Mehr Gruppen in <em>deiner Stadt</em>","Über 1.800 Communities, kostenlos und ohne Anmeldung.")],
"B_parkrun":[
 "<span class=tag>Jeden Samstag</span><h1>Ein Treffen, das <em>nichts kostet</em></h1><p>parkrun: 5 Kilometer, gemeinsam, in über 40 deutschen Städten.</p>",
 "<div class=num>0 €</div><h2>Kostenlos, immer</h2><p>Einmal registrieren, dann einfach hinkommen. Laufen, joggen oder gehen ist alles okay.</p>",
 "<h2>Kein Tempo nötig</h2><p>Am Ende laufen die Letzten ins Ziel und werden genauso gefeiert wie die Ersten.</p>",
 "<h2>Zum Beispiel</h2><div class=card><b>Berlin</b><span>Hasenheide, Mauerweg, Tempelhofer Feld</span></div><div class=card><b>Bonn</b><span>Rheinaue</span></div><div class=card><b>Aachen</b><span>Lousberg</span></div>",
 cta("Finde deinen <em>parkrun</em>","Alle Standorte im Verzeichnis.")],
"C_erstes_treffen":[
 "<span class=tag>Ratgeber</span><h1>Allein zum ersten Treffen: <em>6 Tipps</em></h1><p>Aufregung ist normal. So wird der erste Besuch leichter.</p>",
 "<span class=tag>1</span><h2>Wähle ein Format mit Struktur</h2><p>Lauftreff, Spieleabend oder Workshop geben dir eine Aufgabe und ein Gesprächsthema.</p>",
 "<span class=tag>2</span><h2>Schreib vorab eine kurze Nachricht</h2><p>Zwei Sätze genügen. Dann wartet beim Treffen schon jemand auf dich.</p>",
 "<span class=tag>3</span><h2>Komm etwas früher</h2><p>Zu Beginn sind weniger Leute da, und du kannst dich langsam einfinden.</p>",
 "<span class=tag>4</span><h2>Sag, dass du neu bist</h2><p>Der einfachste Satz überhaupt. Die meisten helfen dir gern.</p>",
 "<span class=tag>5</span><h2>Setz dir ein kleines Ziel</h2><p>Mit zwei Personen sprechen oder eine Stunde bleiben. Hinzugehen war schon der schwerste Teil.</p>",
 "<span class=tag>6</span><h2>Geh ein zweites Mal hin</h2><p>Beim zweiten Mal kennst du Gesichter, und es wird merklich leichter.</p>",
 cta("Mehr im <em>Ratgeber</em>","findedeineleute.de/ratgeber/")]}
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':1080,'height':1350})
    for name,sl in SETS.items():
        for i,s in enumerate(sl):
            f=os.path.join(OUT,'_t.html');open(f,'w').write(page(i,len(sl),s))
            pg.goto('file://'+f);pg.wait_for_timeout(150)
            pg.screenshot(path=os.path.join(OUT,f'{name}_{i+1}.png'))
    b.close()
os.remove(os.path.join(OUT,'_t.html'))
