# Strategie: Communities und Treffen fuer eine Stadt finden (FindeDeineLeute.de)

Ziel: fuer die zugewiesene Stadt moeglichst viele ECHTE, aktive, offene Gruppen finden, bis mindestens 50 Eintraege in der Stadt stehen (bereits vorhandene zaehlen mit, siehe have-Datei).

Format und Regeln: /home/claude/work/repo/src/data/ext/SPEC.md (Stadt|Name|Kategorie|URL|Beschreibung|Wann|Plattform). Beschreibung in eigenen Worten, deutsch, keine Gedankenstriche, keine Emojis. Nur URLs, die du in dieser Sitzung wirklich gesehen hast. Doppelte vermeiden: have-Datei der Stadt (Name|Kategorie) lesen.

Was als Eintrag taugt: Vereine, Stammtische, Clubs, Initiativen, Netzwerke, Hochschulgruppen, Nachbarschafts- und Stadtteiltreffs, Mehrgenerationenhaeuser, offene Sport- und Hobbygruppen, Chore und Orchester mit offenen Proben, Spieletreffs, Lesekreise, Sprachcafes, Freiwilligen-Initiativen, Online-Gruppen mit Stadtbezug. Nicht: Firmen, Studios, Kursanbieter, Parteien, Shops, reine Veranstaltungsorte.

Quellen und Suchmuster (der Reihe nach durchgehen, jede ausschoepfen):
1. Websuche je Kategorie: "<Stadt> Stammtisch", "<Stadt> Verein offen fuer Neue", "<Stadt> Hobbygruppe", "<Stadt> Treffpunkt Neue Leute", "<Stadt> Meetup", plus Themen: Schach, Brettspiele, Rollenspiel, Tischtennis, Volleyball, Badminton, Frisbee, Klettern, Wandern, Radfahren, Laufgruppe, Chor, Orchester, Improtheater, Fotografie, Stricken, Lesekreis, Sprachcafe, Tandem, Toastmasters, Rotaract, Round Table, Kiwanis, Jugendring, Pfadfinder, Foodsharing, Repair Cafe, Gemeinschaftsgarten, Tauschring, Queer, Frauen, Eltern, Hunde, Gaming, LAN, Cosplay, Anime, Tanz (Salsa, Swing, Volkstanz), Kegeln, Boule, Ultimate, Quidditch, Roller Derby, Lacrosse, Rudern, Segeln, Imker, Kleingarten.
2. Stadtportal und Vereinsverzeichnis der Stadt (Vereinssuche, Ehrenamtsboerse, Freiwilligenagentur, Stadtteilzentren, Mehrgenerationenhaeuser, Stadtjugendring, Sportbund/Stadtsportverband mit Vereinsliste).
3. Hochschulen der Stadt: Liste der Hochschulgruppen, AStA/Studierendenwerk, ESN, AIESEC, Fachschaften mit offenen Treffen.
4. Meetup-Stadtseite und Luma, Eventbrite-Gruppen, Vereinsseiten, die Termine nennen.
5. Foren und Verzeichnisse: Reddit-Stadt-Subreddit (Abruf ist oft blockiert, dann Suchtreffer nutzen), InterNations, Expat-Foren, Discord-Server (disboard, discord.me), Telegram-Verzeichnisse (tgstat), Stadtteil-Seiten, Kleinanzeigen-Gruppen nur wenn oeffentlich verlinkt.
6. Bundesweite Verbandsseiten mit Standortlisten, die die Stadt aufzaehlen: z. B. Toastmasters, Rotaract, Round Table, Pfadfinder, DLRG/THW (nur offene Jugend/Engagement), Naturfreunde, NABU/BUND-Ortsgruppen, Chaos-Erfas, Schachbund, Tischtennis- und Volleyballvereine, Roller-Derby-Liga, Ultimate-Frisbee-Verband, Parkrun, Lauftreffs, Critical Mass, VCD, ADFC-Ortsgruppen, Seniorenakademie nur wenn altersoffen.
7. Wenn eine Seite 429 oder blockiert liefert: nicht per curl umgehen, andere Quelle nehmen.

Qualitaet: lieber echte Eintraege mit belegter URL als geratene. Pro Eintrag ein kurzer Satz, was man dort macht, und wenn bekannt Wochentag und Uhrzeit im Feld Wann (Format "Dienstags 19 Uhr" oder "Jeden 1. Mittwoch im Monat, 19 Uhr").

Lernprotokoll: Schreibe am Ende in /home/claude/work/research/learnings_<stadtslug>.md 5 bis 10 kurze Zeilen: welche Quellen und Suchmuster ergiebig waren (mit Trefferzahl), welche nicht, welche Domains blockiert waren, wie viele Eintraege insgesamt, ob 50 erreicht wurden und was fehlt.

