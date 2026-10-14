# -*- coding: utf-8 -*-
import json,re,glob,collections,os,datetime
ROOT=os.path.dirname(os.path.abspath(__file__))
from static_data import *
cities=[l.split('|') for l in CITIES.splitlines()]
CITY_SLUG={c:s for c,s in cities}
out=[]
def add(n,c,t,f='ort',w='',x='',l='',s='',a='',q=1,tags=''):
    out.append(dict(n=n,c=c,t=t,a=a,f=f,w=w,x=x,l=l,s=s,q=q,g=tags))

# ---- München (Basisdatensatz) ----
d=json.load(open(ROOT+'/data/munich_base.json'))
CAT_BY_INT={}
for k in 'running fitness padel golf sport crossfit cycling basketball tennis martial-arts'.split(): CAT_BY_INT[k]='sport'
for k in 'yoga pilates wellness'.split(): CAT_BY_INT[k]='wellbeing'
CAT_BY_INT['newintown']='leute'
for k in 'networking finance'.split(): CAT_BY_INT[k]='business'
CAT_BY_INT['queer']='queer'; CAT_BY_INT['games']='spiele'; CAT_BY_INT['bookclub']='lernen'
for k in 'hiking climbing wintersport surfing horseriding'.split(): CAT_BY_INT[k]='outdoor'
CAT_BY_INT['art']='kunst'; CAT_BY_INT['diy']='kunst'; CAT_BY_INT['creator']='kunst'; CAT_BY_INT['photo']='foto'; CAT_BY_INT['music']='musik'; CAT_BY_INT['dance']='tanz'
CAT_BY_INT['lifestyle']='leute'; CAT_BY_INT['nightlife']='leute'; CAT_BY_INT['female']='frauen'
for k in 'food cooking coffee drinks'.split(): CAT_BY_INT[k]='essen'
LABEL={'running':'Laufgruppe','hiking':'Wandergruppe','fitness':'Fitness-Community','padel':'Padel-Community','golf':'Golf-Community','sport':'Sport-Community','crossfit':'CrossFit-Community','cycling':'Rad-Community','climbing':'Kletter-Community','basketball':'Basketball-Community','tennis':'Tennis-Community','martial-arts':'Kampfsport-Community','horseriding':'Reit-Community','wintersport':'Wintersport-Community','surfing':'Surf-Community','yoga':'Yoga-Community','pilates':'Pilates-Community','wellness':'Wellness-Community','newintown':'Community für Neue in der Stadt','networking':'Netzwerk','female':'Netzwerk für Gründerinnen','finance':'Finanz-Community','queer':'Queere Community','games':'Spielgruppe','bookclub':'Buchclub','art':'Kunst-Community','photo':'Foto-Community','diy':'DIY-Community','music':'Musik-Community','dance':'Tanz-Community','creator':'Creator-Community','lifestyle':'Lifestyle-Community','nightlife':'Community für Nightlife','food':'Food-Community','cooking':'Koch-Community','coffee':'Kaffee-Community','drinks':'Drinks-Community'}
generic=re.compile(r'^(Münchner Community\.?|siehe Links|Wandern|Running|Yoga|Pilates|Creator|New in Town|Kunst & Malen|Brettspiele)$',re.I)
dropped=0
for x in d:
    name=re.sub(r'\s*\n\s*',' – '.replace('–','|'),x['name']).replace('|',' ').strip() if False else re.sub(r'\s*\n\s*',': ',x['name']).strip()
    if 'viele Links' in name: dropped+=1; continue
    ig=x.get('instagram'); web=x.get('website')
    link=web or (('https://www.instagram.com/'+ig.strip('@/')+'/') if ig else '')
    if not link and x.get('email'): link=''
    interest=x.get('interest')
    cat=CAT_BY_INT.get(interest)
    if not cat:
        cat={'sport':'sport','wellness':'wellbeing','expat':'leute','founders':'business','queer':'queer'}.get(x['category'],'kunst')
    pitch=(x.get('pitch') or '').strip()
    pitch=re.sub(r'\s*·\s*(Monetarisiert die Touren|haben einen Newsletter)','',pitch)
    lab=LABEL.get(interest)
    if (generic.match(pitch) or len(pitch)<22):
        desc=(lab+' in München.') if lab else 'Community in München.'
        if pitch and not generic.match(pitch): desc=pitch+'. '+desc
        rich=0
    else: desc=pitch; rich=1
    when=x.get('meetup','')
    if when in ('siehe Links','wechselnd','—'): when=''
    nb=x.get('neighborhood','')
    area='' if nb in ('München','wechselnd','München-weit','1300+ Partner-Studios','') else nb
    f='online' if 'Online' in nb else 'ort'
    if not link and not x.get('email') and not x.get('phone') and rich==0: dropped+=1; continue
    q=1+rich+(1 if when else 0)+(1 if link else 0)+(1 if x.get('size','—') not in ('—','') else 0)
    e=dict(n=name,c=cat,t='München',a=area,f=f,w=when,x=desc,l=link,s='',q=q,g=' '.join(x.get('tags',[])))
    if x.get('size') and x['size']!='—': e['m']=x['size']
    out.append(e)
