# -*- coding: utf-8 -*-
CITIES = """Berlin|berlin
Hamburg|hamburg
München|muenchen
Köln|koeln
Frankfurt am Main|frankfurt-am-main
Düsseldorf|duesseldorf
Leipzig|leipzig
Stuttgart|stuttgart
Dortmund|dortmund
Bremen|bremen
Essen|essen
Dresden|dresden
Nürnberg|nuernberg
Hannover|hannover
Duisburg|duisburg
Bochum|bochum
Wuppertal|wuppertal
Bielefeld|bielefeld
Bonn|bonn
Mannheim|mannheim
Karlsruhe|karlsruhe
Münster|muenster
Augsburg|augsburg
Wiesbaden|wiesbaden
Mönchengladbach|moenchengladbach
Gelsenkirchen|gelsenkirchen
Aachen|aachen
Braunschweig|braunschweig
Kiel|kiel
Chemnitz|chemnitz
Magdeburg|magdeburg
Freiburg im Breisgau|freiburg-im-breisgau
Krefeld|krefeld
Halle (Saale)|halle-saale
Mainz|mainz
Erfurt|erfurt
Lübeck|luebeck
Oberhausen|oberhausen
Rostock|rostock
Kassel|kassel
Hagen|hagen
Potsdam|potsdam
Saarbrücken|saarbruecken
Hamm|hamm
Ludwigshafen am Rhein|ludwigshafen-am-rhein
Oldenburg|oldenburg
Mülheim an der Ruhr|muelheim-an-der-ruhr
Leverkusen|leverkusen
Darmstadt|darmstadt
Osnabrück|osnabrueck
Solingen|solingen
Herne|herne
Heidelberg|heidelberg
Paderborn|paderborn
Neuss|neuss
Regensburg|regensburg
Ingolstadt|ingolstadt
Pforzheim|pforzheim
Würzburg|wuerzburg
Offenbach am Main|offenbach-am-main
Heilbronn|heilbronn
Fürth|fuerth
Göttingen|goettingen
Ulm|ulm
Wolfsburg|wolfsburg
Reutlingen|reutlingen
Bremerhaven|bremerhaven
Bottrop|bottrop
Erlangen|erlangen
Recklinghausen|recklinghausen
Remscheid|remscheid
Koblenz|koblenz
Bergisch Gladbach|bergisch-gladbach
Jena|jena
Trier|trier
Salzgitter|salzgitter
Siegen|siegen
Moers|moers
Kaiserslautern|kaiserslautern"""