## Gelernt aus den Piloten (Nuernberg: 68 neue, Remscheid: 53 neue)
Reihenfolge nach Ergiebigkeit, diese Quellen ZUERST abarbeiten:
1. Vereinsliste des Stadtsportbunds oder Stadtsportverbands der Stadt (z. B. "Sportbund <Stadt> Vereine"), je Verein ein Eintrag. Detailseiten nennen oft kein Angebot: dann kurzer Satz und Wann leer.
2. Stadtportal: Vereinsverzeichnis, Ehrenamts-/Freiwilligenboerse, Freiwilligenmesse-Teilnehmerliste, Kulturlaeden, Stadtteilzentren, Buergerhaeuser, Mehrgenerationenhaeuser, Stadtjugendring.
3. Hochschulen: Hochschulgruppen- und Studierendenorganisationen-Listen, Hochschulsport-Vereinsliste (nur Gruppen der eigenen Stadt).
4. PDFs der Stadt oder Medien: Vereinswegweiser, "Nacht der Kultur" Programmheft, Sportangebot-PDFs, Veranstaltungsbroschueren (liefern oft Zeiten und URLs).
5. Lauftreff-Listen (z. B. runnersworld), Verbandsseiten mit Standortlisten.
6. Gezielte Suche mit Vereinsbegriffen: "<Stadt> e.V. Treffen jeden Monat", "<Stadt> Verein Mitmachen".
Schwach (nur kurz probieren): allgemeine Suchen wie "<Stadt> Stammtisch", Meetup, Discord, Reddit, Chor; sie liefern meist Treffer aus anderen Staedten.
Nicht aufnehmen: reine Seniorenangebote, Parteien und parteinahe Gruppen, Gruppen aus Nachbarstaedten, Studios, Tanzschulen, Firmen.
Abrufe nacheinander machen, nicht viele gleichzeitig (Ratenlimit 429). Wenn ein Eintrag keine eigene Seite hat, die stabile Uebersichtsseite der Quelle als URL nehmen.
Haeufige Luecken, gezielt nachsuchen: Chor, Orchester, Pfadfinder, Fotoclub, Brettspiel, Hochschulgruppen, Online-Gruppen mit Stadtbezug.

## Mengen- und Qualitaetsregel (ab Welle 2)
Liefere ca. Ziel bis Ziel+15 neue Eintraege, nicht mehr. Hoechstens die Haelfte Sportvereine, der Rest soll vielfaeltig sein (Kultur, Engagement, Hobby, Stadtteil, Hochschule, Eltern, Queer, Natur, Spiele, Musik). Qualitaet vor Menge: bei Sportvereinen ohne Angaben ein ehrlich knapper Satz, nichts erfinden. Pflicht am Ende: Format pruefen (7 Felder, keine Gedankenstriche, keine Duplikate zur have-Datei), Lernprotokoll schreiben.
Aufgabenvorlage: Stadt(e) und Ziel stehen im Auftrag. have-Datei: /home/claude/work/research/have/<stadtslug>.txt. Ausgabe: /home/claude/work/repo/src/data/ext/stadt_<stadtslug>.txt (bei mehreren Staedten alle Zeilen in EINE Datei stadt_<erster slug>.txt, Stadtfeld je Zeile exakt der Staedtename). Lernprotokoll: /home/claude/work/research/learnings_<erster slug>.md.

## Weitere Learnings (Welle 1 und 2, Oktober 2026)
- JEDE Zeile braucht eine EIGENE URL (Vereinsseite, Gruppenseite). Mehrere Eintraege mit derselben URL (z. B. ein PDF oder eine Sportbund-Listenseite) verwirft build.py beim Bau. Beim Lesen einer Vereinsliste daher den Link zur Vereinsseite jedes Vereins mitnehmen, nicht die Listenseite.
- WebSearch hat ein gemeinsames Limit von 200 Aufrufen pro Arbeitsschritt (Turn) ueber alle parallelen Agenten. Hoechstens 8 Staedte-Agenten pro Turn starten, danach neuer Turn. Ergiebige Seitenabrufe (WebFetch) auf Vereinslisten sparen Suchen.
- Ergiebigste Quellen bisher: Kreis-/Stadtsportbund-Vereinslisten (50 bis 100 Vereine pro Stadt), Vereinsboersen-Broschueren der Stadtfeste (PDF), Ehrenamts- und Freiwilligenseiten, Hochschul-Studierendenlisten, Stadtjugendring-Mitgliederlisten, Chorlisten des Saengerkreises, Mehrgenerationenhaus-Angebote.
- Schwach: allgemeine Websuche nach Stammtisch, Meetup, Discord, Reddit (liefert Treffer anderer Staedte). Reddit-Abruf ist blockiert. robots.txt sperrt manche Stadtportale (ludwigshafen.de, oberhausen.de www9): dann Suchtreffer oder Fremdverzeichnisse (auskunft.de, golocal, dasoertliche) nutzen.
- socialrunclubs.de: Detailseiten liefern Wochentag und Uhrzeit von Run Clubs (automatisch zusammengestellt, nicht vom Club bestaetigt).
- Staedte, die nach der ersten Runde noch unter 50 liegen, brauchen eine zweite Runde mit gezielten Quellen (Stadtsportbund, Ehrenamt, Hochschule, Chor, Pfadfinder, Foto, Brettspiel).