mun=len(out)

# ---- Run clubs ----
QUEER=re.compile(r'queer|lesbian|frontrunners|rainbow|lavender|pride',re.I)
for fn in sorted(glob.glob(ROOT+'/data/runclubs_*.txt')):
    for line in open(fn,encoding='utf8'):
        line=line.strip()
        if not line: continue
        city,names=line.split('|',1)
        assert city in CITY_SLUG,city
        for n in names.split(';'):
            n=n.strip()
            if not n: continue
            url='https://socialrunclubs.de/'+CITY_SLUG[city]+'/'
            if n.lower().endswith(' parkrun'):
                add(n,'sport',city,w='Samstags',x='Kostenloser, zeitgemessener 5-Kilometer-Lauf im Park, offen für Läufer, Walker und Zuschauer. Registrierung vorab über parkrun.',l='https://www.parkrun.com.de/',s='socialrunclubs.de, parkrun Deutschland',q=3,tags='parkrun laufen 5k')
            else:
                c='queer' if QUEER.search(n) else 'sport'
                add(n,c,city,x='Run Club in '+city+'. Treffzeiten und Kontakt stehen im Verzeichnis von socialrunclubs.de.',l=url,s='socialrunclubs.de',q=1,tags='run club laufen')

# ---- CCC ----
for l in CCC.splitlines():
    city,n,u=l.split('|')
    add(n,'tech',city,x='Lokaler Treffpunkt im Netzwerk des Chaos Computer Club für Technik, Netzpolitik und Selbermachen. Termine stehen auf der Website.',l=u,s='ccc.de',q=3,tags='hackerspace tech chaos computer club netzpolitik')
# ---- Critical Mass ----
for l in CM.splitlines():
    city,w,ort=l.split('|')
    add('Critical Mass '+city,'mobil',city,w=w,x='Gemeinsame Fahrradtour für mehr Platz und Sicherheit im Stadtverkehr. Treffpunkt: '+ort+'.',l='https://criticalmass.de/',s='criticalmass.de',a=ort,q=4,tags='fahrrad radfahren critical mass verkehr')
# ---- Urban Sketchers ----
for city in USK:
    add('Urban Sketchers '+city,'kunst',city,x='Regionalgruppe der Urban Sketchers: gemeinsames Zeichnen vor Ort an wechselnden Plätzen der Stadt. Kontakt und Termine über die Gruppen-Übersicht.',l='https://urbansketchers.de/',s='urbansketchers.de',q=3,tags='zeichnen skizzieren kunst urban sketchers')
# ---- Gardens ----
for l in GARDEN.splitlines():
    city,n,u=l.split('|')
    add(n,'engagement',city,x='Netzwerk für Gemeinschaftsgärten und urbanes Gärtnern in der Stadt. Hier findest du Gärten zum Mitmachen.',l=u,s='urbane-gaerten.de',q=3,tags='garten urban gardening gemeinschaftsgarten')
