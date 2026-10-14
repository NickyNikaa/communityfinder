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
 dict(slug='einsamkeit-in-deutschland-zahlen-und-ursachen', date='2026-10-14',
  title='Einsamkeit in Deutschland: Zahlen, Ursachen und was die Forschung sagt',
  desc='Wie viele Menschen sind einsam, warum belastet Einsamkeit die Gesundheit und was unterscheidet Einsamkeit vom Alleinsein? Ein Überblick mit Studien.',
  lead='Einsamkeit ist kein Randthema. Sie betrifft Menschen jeden Alters, und die Forschung zeigt, dass sie nicht nur schmerzt, sondern auch die Gesundheit beeinflusst. Hier ein Überblick über die wichtigsten Zahlen und Erkenntnisse.',
  body='''## Einsamkeit ist nicht Alleinsein

Alleinsein beschreibt eine Situation: Du bist ohne andere Menschen. Einsamkeit beschreibt ein Gefühl: Du erlebst, dass deine Beziehungen weniger oder weniger tief sind, als du dir wünschst. Man kann allein sein und sich wohlfühlen, und man kann unter vielen Menschen einsam sein. Deshalb hilft es selten, einfach "mehr Leute zu treffen". Entscheidend ist, ob du dich verbunden fühlst.

## Wie viele Menschen sind betroffen?

Das Einsamkeitsbarometer des Bundesfamilienministeriums, das auf Daten des Sozio-oekonomischen Panels beruht, zeigt: 2017 lag der Anteil der Erwachsenen mit erhöhter Einsamkeitsbelastung bei 7,6 Prozent, im ersten Pandemiejahr 2020 bei 28,2 Prozent und 2021 bei 11,3 Prozent. Der Wert ging also nach dem Höhepunkt zurück, blieb aber über dem Niveau vor der Pandemie. 2020 waren junge Erwachsene zwischen 18 und 29 mit 31,8 Prozent stärker betroffen als Menschen über 75 mit 22,8 Prozent. Das [Einsamkeitsbarometer 2024](https://www.bmbfsfj.bund.de/resource/blob/240528/5a00706c4e1d60528b4fed062e9debcc/einsamkeitsbarometer-2024-data.pdf) macht auch klar: Einsamkeit ist nicht allein ein Thema des Alters.

Weltweit schätzt die Weltgesundheitsorganisation, dass etwa jeder sechste Mensch von Einsamkeit betroffen ist. Unter den 13 bis 29 Jährigen geben laut dem [WHO Bericht von 2025](https://www.who.int/news/item/30-06-2025-social-connection-linked-to-improved-heath-and-reduced-risk-of-early-death) 17 bis 21 Prozent an, sich einsam zu fühlen. Die WHO bringt Einsamkeit mit etwa 100 Todesfällen pro Stunde in Verbindung, das sind mehr als 871.000 pro Jahr. Solche Zahlen beschreiben Zusammenhänge und keine einfache Ursache, sie zeigen aber, wie ernst das Thema genommen wird.

## Was Einsamkeit mit der Gesundheit macht

Die Psychologin Julianne Holt-Lunstad und ihr Team werteten 2015 in einer [Meta-Analyse](https://scholarsarchive.byu.edu/facpub/7516) Studien zu Einsamkeit, sozialer Isolation und Sterblichkeit aus. Das Risiko früher zu sterben war bei Einsamkeit um etwa 26 Prozent erhöht, bei sozialer Isolation um etwa 29 Prozent und beim Alleinleben um etwa 32 Prozent. Die Ergebnisse waren über Geschlecht und Weltregion hinweg ähnlich.

Auch die [Harvard Study of Adult Development](https://hsph.harvard.edu/health-happiness/news/the-good-life-a-discussion-with-dr-robert-waldinger/) läuft seit 1938 und kommt zu einem ähnlichen Bild: Menschen mit engen, warmen Beziehungen bleiben im Schnitt gesünder und zufriedener. Auch im Einsamkeitsbarometer zeigt sich ein Zusammenhang mit der psychischen Gesundheit: 2021 hatten knapp 72 Prozent der einsamkeitsbelasteten Menschen eine unterdurchschnittliche psychische Gesundheit. Ob Einsamkeit die Ursache ist oder auch eine Folge, lässt sich daraus nicht sicher ablesen, vermutlich verstärken sich beide gegenseitig.

## Wer ist besonders betroffen?

Die Einsamkeitsforschung nennt unter anderem Menschen in Umbruchphasen (Umzug, Trennung, Jobverlust, Berufseinstieg), Menschen mit wenig Einkommen, Erwerbslose, pflegende Angehörige und Menschen, die einer Minderheit angehören. Die Fokusanalyse im [Einsamkeitsbarometer 2025](https://www.bmbfsfj.bund.de/resource/blob/266140/405c86f87b9ce075738f06b7f87fd12a/einsamkeitsbarometer-2025-data.pdf) fand zum Beispiel bei LSBTIQ* Personen mit 16,1 Prozent eine höhere Belastung als bei der Gesamtbevölkerung. Das ist eine Frage der Lebensumstände, nicht der Persönlichkeit.

## Was dagegen hilft

Einsamkeit lässt sich selten im Kopf lösen, sie braucht Begegnungen. Wiederkehrende Treffen mit denselben Menschen, ein gemeinsames Thema und niedrige Einstiegshürden sind erfahrungsgemäß der leichteste Weg. Genau dafür gibt es Gruppen: Du findest sie in unserer [Suche](/entdecken/) oder in den [Online-Communities](/online/). Wie die innere Spirale entsteht, die den ersten Schritt so schwer macht, liest du im Beitrag [Warum Einsamkeit sich selbst verstärkt](/ratgeber/einsamkeit-teufelskreis-durchbrechen/).

## Wenn es dich stark belastet

Wenn du dich über längere Zeit niedergeschlagen, hoffnungslos oder wie abgeschnitten fühlst, such dir bitte Unterstützung. Die Telefonseelsorge ist kostenlos und rund um die Uhr erreichbar unter 0800 111 0 111 und 0800 111 0 222, und deine Hausärztin oder dein Hausarzt kann dich weitervermitteln. Dieser Beitrag ersetzt keine Beratung oder Behandlung.'''),
 dict(slug='einsamkeit-teufelskreis-durchbrechen', date='2026-10-14',
  title='Warum Einsamkeit sich selbst verstärkt und wie du den Kreislauf durchbrichst',
  desc='Einsamkeit verändert, wie wir andere wahrnehmen. Was die Psychologie über den Teufelskreis weiß und welche kleinen Schritte helfen.',
  lead='Je länger man einsam ist, desto schwerer fällt oft der Kontakt. Das ist keine Schwäche, sondern ein bekanntes psychologisches Muster. Wer es kennt, kann es unterbrechen.',
  body='''## Einsamkeit als Warnsignal

Nach der evolutionären Theorie von John und Stephanie Cacioppo ist Einsamkeit ein Signal, ähnlich wie Hunger: Sie zeigt an, dass uns Verbindung fehlt, und drängt uns dazu, sie zu suchen. Das Problem beginnt, wenn das Signal lange anhält. Dann verändert sich, wie wir andere wahrnehmen.

## Was die Forschung zeigt

Ein Team um Kory Floyd untersuchte 2022 im Fachjournal OBM Neurobiology, wie Einsamkeit Wahrnehmung beeinflusst ([Studie](https://experts.arizona.edu/en/publications/examining-the-social-signaling-and-person-perception-functions-of/)). 480 Beobachtende sahen Videos von Menschen, die sich vorstellten und zuvor ihre Einsamkeit eingeschätzt hatten. Zwei Befunde fallen auf. Erstens erkannten die Beobachtenden einsame Personen häufiger richtig, als der Zufall erwarten lässt, es gibt also Signale im Auftreten, die andere wahrnehmen. Zweitens bewerteten Beobachtende, die selbst einsamer waren, die Sprechenden negativer. Einsamkeit färbt also den Blick auf andere.

## Der Kreislauf in vier Schritten

Wer sich einsam fühlt, rechnet eher mit Ablehnung und hält sich zurück. Zurückhaltung wirkt auf andere distanziert, und Kontakte bleiben aus. Das bestätigt das Gefühl, nicht dazuzugehören, und der Rückzug wird größer. Dieser Kreislauf ist kein Charakterfehler, sondern eine nachvollziehbare Reaktion. Gut ist, dass jeder Schritt eine Stelle bietet, an der man ihn unterbrechen kann.

## So unterbrichst du ihn

Nimm deine Annahmen nicht als Tatsachen. Der Gedanke "Die wollen mich nicht dabeihaben" ist eine Vermutung, die du bei einem Treffen prüfen kannst. Gehe in kleinen Schritten vor und setze dir Ziele wie "Ich bleibe eine Stunde" oder "Ich spreche mit zwei Personen". Such dir Formate mit Struktur, etwa eine Laufgruppe oder einen Spieleabend, dort gibt es Gesprächsstoff. Und plane Wiederholung ein: Das erste Treffen fühlt sich oft schwer an, das dritte deutlich leichter. Wie du den ersten Besuch vorbereitest, steht im Beitrag [Allein zum ersten Treffen](/ratgeber/allein-zum-ersten-treffen/).

## Sei freundlich zu dir

Viele erklären sich ihre Einsamkeit mit eigenen Mängeln. Die Forschung sieht eher Lebensumstände und Muster als Ursache. Sprich mit jemandem, wenn dich das Thema belastet, und hol dir bei anhaltender Niedergeschlagenheit professionelle Hilfe, zum Beispiel über die Hausarztpraxis oder die Telefonseelsorge unter 0800 111 0 111.'''),
 dict(slug='kleine-kontakte-grosse-wirkung', date='2026-10-14',
  title='Kleine Kontakte, große Wirkung: Warum Gespräche mit Fremden guttun',
  desc='Auch flüchtige Gespräche mit Bekannten und Fremden heben die Stimmung. Was die Forschung zu schwachen Bindungen sagt und wie du es ausprobierst.',
  lead='Nicht jeder Kontakt muss tief sein. Studien zeigen, dass auch kurze Begegnungen mit Bekannten und Fremden das Wohlbefinden steigern. Das nimmt den Druck, sofort Freundschaften zu schließen.',
  body='''## Was schwache Bindungen sind

Schwache Bindungen sind Menschen, die du kennst oder siehst, ohne eng befreundet zu sein: die Barista, die Nachbarin, der Mann aus dem Lauftreff. Die Psychologin Gillian Sandstrom von der University of Sussex untersucht, was solche Kontakte bewirken. In einer Studie aus dem Jahr 2014 zählten etwa 50 Teilnehmende sechs Tage lang ihre Gespräche. Wer mehr Gespräche mit schwachen Bindungen führte, war im Schnitt zufriedener, und an Tagen mit mehr solchen Kontakten ging es jedem Einzelnen besser. Diese Befunde schildert der Beitrag von [NPR](https://www.npr.org/sections/goatsandsoda/2023/08/23/1193148718/why-a-strangers-hello-can-do-more-than-just-brighten-your-day).

## Auch kleine Begegnungen zählen

In einer späteren Studie in einem Café in Vancouver waren Menschen, die kurz mit der Person am Tresen sprachen, besser gelaunt und fühlten sich stärker zugehörig. Hanne Collins von der Harvard Business School fand in Daten aus acht Ländern, dass Menschen zufriedener waren, wenn ihre täglichen Gespräche eine größere Vielfalt an Beziehungen umfassten. Der Psychiater Robert Waldinger, der die Harvard Study of Adult Development leitet, rät dazu, mit Smalltalk anzufangen, weil die meisten Menschen positiv darauf reagieren.

## Warum das für dich wichtig ist

Wenn dir enge Freundschaften fehlen, wirkt der Weg dorthin riesig. Schwache Bindungen sind ein Zwischenschritt: Sie geben das Gefühl, gesehen zu werden, und können sich mit der Zeit vertiefen. Wer einmal in der Woche dieselbe Gruppe sieht, wird vom Gesicht zur Bekanntschaft und manchmal zum Freund.

## Drei Dinge zum Ausprobieren

Sprich diese Woche an einem festen Ort mit jemandem, den du öfter siehst, zum Beispiel im Café oder im Hausflur. Geh zu einer Gruppe mit festem Termin, etwa einer [Laufgruppe](/ratgeber/run-club-finden-und-einsteigen/) oder einem Stammtisch, und zähle dein Ziel in Gesprächen, nicht in Freundschaften. Und stelle nach dem ersten Satz eine Frage, die zum Ort passt, etwa nach dem Weg, dem Spiel oder dem Projekt.

Eine Gruppe in deiner Stadt findest du über die [Suche](/entdecken/) oder die [Städteübersicht](/staedte/).'''),
 dict(slug='einsamkeit-podcasts-studien-quellen', date='2026-10-14',
  title='Einsamkeit verstehen: Podcasts, Studien und Anlaufstellen',
  desc='Hörenswerte Podcasts, wichtige Studien und hilfreiche Anlaufstellen rund um das Thema Einsamkeit, deutschsprachig und international.',
  lead='Wer sich mit Einsamkeit beschäftigen möchte, findet inzwischen gute Podcasts, Berichte und Studien. Hier eine Auswahl, die wir selbst gelesen und gehört haben.',
  body='''## Podcasts auf Deutsch

In der Folge [#168 des Podcasts Rebellisch gesund](https://www.podcast.de/episode/703843997/168-einsamkeit-warum-sie-uns-alle-betrifft-mit-einsamkeitsforscherin-prof-dr-maike-luhmann) spricht die Einsamkeitsforscherin Prof. Dr. Maike Luhmann darüber, wie Einsamkeit entsteht, warum sie in eine negative Spirale führen kann und was davor schützt. Die Folge dauert gut eine Stunde.

Die Bundeszentrale für politische Bildung beschäftigt sich im Landwärts-Podcast "Einsam, und jetzt?" mit gesellschaftlichen Folgen. In der ersten Folge, [Einsamkeit und Demokratie](https://www.bpb.de/mediathek/podcasts/571694/01-einsamkeit-und-demokratie/) (Oktober 2025), geht es unter anderem um Risikofaktoren und darum, wie Einsamkeit mit politischem Rückzug zusammenhängen kann.

Der Podcast Gesundheit zum Hören der Techniker Krankenkasse hat eine Folge zum Thema: [Einsamkeit und ihre gesundheitlichen Folgen](https://www.tk.de/techniker/gesundheit-foerdern/digitale-gesundheit/podcasts/einsamkeit-und-ihre-gesundheitlichen-folgen-2149090) mit der Psychologin Dr. Susanne Bücker, unter anderem dazu, wann Einsamkeit zum Gesundheitsrisiko wird.

## Zum Weiterhören auf Englisch

Robert Waldinger, der die Harvard Study of Adult Development leitet, spricht im TED Format über die Frage, was ein gutes Leben ausmacht: [How to lead a happier, more fulfilling life](https://www.ted.com/pages/how-to-lead-a-happier-more-fulfilling-life-with-dr.-robert-waldinger). Seine Kernaussage: Die Qualität unserer Beziehungen ist ein starker Hinweis darauf, wie gesund und zufrieden wir alt werden.

## Berichte und Studien

Das [Einsamkeitsbarometer des Bundesfamilienministeriums](https://www.bmbfsfj.bund.de/resource/blob/240528/5a00706c4e1d60528b4fed062e9debcc/einsamkeitsbarometer-2024-data.pdf) fasst die Entwicklung von Einsamkeit in Deutschland über Jahrzehnte zusammen. Spätere Ausgaben vertiefen einzelne Gruppen, die [Ausgabe 2025](https://www.bmbfsfj.bund.de/resource/blob/266140/405c86f87b9ce075738f06b7f87fd12a/einsamkeitsbarometer-2025-data.pdf) zum Beispiel LSBTIQ* Personen, die [Ausgabe 2026](https://www.bmbfsfj.bund.de/bmbfsfj/service/publikationen/einsamkeitsbarometer-2026-286390) Menschen mit Behinderungen.

Die Weltgesundheitsorganisation hat im Juni 2025 einen [Bericht zu sozialer Verbundenheit](https://www.who.int/news/item/30-06-2025-social-connection-linked-to-improved-heath-and-reduced-risk-of-early-death) veröffentlicht. Die bekannteste Meta-Analyse zu Einsamkeit und Sterblichkeit stammt von [Holt-Lunstad und Kollegen (2015)](https://scholarsarchive.byu.edu/facpub/7516). Über Gespräche mit Fremden berichtet [NPR](https://www.npr.org/sections/goatsandsoda/2023/08/23/1193148718/why-a-strangers-hello-can-do-more-than-just-brighten-your-day), über die Wahrnehmung anderer bei Einsamkeit eine [Studie von Floyd und Kollegen (2022)](https://experts.arizona.edu/en/publications/examining-the-social-signaling-and-person-perception-functions-of/).

## Anlaufstellen, wenn es dich belastet

Die Telefonseelsorge ist kostenlos und rund um die Uhr erreichbar, unter 0800 111 0 111 und 0800 111 0 222. Deine Hausarztpraxis kann dich bei anhaltender Niedergeschlagenheit weitervermitteln. Dieser Beitrag ersetzt keine Beratung oder Behandlung.

## Vom Wissen zum Handeln

Verstehen hilft, aber Verbindung entsteht durch Begegnung. Stöbere in unserem [Verzeichnis](/entdecken/), wähle eine Gruppe mit festem Termin und geh ein zweites Mal hin. Und wenn du eine Gruppe leitest und möchtest, dass andere dich finden, lies [Eigene Community starten](/ratgeber/eigene-community-starten/).'''),
 dict(slug='neu-in-der-stadt-leute-kennenlernen', date='2026-10-14',
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
 dict(slug='run-club-finden-und-einsteigen', date='2026-10-14',
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
 dict(slug='hobby-gruppe-finden', date='2026-10-14',
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
 dict(slug='online-communities-richtig-nutzen', date='2026-10-14',
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
 dict(slug='allein-zum-ersten-treffen', date='2026-10-14',
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
 dict(slug='verein-oder-lockere-gruppe', date='2026-10-14',
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
 dict(slug='freunde-finden-als-erwachsener', date='2026-10-14',
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
 dict(slug='eigene-community-starten', date='2026-10-14',
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

 dict(slug='neue-kontakte-knuepfen', date='2026-10-14',
  title='Neue Kontakte knüpfen: Warum es schwerer geworden ist und wie es trotzdem klappt',
  desc='Neue Leute kennenlernen fühlt sich heute oft schwieriger an als früher. Warum das so ist und welche einfachen Schritte wirklich helfen.',
  lead='Wenn du dich fragst, warum es dir so schwerfällt, neue Menschen kennenzulernen, bist du damit nicht allein. Es liegt selten an dir, sondern an den Bedingungen, unter denen wir heute leben.',
  body='''## Warum es mit der Zeit schwerer wird

In Schule, Ausbildung oder Studium entstehen Freundschaften fast von selbst: Man sieht dieselben Menschen jeden Tag, ohne Plan, ohne Termin. Im Berufsleben fällt genau das weg. Wir ziehen um, wechseln den Job, haben weniger freie Zeit und mehr Verpflichtungen. Kontakte müssen plötzlich aktiv gesucht werden, und das fühlt sich ungewohnt und manchmal peinlich an.

Dazu kommt ein verbreiteter Denkfehler: Wir unterschätzen, wie sehr andere sich über Kontakt freuen. Die Forschung nennt das den Sympathie-Lücke-Effekt. In Studien von Erica Boothby und Kollegen unterschätzten Menschen nach Gesprächen mit Fremden systematisch, wie sehr ihr Gegenüber sie mochte ([Studie in Psychological Science](https://doi.org/10.1177/0956797617741719)). Die Unsicherheit ist also meist größer als der Grund dafür.

## Ansprechen lohnt sich mehr, als es sich anfühlt

Nicholas Epley und Juliana Schroeder ließen Pendler im Zug entweder still bleiben oder ein Gespräch mit Sitznachbarn beginnen. Das Ergebnis: Wer redete, erlebte die Fahrt als angenehmer. Die Teilnehmenden hatten vorher das Gegenteil erwartet ([Studie im Journal of Experimental Psychology](https://doi.org/10.1037/a0037323)). Das Gespräch war fast immer besser als die Vorhersage.

## Ein einfacher Plan für den Anfang

Setz dich nicht unter Druck, sofort Freunde zu finden. Ziel ist zuerst, regelmäßig dieselben Menschen zu sehen. Vertrautheit entsteht durch Wiederholung.

Wähle eine Aktivität, die du ohnehin magst, und gehe mehrmals hin. Ein Lauftreff, ein Spieleabend, ein Sprachkurs oder ein Verein eignen sich gut, weil man etwas gemeinsam tut und nicht ständig reden muss. Passende Gruppen in deiner Stadt findest du über den [Verzeichnis-Filter](/entdecken/), online über die [Online-Communities](/online/).

Gib einer Gruppe mindestens drei bis vier Besuche, bevor du entscheidest, ob sie zu dir passt. Beim ersten Mal kennt dich noch niemand, beim dritten Mal schon.

## Kleine Sätze, die Türen öffnen

Du brauchst keine geistreichen Einstiege. Funktionieren tun einfache Fragen: Wie lange bist du schon dabei? Wie bist du darauf gekommen? Kennst du noch andere Orte dafür? Danach folgt oft von selbst ein Gespräch. Und wenn es sich gut anfühlt, schlag am Ende vor: "Bist du nächste Woche auch dabei?"

## Aus einem Treffen wird eine Freundschaft

Der entscheidende Schritt kommt nach dem Treffen. Tausch Nummern aus und melde dich einmal selbst, zum Beispiel mit einem Foto oder einem Gruß vom Abend. Schlage dann etwas Konkretes vor, etwa einen Kaffee nach dem Training. Wer vage bleibt ("man müsste mal"), verabredet sich selten. Mehr dazu in [Freunde finden als Erwachsener](/ratgeber/freunde-finden-als-erwachsener/) und [Allein zum ersten Treffen](/ratgeber/allein-zum-ersten-treffen/).

## Wenn es trotzdem schwerfällt

Manchmal ist die Einsamkeit so groß, dass schon der erste Schritt zu viel ist. Das ist keine Schwäche. Mehr Hintergründe findest du in unserem Beitrag zum [Teufelskreis der Einsamkeit](/ratgeber/einsamkeit-teufelskreis-durchbrechen/). Wenn dich die Situation sehr belastet, kannst du jederzeit kostenlos und anonym die Telefonseelsorge unter 0800 111 0 111 anrufen.'''),
 dict(slug='social-media-echte-verbindung', date='2026-10-14',
  title='Social Media und echte Verbindung: Warum Kontakte online oft nicht tragen',
  desc='Tausende Kontakte, trotzdem einsam? Warum die vermeintliche Verbindung in sozialen Netzwerken echte Nähe nicht ersetzt und was stattdessen hilft.',
  lead='Nie war es leichter, mit anderen in Verbindung zu bleiben, und doch fühlen sich viele Menschen einsamer. Das ist kein Widerspruch, sondern hat mit der Art zu tun, wie Verbindung online entsteht.',
  body='''## Verbunden wirken ist nicht verbunden sein

Likes, Storys und Nachrichten geben uns kurze Signale von Zugehörigkeit. Sie fühlen sich nach Kontakt an, verlangen aber kaum etwas: keine Verabredung, keine Verletzlichkeit, kein Zuhören über eine Stunde. Echte Nähe entsteht dort, wo man Zeit teilt, sich zeigt und Verlässlichkeit erlebt. Das lässt sich über Bildschirme nur begrenzt herstellen.

## Was die Forschung dazu sagt

Melissa Hunt und ihr Team an der University of Pennsylvania ließen Studierende ihre Social-Media-Zeit auf etwa 30 Minuten pro Tag begrenzen. Nach drei Wochen berichteten sie von weniger Einsamkeit und weniger depressiven Symptomen als die Kontrollgruppe ([Studie im Journal of Social and Clinical Psychology](https://doi.org/10.1521/jscp.2018.37.10.751)).

Ethan Kross und Kollegen fanden bei jungen Erwachsenen, dass häufigere Facebook-Nutzung mit einem schlechteren Wohlbefinden in den folgenden Wochen zusammenhing ([Studie in PLoS One](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0069841)). Wichtig: Diese Studien zeigen Zusammenhänge in bestimmten Gruppen. Sie belegen nicht, dass soziale Netzwerke grundsätzlich schaden. Entscheidend scheint, wie wir sie nutzen: Wer vor allem scrollt und vergleicht, fühlt sich schlechter als jemand, der gezielt Menschen schreibt und Treffen verabredet.

## Der Vergleich macht es schwerer

Online sehen wir die Höhepunkte der anderen: Reisen, Feiern, große Freundesgruppen. Daneben wirkt das eigene Leben leer. Dabei verfügen die meisten dieser Menschen ebenfalls über wenige enge Beziehungen. Das Bild verzerrt, und es verstärkt den Gedanken, dass mit einem selbst etwas nicht stimmt.

## Einseitige Nähe

Folgen wir Creatorn und Podcasts, entsteht ein Gefühl von Vertrautheit, ohne dass die Person uns kennt. Die Medienforschung spricht von parasozialen Beziehungen. Der Begriff geht auf Horton und Wohl zurück, die ihn 1956 prägten. Solche Beziehungen sind nicht schlimm und können Trost spenden. Sie ersetzen aber keinen Menschen, der dich zurückruft.

## Was stattdessen hilft

Du musst das Smartphone nicht verteufeln. Nutze es als Werkzeug, um Menschen zu treffen, nicht um Treffen zu ersetzen.

Schreib einer konkreten Person und schlage ein Datum vor. Tritt einer Gruppe bei, die sich regelmäßig draußen trifft. Setz dir feste, kleine Zeitfenster für Social Media, etwa 30 Minuten am Tag. Und mach aus einer Online-Bekanntschaft schnell ein Treffen im echten Leben, am besten an einem öffentlichen Ort. Wie das gelingt, steht in [Online-Communities richtig nutzen](/ratgeber/online-communities-richtig-nutzen/).

## Ein Anfang, der klein bleiben darf

Fang mit einer Verabredung pro Woche an. Das ist wenig, und doch verändert es mit der Zeit, wen du regelmäßig siehst. Passende Gruppen findest du im [Verzeichnis](/entdecken/). Mehr zu Hintergründen und Studien: [Einsamkeit in Deutschland](/ratgeber/einsamkeit-in-deutschland-zahlen-und-ursachen/) und [Podcasts, Studien und Quellen](/ratgeber/einsamkeit-podcasts-studien-quellen/).

Wenn dich Einsamkeit stark belastet, hilft die Telefonseelsorge kostenlos und anonym unter 0800 111 0 111.'''),
]
