# Grafiken neu erzeugen

Alle Bilder in `assets/` entstehen aus diesen Skripten. Texte, Projekte oder Farben
hier ändern, Skript laufen lassen, committen.

| Skript | erzeugt |
| --- | --- |
| `banner.py` | `assets/banner.svg` – Kopfbild mit Leiterbahnen und AprilTag (ID 42) |
| `schreibzeile.py` | `assets/typing.svg` – Schreibmaschinen-Zeile, Liste `lines` oben im Skript |
| `karten.py` | `assets/technik.svg` und `assets/projekt-*.svg` – Listen `reihen` und `projekte` |

```bash
python3 tools/banner.py
python3 tools/schreibzeile.py
npm install simple-icons          # einmalig, liefert die Logos (Lizenz CC0)
python3 tools/karten.py
```

Logos: Name aus https://simpleicons.org (z. B. `raspberrypi`), ohne Logo `None` eintragen.
Farben stehen jeweils oben im Skript (`CYAN`, `BG` …).
