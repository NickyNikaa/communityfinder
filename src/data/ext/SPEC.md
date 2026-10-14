# Aufgabe: Datensammlung fuer FindeDeineLeute.de (Verzeichnis fuer Communities in deutschen Grossstaedten und online)

Ausgabe: reine Textdatei, EINE Zeile pro Eintrag, Felder getrennt durch "|" (keine "|" im Text), UTF-8:
Stadt|Name|Kategorie|URL|Beschreibung|Wann|Plattform

- Stadt: exakt einer der Namen aus der Staedteliste unten, oder "Online" fuer rein digitale Communities (dann ohne Stadtbezug).
- Name: offizieller Name der Gruppe/Community.
- Kategorie (genau eine ID): sport, outdoor, wellbeing, tanz, musik, kunst, foto, spiele, gaming, lernen, sprachen, essen, business, tech, leute, queer, frauen, familie, tiere, mobil, reisen, engagement, studium
- URL: Seite der Community selbst (Website, Instagram, Reddit, Discord-Vanity, t.me Kanal usw.). Nur URLs, die du in dieser Sitzung wirklich gesehen hast (Suchergebnis oder Abruf). KEINE erfundenen oder aus dem Gedaechtnis geratenen URLs. Lieber weniger, dafuer echte Eintraege.
- Beschreibung: 1 bis 2 Saetze in EIGENEN Worten auf Deutsch, was die Gruppe macht (nicht von der Seite kopieren). Keine Gedankenstriche (– oder —), keine Emojis, keine Werbesprache.
- Wann: Rhythmus/Ort falls bekannt (z. B. "Jeden Dienstag, 19 Uhr"), sonst leer lassen.
- Plattform: website, instagram, facebook, discord, telegram, whatsapp, reddit, slack, signal, meetup, forum, sonstige. Bei Facebook/Instagram/WhatsApp nur eintragen, wenn die Seite oeffentlich verlinkt ist.

Regeln:
- Nur real existierende, aktuell aktive Gruppen. Keine Firmen/Studios/Shops, keine Parteien, keine Anbieter kommerzieller Kurse. Vereine, Stammtische, Initiativen, Netzwerke, Clubs, Subreddits, Server, Kanaele sind richtig.
- Bereits vorhanden (nicht nochmals liefern): Run Clubs/parkrun, CCC-Erfa/Hackerspaces, Critical Mass, Urban Sketchers, Gemeinschaftsgaerten, DAV-Sektionen, Repair Cafes, Nerd Nite sowie der Basisdatensatz fuer Muenchen.
- WebFetch/WebSearch verwenden. Wenn eine Domain blockiert ist, NICHT per curl/Python umgehen, Eintrag dann nur aus Suchergebnissen belegen oder weglassen.
- Breite vor Tiefe: moeglichst viele der 79 Staedte abdecken, jede Stadt mit mehreren Eintraegen, plus Online.
- Datei fortlaufend schreiben (mehrfach an die Datei anhaengen), damit nichts verloren geht. Am Ende nur kurz melden: Dateipfad, Zeilenzahl, abgedeckte Staedte.

Staedteliste:
Berlin
Hamburg
München
Köln
Frankfurt am Main
Düsseldorf
Leipzig
Stuttgart
Dortmund
Bremen
Essen
Dresden
Nürnberg
Hannover
Duisburg
Bochum
Wuppertal
Bielefeld
Bonn
Mannheim
Karlsruhe
Münster
Augsburg
Wiesbaden
Mönchengladbach
Gelsenkirchen
Aachen
Braunschweig
Kiel
Chemnitz
Magdeburg
Freiburg im Breisgau
Krefeld
Halle (Saale)
Mainz
Erfurt
Lübeck
Oberhausen
Rostock
Kassel
Hagen
Potsdam
Saarbrücken
Hamm
Ludwigshafen am Rhein
Oldenburg
Mülheim an der Ruhr
Leverkusen
Darmstadt
Osnabrück
Solingen
Herne
Heidelberg
Paderborn
Neuss
Regensburg
Ingolstadt
Pforzheim
Würzburg
Offenbach am Main
Heilbronn
Fürth
Göttingen
Ulm
Wolfsburg
Reutlingen
Bremerhaven
Bottrop
Erlangen
Recklinghausen
Remscheid
Koblenz
Bergisch Gladbach
Jena
Trier
Salzgitter
Siegen
Moers
Kaiserslautern