# ---- DAV ----
for l in DAV.splitlines():
    city,n,u=l.split('|')
    add(n,'outdoor',city,x='Sektion des Deutschen Alpenvereins mit Touren, Kursen und Gruppen für Wandern, Klettern und Bergsport.',l=u,s='alpenverein.de',q=3,tags='wandern klettern berge alpenverein')
# ---- Repair Cafés ----
for l in REPAIR.splitlines():
    city,n,u=l.split('|')
    add(n,'engagement',city,x='Gemeinsam reparieren statt wegwerfen: Hier helfen Ehrenamtliche beim Reparieren von Geräten, Textilien und mehr. Termine stehen auf der verlinkten Seite.',l=u,s='Websuche, reparatur-initiativen.de',q=3,tags='repair café reparieren nachhaltigkeit')
# ---- Nerd Nite ----
add('Nerd Nite Hamburg','lernen','Hamburg',x='Wissenschaft mit Spaß: Kurzvorträge über Themen aller Art, in lockerer Atmosphäre mit Getränken.',l='https://hamburg.nerdnite.com/',s='nerdnite.com',q=3,tags='vorträge wissenschaft nerd')
add('Nerd Nite München','lernen','München',x='Wissenschaft mit Spaß: Kurzvorträge über Themen aller Art, in lockerer Atmosphäre mit Getränken.',l='https://muenchen.nerdnite.com/',s='nerdnite.com',q=3,tags='vorträge wissenschaft nerd')
# ---- Online ----
add('Dachmasters','business','Online',f='online',x='Deutschsprachiger Online-Club von Toastmasters zum Üben von Reden und Präsentationen, von überall teilnehmbar.',l='https://dachmasters.org',s='redeclub.de',q=4,tags='rhetorik reden toastmasters präsentieren')
add('Silent Book Club, virtuelle Treffen','lernen','Online',f='online',x='Gemeinsam lesen, jeder sein eigenes Buch. Die virtuellen Treffen des weltweiten Silent Book Club stehen allen offen.',l='https://silentbook.club/pages/sbc-virtual-meetups',s='silentbook.club',q=4,tags='lesen bücher buchclub')