# Critical Mass: Stadt|Termin|Treffpunkt (radfahren.de, Tabelle 2026)
CM = """Aachen|Letzter Freitag, 18 Uhr|Elisenbrunnen
Augsburg|Letzter Freitag, 18 Uhr|Rathausplatz
Berlin|1. Sonntag, 14 Uhr, und letzter Freitag, 20 Uhr|Brandenburger Tor bzw. Heinrichplatz
Bielefeld|Letzter Freitag, 19 Uhr|Kesselbrink
Bochum|Letzter Freitag, 19 Uhr|Hofgarten
Bonn|Letzter Freitag, 18 Uhr|Rathausplatz
Bottrop|1. Freitag, 19 Uhr|Berliner Platz
Braunschweig|Letzter Freitag, 19 Uhr|Hauptbahnhof Vorplatz
Bremen|Letzter Freitag, 19 Uhr|Hollerallee / Gustav-Deetjen-Allee
Chemnitz|Letzter Freitag, 18 Uhr|Bahnhofsvorplatz
Darmstadt|2. Freitag, 19 Uhr|Marktplatz
Dortmund|3. Freitag, 19 Uhr|Friedensplatz
Dresden|Letzter Freitag, 18:30 Uhr|Halfpipe Lignerallee
Duisburg|Letzter Freitag, 19 Uhr|Plymouthplatz
Düsseldorf|2. Freitag, 19 Uhr|Fürstenplatz
Erfurt|Letzter Freitag, 18:30 Uhr|Bahnhofsvorplatz
Erlangen|1. Mittwoch, 19 Uhr|Schlossplatz
Essen|2. Freitag, 19 Uhr|Willy-Brandt-Platz
Frankfurt am Main|1. Sonntag, 14 Uhr, und darauffolgender Freitag, 19 Uhr|Alte Oper
Freiburg im Breisgau|Letzter Freitag, 18 Uhr|Theatervorplatz
Fürth|3. Freitag, 18 Uhr|Paradiesbrunnen
Gelsenkirchen|3. Montag, 19 Uhr|Hans-Sachs-Haus
Hagen|2. Freitag, 19 Uhr|Hauptbahnhof
Halle (Saale)|1. Freitag, 18 Uhr|August-Bebel-Platz
Hamburg|Letzter Freitag, 19 Uhr|Wechselnde Treffpunkte
Hannover|Letzter Freitag, 18:30 Uhr|Klagesmarkt
Heidelberg|Letzter Freitag, 18 Uhr|Universitätsplatz
Heilbronn|1. Freitag, 18:42 Uhr|Götzenturmbrücke
Karlsruhe|Letzter Freitag, 18 Uhr|Kronenplatz
Kassel|Letzter Freitag, 18 Uhr|Fridericianum
Kiel|Letzter Freitag, 19 Uhr|Platz der Kieler Matrosen
Koblenz|1. Donnerstag, 17:30 Uhr|Löhrrondell
Köln|Letzter Freitag, 17:30 Uhr|Rudolfplatz
Krefeld|Letzter Freitag, 18 Uhr|Hauptbahnhof Vorplatz
Leipzig|Letzter Freitag, 18 Uhr|Augustusplatz
Ludwigshafen am Rhein|1. Freitag, 18 Uhr|Pfalzplatz
Lübeck|1. Freitag, 19 Uhr|Lindenteller
Magdeburg|Letzter Freitag, 19 Uhr|Elbbalkon
Mainz|1. Freitag, 18 bis 19 Uhr|Staatstheater
Mannheim|3. Freitag, 18:30 Uhr|Wasserturm
Mönchengladbach|Letzter Freitag, 19 Uhr|Schillerplatz
München|Letzter Freitag, 18 Uhr|Max-Joseph-Platz
Münster|Letzter Freitag, 19 Uhr|Domplatz
Nürnberg|Letzter Freitag, 18 Uhr|Opernhaus
Offenbach am Main|Letzter Freitag, 19 Uhr|Isenburger Schloss
Oldenburg|Letzter Freitag, 18:30 Uhr|Hauptbahnhof
Osnabrück|Letzter Freitag, 19 Uhr|Osnabrückhalle
Paderborn|Letzter Freitag, 18 Uhr|Hauptbahnhof
Pforzheim|Letzter Freitag, 19 Uhr|Waisenhausplatz
Potsdam|1. Freitag, 18:30 Uhr|Luisenplatz, Springbrunnen
Regensburg|Letzter Freitag, 17 Uhr|Schwammerl
Reutlingen|Letzter Freitag, 18 Uhr|Stadthalle
Saarbrücken|Letzter Freitag, 18:30 Uhr|Max-Ophüls-Platz
Stuttgart|1. Freitag, 18:30 Uhr|Feuersee
Ulm|Letzter Freitag, 18:30 Uhr|Münsterplatz
Wiesbaden|3. Freitag, 18:30 Uhr|Hauptbahnhof
Wuppertal|1. Freitag, 19 Uhr|CinemaxX"""

