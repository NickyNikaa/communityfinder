# -*- coding: utf-8 -*-
# Redaktionelle Inhalte: Themenbeschreibungen und Ratgeber-Beiträge.
# Keine Gedankenstriche verwenden.

# id: (Überschriftsbegriff, was man dort erlebt, Tipp für den Einstieg, Frage, Antwort)
CATINFO = {
 'sport': ('Sport und Fitness',
  'Hier finden sich Laufgruppen, Freizeitteams und offene Trainingstreffs, bei denen es um gemeinsame Bewegung geht und nicht um Leistung. Viele Gruppen sind ausdrücklich für Anfänger gedacht und treffen sich zu festen Zeiten im Park oder an einem Treffpunkt.',
  'Schau dir zuerst Treffzeit und Treffpunkt an und komm einfach beim nächsten Termin vorbei. Meist reicht normale Sportkleidung, angemeldet wird oft erst später oder gar nicht.',
  'Muss ich fit sein, um mitzumachen?',
  'Nein. Die meisten offenen Gruppen sind auf unterschiedliche Level eingestellt, oft gibt es mehrere Tempogruppen. Frag im Zweifel kurz vorab, welches Tempo üblich ist.'),
 'outdoor': ('Outdoor und Natur',
  'Dazu zählen Wandergruppen, Klettertreffs, Kanu- und Radtouren, Wintersport und Naturgruppen. Die Touren sind meist gemeinschaftlich organisiert, und viele Gruppen bieten Einsteigerrunden an.',
  'Prüfe bei der Gruppe, ob eine Tour für Anfänger gekennzeichnet ist, und frag nach Ausrüstung. Bei Bergtouren und Klettern solltest du dich über Erfahrung und Sicherheit vorab informieren.',
  'Brauche ich eine eigene Ausrüstung?',
  'Für Wanderungen reichen feste Schuhe und Wetterkleidung. Bei Klettern, Kanu oder Wintersport kann Ausrüstung oft geliehen werden. Die Gruppe sagt dir in der Regel vorab, was du brauchst.'),
 'wellbeing': ('Wellbeing',
  'Hier geht es um Entspannung, Achtsamkeit, Yoga, Atemtreffs oder gemeinsames Eisbaden, also darum, sich in Gesellschaft Zeit für sich zu nehmen. Die Gruppen sind meist klein und wenig leistungsorientiert.',
  'Probiere zuerst ein offenes oder kostenloses Treffen aus, bevor du dich bindest. Ein Schnuppertermin zeigt schnell, ob die Stimmung zu dir passt.',
  'Sind solche Gruppen etwas für Anfänger?',
  'Ja, die meisten Treffen setzen keine Vorkenntnisse voraus. Sag vorab Bescheid, wenn du Einschränkungen hast, dann kann die Gruppe darauf eingehen.'),
 'tanz': ('Tanz',
  'Von Swing und Lindy Hop über Salsa bis zu Contact Improvisation: Tanzgruppen und Vereine laden oft zu offenen Abenden ein, bei denen man ohne feste Partnerin oder festen Partner mittanzen kann.',
  'Frag, ob es einen Einsteigerteil oder einen Workshop vor der Tanzfläche gibt. Viele Abende beginnen mit einer kurzen Einführung für Neue.',
  'Brauche ich einen Tanzpartner?',
  'Meistens nicht. Bei offenen Tanzabenden wird häufig gewechselt, und neue Gesichter sind ausdrücklich willkommen.'),
 'musik': ('Musik und Chor',
  'Offene Chöre, Bandbörsen, Orchester und Jam-Treffs: Hier machst du Musik gemeinsam, vom lockeren Mitsingen bis zum regelmäßigen Proben für Auftritte.',
  'Frag nach einer Schnupperprobe. Viele Chöre und Gruppen lassen dich zwei bis drei Termine unverbindlich mitmachen, bevor du dich entscheidest.',
  'Muss ich ein Instrument spielen oder Noten lesen können?',
  'Bei vielen Chören und Mitmachformaten nicht. Bei Orchestern und Bands hilft Spielerfahrung, aber auch dort gibt es Gruppen für Wiedereinsteiger.'),
 'kunst': ('Kunst und Handwerk',
  'Zeichentreffs, Malgruppen, Strick- und Handarbeitsrunden, Schreibwerkstätten und Maker-Gruppen. Hier entsteht etwas gemeinsam, und der Austausch über das Machen steht im Vordergrund.',
  'Bring zum ersten Mal einfach ein Skizzenbuch oder dein aktuelles Projekt mit. Material wird oft geteilt, und niemand erwartet Können.',
  'Muss ich schon gut zeichnen oder basteln können?',
  'Nein. Die meisten Gruppen sind für alle Level offen, und es geht um die Freude am Machen und den Austausch.'),
 'foto': ('Foto und Film',
  'Fotowalks, Fotoclubs, Filmstammtische und Kurzfilm-Treffen: Du lernst voneinander, bekommst Feedback und entdeckst neue Ecken der Stadt.',
  'Komm mit der Kamera, die du hast, auch das Smartphone ist bei vielen Walks willkommen. Frag nach, ob es ein Thema oder eine Route gibt.',
  'Brauche ich eine teure Kamera?',
  'Nein. Bei vielen Treffs geht es um den Blick und das Motiv, nicht um die Ausrüstung.'),
 'spiele': ('Brett- und Rollenspiele',
  'Spieleabende, Pen-and-Paper-Runden, Tabletop, Schach und Quizabende: Hier sitzt man zusammen am Tisch. Viele Treffen haben einen offenen Charakter, und Spiele werden gestellt oder erklärt.',
  'Sag beim Ankommen, dass du neu bist. Die meisten Gruppen erklären dir gern ein Spiel oder setzen dich an einen Einsteigertisch.',
  'Muss ich die Regeln schon kennen?',
  'Nein. Gerade offene Spieleabende leben davon, dass Neue mitspielen, und es gibt meistens jemanden, der erklärt.'),
 'gaming': ('Gaming und E-Sport',
  'Hier treffen sich Spielerinnen und Spieler für Videospiele, Turniere und E-Sport, ob im Verein, an der Hochschule oder in Gruppen, die sich vor Ort verabreden.',
  'Schau, welche Spiele und Level gespielt werden, und fang mit einem offenen Treffen oder Einsteigerturnier an.',
  'Gibt es auch Gruppen ohne Wettkampf?',
  'Ja. Neben Turnierteams gibt es lockere Spieltreffs, Retro-Abende und Entwickler-Meetups, bei denen der Spaß im Mittelpunkt steht.'),
 'lernen': ('Bücher und Lernen',
  'Buchclubs, Lesetreffs, Vortragsabende und Lerngruppen: Wer gern liest, diskutiert oder dazulernt, findet hier Gleichgesinnte, mit festen Terminen oder ganz locker.',
  'Viele Buchclubs legen das nächste Buch vorab fest. Schau, ob du ohne Vorbereitung reinschnuppern kannst, bei Silent Book Clubs liest jeder sein eigenes Buch.',
  'Muss ich das Buch vorher gelesen haben?',
  'Bei klassischen Buchclubs ist das üblich, bei Leserunden wie dem Silent Book Club nicht. Die Gruppenbeschreibung nennt meist das Format.'),
 'sprachen': ('Sprachen und Austausch',
  'Sprachcafés, Tandem-Treffs und Stammtische: Hier übst du eine Sprache im Gespräch und lernst Menschen aus aller Welt kennen. Viele Treffen finden in Cafés oder Bars statt.',
  'Wähle einen Abend mit deiner Zielsprache und komm ohne Druck. Es geht ums Sprechen und nicht um Perfektion.',
  'Welches Sprachniveau brauche ich?',
  'Die meisten Sprachtreffs sind für alle Niveaus offen. Einsteiger sind willkommen, oft gibt es Tische für verschiedene Stufen.'),
 'essen': ('Essen und Trinken',
  'Kochclubs, Slow-Food-Gruppen, Supper-Clubs und Genusstreffs: Gemeinsam kochen und essen verbindet, und viele Runden sind offen für Neue.',
  'Frag nach Kostenbeteiligung und Allergien und bring bei gemeinsamen Koch-Abenden Neugier mit. Oft reicht eine kurze Anmeldung.',
  'Was kostet die Teilnahme?',
  'Das ist unterschiedlich. Manche Treffen sind kostenlos, bei anderen teilt man die Zutaten. Die Gruppe nennt das vorab.'),
 'business': ('Business und Karriere',
  'Rhetorikclubs, Gründerstammtische, Service-Clubs und Netzwerke für den Berufsalltag. Hier geht es um Austausch, Feedback und neue Kontakte außerhalb der eigenen Firma.',
  'Besuche zuerst als Gast. Viele Clubs erlauben ein bis zwei Termine zum Kennenlernen, bevor eine Mitgliedschaft Thema wird.',
  'Ist eine Mitgliedschaft nötig?',
  'Gäste sind bei den meisten Treffen willkommen. Eine Mitgliedschaft ist dann eine spätere Entscheidung und oft mit einem Beitrag verbunden.'),
 'tech': ('Tech und Code',
  'Hackerspaces, Programmier-Stammtische, User Groups und Open-Source-Treffs: Hier tauschen sich Menschen über Technik aus, bauen gemeinsam Projekte und teilen Wissen.',
  'Die meisten Treffen haben offene Abende oder Vortragsformate. Komm mit deiner Frage oder deinem Projekt, Vorkenntnisse sind oft nicht nötig.',
  'Muss ich programmieren können?',
  'Nicht immer. Viele Treffs richten sich an Einsteiger, und in Hackerspaces gibt es auch Elektronik, Handwerk und Netzpolitik.'),
 'leute': ('Neue Leute',
  'Stammtische, Neu-in-der-Stadt-Treffs und offene Gruppen, bei denen das Kennenlernen im Mittelpunkt steht. Genau richtig, wenn du neu in der Stadt bist oder dein Umfeld erweitern möchtest.',
  'Such dir ein Format, das zu dir passt, etwa einen Spaziergang, einen Spieleabend oder einen Stammtisch, und geh mehrmals hin. Beim zweiten und dritten Mal wird es deutlich leichter.',
  'Wie lerne ich dort wirklich Leute kennen?',
  'Komm regelmäßig. Wer mehrfach auftaucht, kommt ins Gespräch, und aus Gesichtern werden Bekanntschaften.'),
 'queer': ('Queer',
  'Queere Stammtische, Sportgruppen, Chöre und Vereine: Räume, in denen du dich ohne Erklärungen zugehörig fühlen kannst. Viele Gruppen sind offen für alle, die respektvoll mitmachen.',
  'Lies die Beschreibung der Gruppe, oft steht dort, für wen sie gedacht ist. Bei Unsicherheit hilft eine kurze Nachricht vorab.',
  'Sind die Gruppen für alle offen?',
  'Das hängt von der Gruppe ab. Manche richten sich an bestimmte Gruppen, andere sind für alle offen. Die Beschreibung oder eine kurze Nachfrage klärt das.'),
 'frauen': ('Frauen',
  'Netzwerke, Stammtische und Gruppen, die Frauen in den Mittelpunkt stellen, ob beruflich, sportlich oder zum Austausch. Viele sind ein geschützter Rahmen für offene Gespräche.',
  'Schau nach, ob ein Treffen offen für Gäste ist. Viele Netzwerke laden zum Kennenlernen ein, bevor eine feste Teilnahme Thema wird.',
  'Für wen sind die Gruppen gedacht?',
  'Das steht in der jeweiligen Beschreibung. Manche Gruppen sind ausschließlich für Frauen, andere offen für alle Geschlechter.'),
 'familie': ('Eltern und Familie',
  'Eltern-Kind-Treffs, Familiennetzwerke und Nachbarschaftsgruppen: Hier findest du Austausch, Spielpartner für die Kinder und Menschen in einer ähnlichen Lebensphase.',
  'Viele Treffen haben feste Wochentage. Komm einfach vorbei oder schreib kurz vorab, besonders bei kleinen Gruppen.',
  'Ab welchem Alter der Kinder sind die Treffs geeignet?',
  'Das unterscheidet sich je nach Gruppe, von Krabbelgruppen bis zu Familientreffs mit größeren Kindern. Die Beschreibung nennt meist die Altersspanne.'),
 'tiere': ('Tiere',
  'Hundegruppen, Tierschutz-Ehrenamt, Vogelkunde und Aquaristik: Wer Tiere mag, findet hier Gleichgesinnte zum Austausch, Gassigehen oder Mitanpacken.',
  'Frag bei Ehrenamtsgruppen nach einem Schnuppertermin. Für gemeinsame Hundespaziergänge ist ein sozialverträglicher Hund hilfreich.',
  'Kann ich auch ohne eigenes Tier mitmachen?',
  'Bei Ehrenamtsgruppen und Naturgruppen ja. Bei Hundetreffs sind meist Halter gemeint, die Beschreibung klärt das.'),
 'mobil': ('Mobilität und Rad',
  'Critical Mass, Radgruppen, Initiativen für bessere Radwege und Oldtimer-Clubs: Hier geht es um Bewegung auf zwei und mehr Rädern, oft mit einem Engagement für die Stadt.',
  'Bei Radtouren und der Critical Mass reicht ein verkehrssicheres Rad. Schau nach Treffpunkt und Zeit, die Touren sind meist regelmäßig.',
  'Wie funktioniert die Critical Mass?',
  'Radfahrende treffen sich zu einer gemeinsamen Fahrt durch die Stadt, meist am letzten Freitag im Monat. Du brauchst keine Anmeldung, nur ein Rad und den Treffpunkt.'),
 'reisen': ('Reisen',
  'Reise-Stammtische, Backpacker-Treffs und Gruppen, die Touren und Ausflüge planen. Hier tauscht man Tipps aus und findet Mitreisende.',
  'Starte mit einem Stammtisch, bevor du gemeinsam verreist. So lernst du die Leute kennen und merkst, ob der Reisestil passt.',
  'Reise ich dann in der Gruppe?',
  'Nicht unbedingt. Viele Treffs sind reine Austauschabende, gemeinsame Reisen entstehen daraus auf freiwilliger Basis.'),
 'engagement': ('Umwelt und Engagement',
  'Fridays for Future, Parents for Future, Repair Cafés, Gemeinschaftsgärten und Nachbarschaftsinitiativen: Hier packt man gemeinsam an und verändert etwas in der Stadt.',
  'Die meisten Gruppen freuen sich über Neue und haben Einsteigertermine. Komm zu einem offenen Treffen und frag, wo gerade Hilfe gebraucht wird.',
  'Wie viel Zeit muss ich mitbringen?',
  'So viel, wie du möchtest. Viele Initiativen leben von Menschen, die mal eine Stunde, mal einen Nachmittag helfen.'),
 'studium': ('Studium',
  'Hochschulgruppen, studentische Initiativen und Netzwerke: Hier lernst du Mitstudierende über das Fach hinaus kennen und kannst eigene Projekte anstoßen.',
  'Informiere dich zu Semesterbeginn, dann stellen sich viele Gruppen vor. Frag bei den Treffen, ob du als Gast mitmachen kannst.',
  'Muss ich an der Hochschule eingeschrieben sein?',
  'Bei vielen Hochschulgruppen ja, bei anderen sind Gäste willkommen. Die Beschreibung oder eine kurze Nachfrage klärt das.'),
}