# ---- Recherche-Dateien (data/ext) ----
import os
from urllib.parse import urlparse
VALID=set('sport outdoor wellbeing tanz musik kunst foto spiele gaming lernen sprachen essen business tech leute queer frauen familie tiere mobil reisen engagement studium'.split())
FIX=[('fuer','für'),('Fuer','Für'),('ueber','über'),('Ueber','Über'),('Schueler','Schüler'),('Grosse','Große'),('grosse','große'),('Grosser','Großer'),('grosser','großer'),('groesser','größer'),('Gross','Groß'),('Staedt','Städt'),('staedt','städt'),('laengere','längere'),('ausser','außer'),('Muenchen','München'),('Koeln','Köln'),('Duesseldorf','Düsseldorf'),('Nuernberg','Nürnberg'),('Gruppen','Gruppen'),('Taetig','Tätig'),('gemeinsam','gemeinsam'),('regelmaessig','regelmäßig'),('Regelmaessig','Regelmäßig'),('spielerisch','spielerisch'),('Maenner','Männer'),('Maedchen','Mädchen'),('moeglich','möglich'),('Moeglich','Möglich'),('Tuer','Tür'),('Zuhoeren','Zuhören'),('zuhoeren','zuhören'),('Kanaele','Kanäle'),('Kanaelen','Kanälen'),('Lebensfuehrung','Lebensführung'),('Eltern- und','Eltern- und'),('Klimaschutz','Klimaschutz'),('hoeren','hören'),('Hoeren','Hören'),('Veranstaltungen','Veranstaltungen'),('Spielemaessig','Spielemäßig'),('aeltere','ältere'),('Aeltere','Ältere'),('Gaeste','Gäste'),('gaeste','gäste'),('Freundschaft','Freundschaft'),('Begegnung','Begegnung'),('verknuepf','verknüpf'),('Stueck','Stück'),('stueck','stück'),('Fruehstueck','Frühstück'),('fruehstueck','frühstück'),('Treffpunkte','Treffpunkte'),('natuerlich','natürlich'),('Natuerlich','Natürlich'),('koennen','können'),('Koennen','Können'),('moechte','möchte'),('waehrend','während'),('Waehrend','Während'),('Beitraege','Beiträge'),('Zusammenhalt','Zusammenhalt'),('praesent','präsent'),('Prasent','Präsent'),('Musiker','Musiker'),('Faelle','Fälle'),('Angebote','Angebote'),('Aktivitaet','Aktivität'),('Aktivitaeten','Aktivitäten'),('Qualitaet','Qualität'),('Universitaet','Universität'),('Gemeinschaftsgaerten','Gemeinschaftsgärten'),('Gaerten','Gärten'),('Garten','Garten'),('Uebung','Übung'),('Ueben','Üben'),('ueben','üben'),('Uebungen','Übungen'),('Oeffentlich','Öffentlich'),('oeffentlich','öffentlich'),('Oeffentlichkeit','Öffentlichkeit'),('Aerzte','Ärzte'),('Aenderung','Änderung'),('Verbaende','Verbände'),('Verband','Verband'),('Anfaenger','Anfänger'),('Anfaengerinnen','Anfängerinnen'),('Faehigkeit','Fähigkeit'),('Faehigkeiten','Fähigkeiten'),('Unterstuetz','Unterstütz'),('unterstuetz','unterstütz'),('Gespraech','Gespräch'),('Gespraeche','Gespräche'),('Spaziergaenge','Spaziergänge'),('Spaziergang','Spaziergang'),('Wanderwege','Wanderwege'),('Naechste','Nächste'),('naechste','nächste'),('Naehe','Nähe'),('naehe','nähe'),('Lernbegeistert','Lernbegeistert'),('Hoehe','Höhe'),('Hoehen','Höhen'),('Gefuehl','Gefühl'),('Gefuehle','Gefühle'),('Erfuell','Erfüll'),('Fuehrung','Führung'),('Fuehr','Führ'),('fuehr','führ'),('Buecher','Bücher'),('buecher','bücher'),('Buechern','Büchern'),('Buch','Buch'),('Stammtische','Stammtische'),('Schuelerinnen','Schülerinnen'),('Kuenstler','Künstler'),('Kuenste','Künste'),('Kunst','Kunst'),('Jugendlich','Jugendlich'),('Tauschen','Tauschen'),('Gemuese','Gemüse'),('Waerme','Wärme'),('Gelaende','Gelände'),('Ausfluege','Ausflüge'),('Ausflug','Ausflug'),('Tuerkisch','Türkisch'),('Uebersetz','Übersetz'),('Verfuegbar','Verfügbar'),('verfuegbar','verfügbar'),('Zusaetzlich','Zusätzlich'),('zusaetzlich','zusätzlich'),('Saetze','Sätze'),('Sprachkenntnisse','Sprachkenntnisse'),('Maerz','März'),('Foerder','Förder'),('foerder','förder'),('Woerter','Wörter'),('Voegel','Vögel'),('Hunde','Hunde'),('Rueck','Rück'),('rueck','rück'),('Kaempf','Kämpf'),('kaempf','kämpf'),('Konzerte','Konzerte'),('Tanzabend','Tanzabend'),('Taenze','Tänze'),('Taenzer','Tänzer'),('Abende','Abende'),('Bruecke','Brücke'),('Entwicklerinnen','Entwicklerinnen'),('Austausch','Austausch'),('Beratung','Beratung'),('Wuensch','Wünsch'),('wuensch','wünsch'),('Aeusser','Äußer'),('sechs','sechs')]
WORDFIX={'Muenchner': 'Münchner', 'Spielstaerken': 'Spielstärken', 'woechentlichen': 'wöchentlichen', 'woechentliche': 'wöchentliche', 'Woechentliche': 'Wöchentliche', 'Ratschlaege': 'Ratschläge', 'Thueringen': 'Thüringen', 'Ernaehrung': 'Ernährung', 'Ernaehrungsfragen': 'Ernährungsfragen', 'Kueche': 'Küche', 'Boerse': 'Börse', 'Schutzausruestung': 'Schutzausrüstung', 'Getraenk': 'Getränk', 'fuenf': 'fünf', 'Taeglich': 'Täglich', 'noetig': 'nötig', 'ergaenzt': 'ergänzt', 'Radausfluege': 'Radausflüge', 'Sehenswuerdigkeiten': 'Sehenswürdigkeiten', 'zuegiges': 'zügiges', 'duesseldorf': 'düsseldorf', 'thueringische': 'thüringische', 'Pfaelzerwald': 'Pfälzerwald', 'Gemuetliches': 'Gemütliches', 'Gemeinnuetziger': 'Gemeinnütziger', 'Luebecker': 'Lübecker', 'Moenchengladbach': 'Mönchengladbach', 'Muelheim': 'Mülheim', 'Neuankoemmlingen': 'Neuankömmlingen', 'Muensteraner': 'Münsteraner', 'Muenster': 'Münster', 'Gegenstaenden': 'Gegenständen', 'Raeume': 'Räume', 'Leseuebungen': 'Leseübungen', 'Gruenderinnen': 'Gründerinnen', 'Selbststaendigen': 'Selbstständigen', 'Berufstaetigen': 'Berufstätigen', 'Schulfaecher': 'Schulfächer', 'Verlagsunabhaengiger': 'Verlagsunabhängiger', 'Nachbarlaendern': 'Nachbarländern', 'verstaendlichen': 'verständlichen', 'Fahrraedern': 'Fahrrädern', 'persoenlichen': 'persönlichen', 'Trainingsplaenen': 'Trainingsplänen', 'Lehrkraefte': 'Lehrkräfte', 'Wuerttemberg': 'Württemberg', 'erklaeren': 'erklären', 'Saarlaendische': 'Saarländische', 'Wuerzburger': 'Würzburger', 'Wuerzburg': 'Würzburg', 'Hoerbüchern': 'Hörbüchern', 'hoerbücher': 'hörbücher', 'Kampfkuenste': 'Kampfkünste', 'Ausruestung': 'Ausrüstung', 'Buerunners': 'Büroläufer'}
def fixde(t):
    for a,b in FIX:
        if a!=b: t=t.replace(a,b)
    for a,b in WORDFIX.items(): t=re.sub(r'\b'+a+r'\b',b,t)
    return t