# Chaos Computer Club: Stadt|Name|URL (ccc.de Erfa-Kreise und Chaostreffs)
CCC = """Aachen|CCC Aachen|https://ccc.ac
Berlin|CCC Berlin, Club Discordia|https://berlin.ccc.de
Bremen|CCC Bremen|https://ccchb.de
Chemnitz|CCC Chemnitz|https://chaoschemnitz.de
Darmstadt|CCC Darmstadt|https://chaos-darmstadt.de
Dortmund|CCC Dortmund|https://chaostreff-dortmund.de
Dresden|CCC Dresden (c3d2)|https://c3d2.de
Düsseldorf|Chaosdorf Düsseldorf|https://chaosdorf.de
Erlangen|Bits'n'Bugs Erlangen|https://erlangen.ccc.de
Essen|Chaospott Essen|https://chaospott.de
Frankfurt am Main|CCC Frankfurt am Main|https://ccc-ffm.de
Freiburg im Breisgau|CCC Freiburg|https://cccfr.de
Göttingen|CCC Göttingen|https://chaostreff-goettingen.de
Hamburg|CCC Hamburg|https://hamburg.ccc.de
Hannover|CCC Hannover|https://hannover.ccc.de
Kaiserslautern|Chaos inKL|https://chaos-inkl.de
Karlsruhe|Entropia Karlsruhe|https://entropia.de
Kassel|flipdot Kassel|https://kassel.ccc.de
Köln|c4 Cologne|https://koeln.ccc.de
Leipzig|dezentrale Leipzig|https://dezentrale.space
Lübeck|Chaotikum Lübeck|https://chaotikum.org
Mainz|CCC Mainz/Wiesbaden|https://cccmz.de
Wiesbaden|CCC Mainz/Wiesbaden|https://cccmz.de
Mannheim|CCC Mannheim|https://ccc-mannheim.de
München|µC³ Munich|https://muc.ccc.de
Paderborn|CCC Paderborn|https://c3pb.de
Siegen|Chaos Siegen|https://c3si.de
Stuttgart|CCC Stuttgart|https://cccs.de
Ulm|Chaostreff Ulm|https://ulm.ccc.de
Würzburg|Nerd2Nerd Würzburg|https://nerd2nerd.org
Augsburg|OpenLab Augsburg|https://openlab-augsburg.de
Bielefeld|Hackerspace Bielefeld|http://hackerspace-bielefeld.de/
Bochum|Das Labor Bochum|https://das-labor.org
Bonn|Datenburg Bonn|https://datenburg.org/
Erfurt|Bytespeicher Erfurt|https://www.bytespeicher.org/
Halle (Saale)|Chaostreff Halle (Saale), Eigenbaukombinat|https://eigenbaukombinat.de
Hamm|c3hamm|https://chaos.social/@c3hamm
Heidelberg|NoName e.V. Heidelberg|https://www.noname-ev.de
Ingolstadt|bytewerk Ingolstadt|http://www.bytewerk.org/
Jena|Offener Chaostreff Jena, Krautspace|https://kraut.space/
Kiel|Science Monday Kiel, Toppoint|http://toppoint.de/
Münster|warpzone Münster|http://www.warpzone.ms/
Neuss|fnordeingang Neuss|https://fnordeingang.de/chaostreff
Nürnberg|Chaostreff Nürnberg|https://chaostreff-nuernberg.de
Osnabrück|Chaostreff Osnabrück|https://chaostreff-osnabrueck.de/
Potsdam|Chaostreff Potsdam, machBar|https://www.ccc-p.org/
Recklinghausen|Chaostreff Recklinghausen, Hackerhütte|http://c3re.de
Regensburg|Binary Kitchen Regensburg|http://binary.kitchen
Saarbrücken|hacksaar Saarbrücken|https://www.hacksaar.de
Trier|Maschinendeck Trier|http://www.maschinendeck.org
Wuppertal|Chaostreff Wuppertal, chaostal|https://www.chaostal.de/category/meeting"""

# Urban Sketchers (urbansketchers.de, Regionalgruppen)
USK = "Aachen,Berlin,Bonn,Braunschweig,Bremen,Düsseldorf,Erlangen,Göttingen,Hamburg,Hannover,Heidelberg,Karlsruhe,Koblenz,Köln,Leipzig,Lübeck,Magdeburg,München,Osnabrück,Regensburg,Stuttgart,Augsburg,Bielefeld,Bochum,Chemnitz,Dortmund,Dresden,Essen,Freiburg im Breisgau,Hagen,Ingolstadt,Jena,Kassel,Kiel,Mannheim,Nürnberg,Paderborn,Potsdam,Saarbrücken,Trier,Ulm,Würzburg".split(",")

# Gemeinschaftsgarten-Netzwerke (urbane-gaerten.de, Lokale Gartennetzwerke)
GARDEN = """Augsburg|Arbeitskreis Urbane Gärten Augsburg|http://www.urbane-gaerten.org/
Berlin|Netzwerk Urbane Gärten Berlin|https://www.netzwerkurbanegaertenberlin.org/
Berlin|Gemeinschaftsgärtnern Berlin|https://www.berlin.de/gemeinschaftsgaertnern/
Bonn|Gemeinschaftsgärten Bonn|https://bonnimwandel.de/gartnern-in-bonn/
Bottrop|Gemeinschaftsgärten Bottrop|http://gemeinsinnschafftgarten.de/die-gaerten
Braunschweig|Gartennetzwerk Braunschweig|https://gartennetzwerk.inbraunschweig.org/aktuell
Chemnitz|Netzwerk urbane Gärten und Farmen|https://www.sprossachse.org/sdb/wir/
Dortmund|Querbeet Dortmund|https://www.dortmund.de/themen/foerderungen/querbeet-dortmund/
Dresden|Gartennetzwerk Dresden|https://www.dresden-pflanzbar.de/
Essen|Gemeinschaftsgärten Essen|https://gemeinschaftsgartenessen.wordpress.com/
Freiburg im Breisgau|Urbanes Gärtnern Freiburg|https://urbanes-gaertnern-freiburg.de
Göttingen|Gartennetzwerk Göttinger Land|https://goettinger-land-gaerten.de/
Hamburg|Hamburgs Gärten|https://hamburgsgaerten.de/
Hannover|Gartenkarte Hannover|http://www.isghannover.de/gartenkarte-hannover/
Köln|Gemeinschaftsgärten Köln|https://gemeinschaftsgaerten-koeln.de/
Köln|Essbare Stadt Köln|https://essbare-stadt.koeln/im-veedel/
Leipzig|Netzwerk Leipziger Gemeinschaftsgärten|https://nelge.de/
München|Urbane Gärten München|http://urbane-gaerten-muenchen.de/
Nürnberg|Essbare Stadt Nürnberg|https://essbare-stadt-nuernberg.de/
Nürnberg|Urbane Gärten Nürnberg und Fürth|https://www.nuernberg.de/internet/agenda21/urban_gardening.html
Fürth|Urbane Gärten Nürnberg und Fürth|https://www.nuernberg.de/internet/agenda21/urban_gardening.html
Wuppertal|Wuppertals urbane Gärten|https://www.wuppertals-urbane-gaerten.de/newsletter-archiv/"""