# Ratgeber-Beiträge. Markup: '## ' Zwischenüberschrift, Leerzeile trennt Absätze, [Text](/pfad/) Links.
ARTICLES = [
 dict(slug='neu-in-der-stadt-leute-kennenlernen', date='2026-10-15',
  title='Neu in der Stadt: 9 Wege, Leute kennenzulernen',
  desc='Neu in der Stadt und niemand da? Neun erprobte Wege, wie du Anschluss findest: von Stammtischen über Sportgruppen bis zu Online-Communities.',
  lead='Der Umzug ist geschafft, die Kartons sind ausgepackt, aber niemand kennt dich. Das geht fast allen so. Mit etwas Planung findest du in wenigen Wochen Anschluss, ohne dich zu verstellen.',
  body='''## 1. Such dir ein festes Format statt Einzeltreffen

Menschen lernen sich am besten kennen, wenn sie sich wiedersehen. Ein wöchentlicher Lauftreff oder ein monatlicher Stammtisch schlägt deshalb jedes einmalige Event. Nach dem dritten Besuch kennst du Gesichter und wirst begrüßt.

## 2. Starte mit einem Hobby, das du sowieso machst

Wer ohnehin gern läuft, liest oder zeichnet, hat sofort ein Gesprächsthema. Das nimmt den Druck, etwas Kluges sagen zu müssen. In unserem Verzeichnis findest du Gruppen für fast jedes Interesse, zum Beispiel [Sport und Fitness](/entdecken/?kategorie=sport) oder [Kunst und Handwerk](/entdecken/?kategorie=kunst).

## 3. Nutze Neu-in-der-Stadt-Treffs

Viele Städte haben Stammtische, die sich ausdrücklich an Zugezogene richten. Dort sind alle in einer ähnlichen Lage, und das Ansprechen fällt leichter. Schau in die Kategorie [Neue Leute](/entdecken/?kategorie=leute).

## 4. Probier eine Sportgruppe oder einen Run Club

Bewegung verbindet, und beim Laufen oder Radfahren redet man nebenbei. Viele Gruppen sind für Anfänger gedacht und haben feste Treffpunkte. Gerade Run Clubs bieten oft mehrere Tempogruppen und einen Treffpunkt im Anschluss.

## 5. Engagiere dich ehrenamtlich

Ob Repair Café, Gemeinschaftsgarten oder Tierschutz: Beim gemeinsamen Anpacken kommen Gespräche von allein. Du bist gleichzeitig nützlich, und das macht den Einstieg angenehm.

## 6. Geh zu Sprach- und Spielabenden

Sprachcafés und offene Spieleabende haben eingebaute Gesprächsanlässe. Du musst kein Thema erfinden, die Sprache oder das Spiel liefert es.

## 7. Verabrede dich zuerst online

Wenn dir ein erster Schritt vor Ort schwerfällt, kann ein Chat helfen. Lokale Gruppen auf Discord, Telegram oder Reddit zeigen, wer in der Stadt aktiv ist und wo Treffen geplant werden. Mehr dazu in unserem Ratgeber [Online-Communities richtig nutzen](/ratgeber/online-communities-richtig-nutzen/).

## 8. Sag zu, auch wenn du zögerst

Wenn dich jemand zu einem Treffen einlädt, sag ja. Die zweite Einladung kommt meist nur, wenn du die erste angenommen hast. Du kannst jederzeit früher gehen.

## 9. Gib dir Zeit

Freundschaften brauchen Wochen bis Monate. Rechne nicht damit, nach dem ersten Abend neue beste Freunde zu haben. Wenn du dranbleibst, entstehen Bekanntschaften, aus denen oft mehr wird.

Alle Städte findest du in der [Städteübersicht](/staedte/), dort kannst du direkt in deiner Stadt nach Gruppen suchen.'''),
 dict(slug='run-club-finden-und-einsteigen', date='2026-10-15',
  title='Run Club finden und einsteigen: Das solltest du wissen',
  desc='Wie funktioniert ein Run Club, brauche ich Vorkenntnisse und was kostet das? Antworten auf die häufigsten Einsteigerfragen.',
  lead='Run Clubs sind in vielen Städten ein beliebter Treffpunkt: gemeinsam laufen, danach Kaffee trinken. Die gute Nachricht: Du musst dafür nicht schnell sein.',
  body='''## Was ist ein Run Club?

Ein Run Club ist eine Laufgruppe, die sich regelmäßig zu festen Zeiten trifft. Anders als im klassischen Verein gibt es meist keine Mitgliedschaft, du kommst einfach vorbei. Viele Clubs verbinden den Lauf mit einem gemeinsamen Ausklang im Café.

## Muss ich schnell oder fit sein?

Nein. Viele Run Clubs laufen in mehreren Gruppen mit unterschiedlichem Tempo, und niemand wird zurückgelassen. Schreib vorab kurz, welches Tempo du läufst, dann weißt du, welche Gruppe passt.

## Was kostet ein Run Club?

Viele Clubs sind kostenlos, einige finanzieren sich über Sponsoren oder bitten um freiwillige Beiträge. Auch die parkrun-Läufe am Samstagmorgen sind kostenlos, du registrierst dich einmal vorab.

## Wie finde ich einen Club in meiner Stadt?

Am einfachsten über die Städteseiten: Wähle deine Stadt und schau dir die Kategorie [Sport und Fitness](/entdecken/?kategorie=sport) an. Viele Clubs veröffentlichen ihre Termine auf Instagram oder auf einer eigenen Seite. Dort steht meist auch der Treffpunkt.

## Was ziehe ich an und was nehme ich mit?

Bequeme Sportkleidung und eingelaufene Schuhe reichen. Je nach Jahreszeit brauchst du eine Jacke und im Dunkeln eine Lampe oder reflektierende Kleidung. Wasser nimmst du nur bei längeren Runden mit.

## Wie läuft der erste Besuch ab?

Komm ein paar Minuten früher, sag, dass du neu bist, und frag nach der Strecke. Meist wird dir jemand zugeteilt, der dich begleitet. Nach dem Lauf bleibt Zeit zum Austausch, und genau dort entstehen die Kontakte.

## Was, wenn es mir nicht gefällt?

Dann probierst du den nächsten Club. In größeren Städten gibt es mehrere Gruppen mit unterschiedlicher Stimmung, von sportlich bis gemütlich. Alle Gruppen findest du auf den Seiten der Städte, zum Beispiel in der [Städteübersicht](/staedte/).'''),
 dict(slug='hobby-gruppe-finden', date='2026-10-15',
  title='Die passende Hobby-Gruppe finden: So gehst du vor',
  desc='Wie du aus hunderten Angeboten die Gruppe findest, die zu dir passt, und woran du eine gute Community erkennst.',
  lead='Es gibt Gruppen für fast alles, und genau das macht die Auswahl schwer. Mit diesen Schritten findest du schneller eine Gruppe, in der du dich wohlfühlst.',
  body='''## Starte bei deinem Interesse, nicht beim Format

Überleg zuerst, was du gern tust oder lernen möchtest. Ob Tanzen, Schach oder Fotografieren: In unserer Übersicht findest du alle [Kategorien](/entdecken/) und kannst sie mit deiner Stadt kombinieren.

## Wähle ein Format, das zu deinem Alltag passt

Prüfe, wie oft und wann sich die Gruppe trifft. Eine wöchentliche Verpflichtung am Dienstagabend passt nicht zu jedem Kalender. Ein monatlicher Stammtisch ist leichter einzuplanen und ein guter Einstieg.

## Achte auf Offenheit für Neue

Eine gute Community sagt klar, dass Neue willkommen sind, und nennt Treffpunkt, Zeit und Ansprechperson. Wenn du nirgends einen Hinweis findest, wie du dazustoßen kannst, frag kurz nach.

## Probiere zwei oder drei Gruppen aus

Du erkennst oft schon nach einem Besuch, ob die Stimmung passt. Vergleiche mindestens zwei Gruppen, bevor du dich festlegst. Verein oder lockere Gruppe? Dazu mehr im Beitrag [Verein oder lockere Gruppe](/ratgeber/verein-oder-lockere-gruppe/).

## Prüfe, ob die Gruppe aktiv ist

Schau, ob es aktuelle Termine oder Beiträge gibt. Gruppen ohne Aktivität seit Monaten solltest du vorab anschreiben. Wir prüfen die Links im Verzeichnis alle zwei Wochen, ein Restrisiko bleibt aber.

## Sei geduldig mit dir

Nicht jede Gruppe passt beim ersten Mal. Wenn du dich unwohl fühlst, heißt das nicht, dass du das Problem bist. Probier die nächste, die Auswahl ist groß.'''),
 dict(slug='online-communities-richtig-nutzen', date='2026-10-15',
  title='Online-Communities richtig nutzen: Discord, Telegram und Reddit',
  desc='Wie funktionieren Discord-Server, Telegram-Gruppen und Subreddits, wie findest du sie und wie bleibst du dabei sicher?',
  lead='Nicht jede Community trifft sich im Park. Auf Discord, Telegram und Reddit finden sich Menschen mit gleichen Interessen, egal wo sie wohnen. Hier erfährst du, worin sich die Plattformen unterscheiden.',
  body='''## Discord: Server mit Themenkanälen

Ein Discord-Server ist wie ein Haus mit vielen Räumen: Du findest Textkanäle zu Unterthemen und Sprachkanäle zum Reden. Besonders verbreitet ist Discord bei Gaming, Lernen und Programmieren, es gibt aber auch Server für Kunst, Musik oder Sprachaustausch. Du brauchst einen Account und meist eine Einladung.

## Telegram: Gruppen und Kanäle

Telegram kennt Gruppen, in denen alle schreiben, und Kanäle, in denen nur Administratoren posten. Gruppen sind gut für lokale Absprachen und schnelle Treffen. Prüfe, ob du in der Gruppe sichtbar bist, und teile deine Nummer nur, wenn du das wirklich willst.

## Reddit: Subreddits zum Stöbern

Reddit ist ein Forum mit thematischen Bereichen, den Subreddits. Viele Städte haben ein eigenes, dort gibt es Tipps und Fragen aus dem Alltag. Du liest auch ohne Account mit und kannst später mitdiskutieren.

## So findest du die passende Community

In unserem [Online-Bereich](/online/) kannst du nach Plattform und Thema filtern. Starte mit einer Plattform, die du schon kennst, und tritt ein bis zwei Gruppen bei, statt dich überall anzumelden.

## Sicher bleiben

Gib persönliche Daten wie Adresse oder Telefonnummer nicht in offenen Gruppen preis. Sei vorsichtig bei Direktnachrichten von Unbekannten, besonders wenn es um Geld oder Links geht. Einladungslinks können ablaufen oder ersetzt werden, wir prüfen sie regelmäßig, trotzdem kann ein Link einmal nicht mehr funktionieren.

## Vom Chat zum echten Treffen

Viele lokale Gruppen verabreden Treffen im Chat. Wenn du dich online wohlfühlst, ist das ein sanfter Einstieg. Wie du dann den ersten Schritt vor Ort machst, liest du im Beitrag [Allein zum ersten Treffen](/ratgeber/allein-zum-ersten-treffen/).'''),
 dict(slug='allein-zum-ersten-treffen', date='2026-10-15',
  title='Allein zum ersten Treffen: Tipps gegen die Hemmschwelle',
  desc='Aufgeregt vor dem ersten Gruppentreffen? Mit diesen sechs Tipps wird der erste Besuch leichter.',
  lead='Allein in eine Gruppe zu gehen, kostet Überwindung. Das geht fast jedem so, und es gibt einfache Wege, den ersten Besuch zu erleichtern.',
  body='''## Wähle ein Format mit Struktur

Ein Lauftreff, Spieleabend oder Workshop gibt dir eine Aufgabe und ein Gesprächsthema. Das ist leichter als ein offener Stammtisch ohne Programm.

## Schreib vorab eine kurze Nachricht

Wenn es Kontaktdaten gibt, melde dich mit zwei Sätzen: dass du neu bist und kommen möchtest. Oft bekommst du eine freundliche Antwort, und beim Treffen wartet jemand auf dich.

## Komm etwas früher

Zu Beginn sind weniger Leute da, und du kannst dich langsam einfinden. Später in eine volle Runde zu kommen ist deutlich schwerer.

## Sag, dass du neu bist

Das ist der einfachste Satz überhaupt. Er nimmt Druck raus, und die meisten helfen dir gern.

## Setz dir ein kleines Ziel

Zum Beispiel: mit zwei Personen sprechen oder eine Stunde bleiben. Wenn du danach gehen möchtest, ist das in Ordnung. Du hast es geschafft hinzugehen.

## Geh ein zweites Mal hin

Das erste Treffen fühlt sich fast immer holprig an. Beim zweiten Mal kennst du Gesichter, und es wird merklich leichter. Gib einer Gruppe deshalb mindestens zwei Chancen.

Eine Gruppe in deiner Stadt findest du über die [Städteübersicht](/staedte/) oder die [Suche](/entdecken/).'''),
 dict(slug='verein-oder-lockere-gruppe', date='2026-10-15',
  title='Verein oder lockere Gruppe: Was passt zu dir?',
  desc='Wo liegen die Unterschiede zwischen Verein, Stammtisch und offener Community, und wie entscheidest du dich?',
  lead='Manche Gruppen sind eingetragene Vereine, andere treffen sich einfach so. Beides hat Vorteile. Hier die wichtigsten Unterschiede.',
  body='''## Der Verein

Ein Verein hat Mitglieder, eine Satzung und meist einen Beitrag. Dafür gibt es feste Strukturen, Räume, oft Trainer und Versicherungsschutz. Das passt, wenn du langfristig dabeibleiben und Teil von etwas Festem sein möchtest. Typische Beispiele sind Sportvereine, Chöre oder die Sektionen des Alpenvereins.

## Die lockere Gruppe

Offene Gruppen und Stammtische haben meist keine Mitgliedschaft und keine Beiträge. Du kommst, wenn du Zeit hast. Das passt, wenn du erst ausprobieren möchtest oder unregelmäßig Zeit hast. Der Nachteil: Gruppen können sich auflösen, wenn die Organisatoren aufhören.

## Die Online-Community

Sie ist ortsunabhängig und jederzeit erreichbar. Gut für Nischenthemen und für den Anfang. Mehr dazu im Ratgeber [Online-Communities richtig nutzen](/ratgeber/online-communities-richtig-nutzen/).

## So entscheidest du

Frag dich: Wie oft kann ich verlässlich kommen? Möchte ich mich verpflichten? Brauche ich Trainer oder Ausrüstung? Wenn du unsicher bist, starte locker und wechsle später in einen Verein, wenn dir die Gruppe gefällt. Viele Vereine erlauben ohnehin Probetermine.

Stöbere in unserem [Verzeichnis](/entdecken/), dort findest du beide Arten nebeneinander.'''),
 dict(slug='freunde-finden-als-erwachsener', date='2026-10-15',
  title='Freunde finden als Erwachsener: Warum es schwerer ist und was hilft',
  desc='Warum es im Erwachsenenalter schwerer wird, Freunde zu finden, und welche Gewohnheiten wirklich helfen.',
  lead='In Schule und Studium entstehen Freundschaften fast von allein. Später fehlt der Rahmen. Das ist normal, und du kannst etwas dagegen tun.',
  body='''## Warum es schwerer wird

Im Alltag begegnen wir immer denselben Menschen, Verpflichtungen füllen den Kalender, und der Zufall fällt weg. Freundschaften brauchen Zeit und regelmäßige Begegnungen. Wenn beides fehlt, passiert wenig.

## Schaffe Orte, an denen du Leute wiedersiehst

Der wichtigste Faktor sind regelmäßige Treffen. Eine feste Gruppe, die sich jede Woche oder jeden Monat sieht, ersetzt den Zufall. Wähle ein Thema, das dir Spaß macht, aus unserem [Verzeichnis](/entdecken/).

## Mach den ersten Schritt

Die meisten warten darauf, dass jemand anderes sich meldet. Schlag nach dem Treffen ein Kaffeetrinken oder einen gemeinsamen Spaziergang vor. Ein konkreter Vorschlag funktioniert besser als ein vages "Wir sollten mal was machen".

## Bleib dran, auch wenn es langsam geht

Wer Freundschaften aufbauen will, braucht Geduld. Es kann Monate dauern, bis aus Bekannten Freunde werden. Das ist kein Zeichen, dass etwas falsch läuft.

## Nutze Online und Offline zusammen

Ein Chat kann den Kontakt zwischen den Treffen halten. Gerade in lokalen Gruppen auf Discord oder Telegram entstehen Verabredungen. Mehr dazu in [Online-Communities richtig nutzen](/ratgeber/online-communities-richtig-nutzen/).

## Sei selbst jemand, der einlädt

Wer zu einem Spieleabend oder Spaziergang einlädt, wird oft zum Mittelpunkt der Gruppe. Du musst keine große Veranstaltung planen, ein kleiner Anlass reicht. Wenn du eine eigene Gruppe starten möchtest, lies unseren Beitrag [Eigene Community starten](/ratgeber/eigene-community-starten/).'''),
 dict(slug='eigene-community-starten', date='2026-10-15',
  title='Eigene Community starten: In 6 Schritten zur ersten Runde',
  desc='So startest du eine eigene Gruppe vor Ort: Thema, Format, Ort, Reichweite und wie du gefunden wirst.',
  lead='Du findest nichts Passendes? Dann gründe selbst etwas. Eine gute Gruppe braucht weniger, als du denkst: ein klares Thema, einen festen Termin und etwas Ausdauer.',
  body='''## 1. Wähle ein klares Thema

Je konkreter, desto besser: nicht "Leute treffen", sondern "Sonntagslauf im Park" oder "Brettspielabend für Einsteiger". Ein klares Thema zieht die richtigen Leute an.

## 2. Lege ein festes Format fest

Bestimme Wochentag, Uhrzeit und Ort und halte sie konstant. Regelmäßigkeit schafft Gewohnheit. Starte lieber mit einem monatlichen Termin, den du sicher einhältst, als mit einem wöchentlichen, der ausfällt.

## 3. Such dir einen einfachen Ort

Ein Park, ein Café oder ein Raum mit niedriger Hürde reicht. Kläre bei Cafés und Räumen kurz vorab, ob eine Gruppe willkommen ist.

## 4. Mach es leicht, mitzumachen

Schreib in die Ankündigung, dass Neue willkommen sind, nenne den Treffpunkt und einen Ansprechpartner. Je klarer, desto mehr Menschen trauen sich.

## 5. Sorge für Reichweite

Eine kleine Seite oder eine Instagram-Gruppe, ein Chat und Aushänge im Viertel reichen für den Start. Aufwendige Webseiten sind nicht nötig.

## 6. Lass dich finden

Trag deine Gruppe bei uns ein, damit Menschen, die danach suchen, sie finden. Wähle auf der [Anfrageseite](/kontakt/?thema=eintragen) das Thema "Meine Community eintragen" und beschreibe kurz Thema, Stadt und Link. Wir melden uns bei dir.

Bleib am Anfang geduldig: Viele Gruppen starten mit zwei, drei Personen und wachsen über Monate.'''),
]