EXTSRC={'meetup':'meetup.com','reddit':'reddit.com','discord':'discord.com','telegram':'t.me','facebook':'facebook.com'}
for fn in sorted(glob.glob(ROOT+'/data/ext/*.txt')):
    for line in open(fn,encoding='utf8'):
        line=line.strip()
        if not line or line.startswith('#'): continue
        p=[x.strip() for x in line.split('|')]
        if len(p)!=7: continue
        city,n,c,u,x,wn,pf=p
        if c not in VALID or not u.startswith('http') or not n: continue
        if city!='Online' and city not in CITY_SLUG: continue
        host=urlparse(u).hostname or ''
        host=re.sub(r'^www\.','',host)
        pf=pf.lower() if pf.lower() in 'website instagram facebook discord telegram whatsapp reddit slack signal meetup forum sonstige'.split() else ''
        if not pf:
            pf={'reddit.com':'reddit','discord.com':'discord','discord.gg':'discord','t.me':'telegram','meetup.com':'meetup','facebook.com':'facebook','instagram.com':'instagram','chat.whatsapp.com':'whatsapp'}.get(host,'website')
        if city=='Online' or pf in ('discord','telegram','reddit','slack','whatsapp','forum') and city=='Online': f='online'
        else: f='ort'
        if city=='Online': f='online'
        wn='' if wn.lower() in ('laufend','') else fixde(wn)
        e=dict(n=fixde(n),c=c,t=city,a='',f=f,w=wn,x=fixde(x),l=u,s=host,q=2+(1 if wn else 0)+(1 if len(x)>60 else 0),g=c+' '+pf)
        e['p']=pf
        e['_ext']=1
        out.append(e)