# DAV-Sektionen (alpenverein.de Überblick; Links aus eigener Recherche)
DAV = """Augsburg|DAV Sektion Augsburg|https://www.dav-augsburg.de/
Berlin|DAV Sektion Berlin|https://www.alpenverein.de/
Darmstadt|DAV Sektion Darmstadt-Starkenburg|https://www.alpenverein.de/
Erlangen|DAV Sektion Erlangen|https://www.alpenverein-erlangen.de/
Frankfurt am Main|DAV Sektion Frankfurt am Main|https://www.alpenverein.de/
Hannover|DAV Sektion Hannover|https://www.alpenverein-hannover.de/
Heidelberg|DAV Sektion Heidelberg|https://www.alpenverein.de/
Karlsruhe|DAV Sektion Karlsruhe|https://www.alpenverein.de/
Leipzig|DAV Sektion Leipzig|https://www.alpenverein.de/
Nürnberg|DAV Sektion Nürnberg|https://www.alpenverein.de/
Pforzheim|DAV Sektion Pforzheim|https://www.alpenverein.de/
Regensburg|DAV Sektion Regensburg|https://www.alpenverein.de/
Reutlingen|DAV Sektion Reutlingen|https://www.alpenverein.de/
Stuttgart|DAV Sektion Schwaben|https://www.alpenverein.de/"""

# Repair Cafés (Treffer der Websuche, Quelle je Eintrag verlinkt)
REPAIR = """Bergisch Gladbach|Reparatur-Café GL|https://www.reparatur-initiativen.de/reparatur-cafe-gl65647
Bergisch Gladbach|Repair-Café Bensberg|https://www.reparatur-initiativen.de/repair-cafe-bensberg
Bergisch Gladbach|Reparatur Café GL Refrath|https://www.reparatur-initiativen.de/reparatur-cafe-gl-refrath
Oberhausen|Repair Café Oberhausen|https://www.lokalkompass.de/oberhausen/c-vereine-ehrenamt/repair-caf-oberhausen_a875849
Oberhausen|Repair Café der Lebenshilfe Oberhausen|https://www.oberhausen-aktuell.de/Veranstaltung/repair-cafe-des-lebenshilfe-e-v/
Mülheim an der Ruhr|Repair Café MH|http://www.repaircafe-mh.de/
Mülheim an der Ruhr|Repair Café Netzwerk Broich|https://www.reparatur-initiativen.de/repair-cafe-muelheim-netzwerk-broich
Herne|Repaircafé der Kolpingsfamilie Herne-Zentral|https://www.reparatur-initiativen.de/repaircafe-der-kolpingsfamilie-herne-zentral
Remscheid|Reparaturen-Café Remscheid|https://www.reparatur-initiativen.de/reparaturen-cafe-remscheid
Moers|Repair Café Moers|https://www.reparatur-initiativen.de/repair-cafe-moers
Salzgitter|Repair-Café Salzgitter-Bad|https://www.wirhelfenkindern.eu/neuigkeiten/details/repair-cafe-salzgitter-ba
Solingen|Reparaturcafé Solingen e.V.|https://www.reparatur-initiativen.de/reparaturcafe-solingen-e-v
Neuss|Reparatur Café Neuss|https://www.reparatur-initiativen.de/reparatur-cafe-neuss
Neuss|Repair Café Transition Town Neuss|https://transitiontown-neuss.de/was-wir-machen/repair-cafe/
Gelsenkirchen|Reparatur Café im Alfred-Zingler-Haus|https://www.reparatur-initiativen.de/reparatur-cafe-im-alfred-zingler-haus
Offenbach am Main|Repair Café und Reparaturtreff im W58|https://fzof.de/Veranstaltung/repair-cafe-reparaturtreff-im-w58/"""
