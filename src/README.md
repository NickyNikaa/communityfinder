# FindeDeineLeute.de, Quellcode

- `data/ext/*.txt`, `data/runclubs_*.txt`, `static_data.py`: Rohdaten (eine Community pro Zeile)
- `build.py`: erzeugt `data/data.json`, ordnet Kategorien zu, übernimmt den Prüfstand aus `data/state.json`
- `refresh.py`: Linkprüfung, läuft alle zwei Wochen per GitHub Action (`.github/workflows/refresh.yml`)
- `gen.py`: erzeugt alle HTML-Seiten, Sitemap und `communities.json`
- Lokal: `python src/build.py && OUT=dist python src/gen.py`

Neue Communities eintragen: Zeile in eine Datei unter `data/ext/` im Format
`Stadt|Name|Kategorie|URL|Beschreibung|Wann|Plattform` ergänzen. Beim nächsten Lauf erscheint sie auf der Seite.
Optional: GitHub-Secrets `REDDIT_CLIENT_ID` und `REDDIT_CLIENT_SECRET` (kostenlose Reddit-App) erlauben die Prüfung der Subreddits.