# dedupe identical (name, city)
seen=set();seenu=set();res=[]
for e in out:
    k=(e['n'].lower(),e['t'])
    uk=e['l'].rstrip('/').lower() if e['l'] and e['s']=='' else None
    if k in seen: continue
    if e.get('p') and e['l'].rstrip('/').lower() in seenu: continue
    if e.get('p'): seenu.add(e['l'].rstrip('/').lower())
    seen.add(k);res.append(e)
def clean(t):
    t=re.sub(r'(\d)\s*[–—]\s*(\d)',r'\1 bis \2',t)
    return re.sub(r'\s[—–]\s',', ',t)
PH={'reddit.com':'reddit','discord.com':'discord','discord.gg':'discord','t.me':'telegram','meetup.com':'meetup','facebook.com':'facebook','instagram.com':'instagram','chat.whatsapp.com':'whatsapp'}
for e in res:
    for k in ('n','x','w','a'): e[k]=clean(e[k])
    if not e.get('p'):
        h=re.sub(r'^www\.','',urlparse(e['l']).hostname or '') if e['l'] else ''
        e['p']=PH.get(h,'website') if e['l'] else ''
# Prüfstand aus refresh.py einarbeiten
ST={}
try: ST=json.load(open(ROOT+'/data/state.json',encoding='utf8'))
except Exception: pass
def compact(n):
    return ('%.1fk'%(n/1000)).replace('.',',').replace(',0k','k') if n>=1000 else str(n)
hidden=0;keep=[]
for e in res:
    s_=ST.get('links',{}).get(e['l'])
    if s_:
        if s_.get('fails',0)>=3: hidden+=1; continue
        if s_.get('ok'): e['v']=s_['ok']
        if s_.get('members') and e.get('p') in ('discord','telegram','reddit'):
            e['m']=compact(s_['members'])+(' Mitglieder' if e['p']!='reddit' else ' Abonnenten')
    keep.append(e)
res=keep
# Erstes Auftreten je Eintrag (für automatische Neuigkeiten)
FSF=ROOT+'/data/firstseen.json'
try: FS=json.load(open(FSF,encoding='utf8'))
except Exception: FS=None
first_run=FS is None
if first_run: FS={}
TODAY_=datetime.date.today().isoformat()
for e in res:
    k=e['t']+'|'+e['n']
    if k not in FS:
        # Erstbefüllung: Bestand gilt als alt, Einträge aus data/ext als heute neu
        FS[k]=TODAY_ if (not first_run or e.get('_ext')) else '2026-09-01'
    e['fs']=FS[k]
    e.pop('_ext',None)
json.dump(FS,open(FSF,'w',encoding='utf8'),ensure_ascii=False,sort_keys=True,indent=0)
print('wegen toter Links ausgeblendet',hidden)
res.sort(key=lambda e:(-e['q'],e['t'],e['n'].lower()))
for i,e in enumerate(res): e['i']=i+1
json.dump(res,open(ROOT+'/data/data.json','w',encoding='utf8'),ensure_ascii=False,separators=(',',':'))
cnt=collections.Counter(e['t'] for e in res)
print('total',len(res),'munich',mun,'dropped',dropped)
print('cities with entries',len([c for c,_ in cities if cnt[c]]),'of',len(cities))
print([ (c,cnt[c]) for c,_ in cities if cnt[c]<3])
print(collections.Counter(e['c'] for e in res))
import os;print(os.path.getsize(ROOT+'/data/data.json'))
