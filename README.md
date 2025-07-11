# GameStat

**GameStat** ist eine Desktop-Anwendung zur Erfassung, Verwaltung und Auswertung von Spieldaten. Die Software wurde mit Python und dem GUI-Toolkit **Tkinter** unter Verwendung des **Azure-Themes** entwickelt. Der Fokus liegt auf Benutzerfreundlichkeit, einfacher Bedienung und einem übersichtlichen Design.

## 📦 Funktionen

- Spielstände und Spieldetails erfassen  
- Spieler-Statistiken verwalten und auswerten  
- Tabellenansicht mit Such- und Sortierfunktionen  
- Export- und Druckoptionen für Auswertungen  
- Anpassbares Design durch Themes

## 🧠 Technologien

- Programmiersprache: Python 3.12  
- GUI: Tkinter + Azure-Theme  
- Exe-Erstellung: PyInstaller

## 🛠️ Kompilierung

Das Projekt kann mit folgendem Befehl in eine `.exe` kompiliert werden:

```bash
pyinstaller --onefile --noconsole --add-data "images;images" --add-data "themes;themes" main.py
```

## 👥 Projektarbeit

Dieses Projekt wurde im Rahmen einer **Partnerarbeit** an der Rudolf-Diesel-Fachschule Nürnberg durchgeführt. Ziel war es, ein vollständiges Softwareprojekt von der Konzeption über die Umsetzung bis hin zur Dokumentation im Team zu realisieren.

## 🧍 Projektteam

- Marc Stieglitz, Wirtschaftsinformatik
- Maxim Rese, Wirtschaftsinformatik

## 📁 Ordnerstruktur

```
GameStat/
├── images/         # Icons und Grafiken
├── themes/         # Azure-Theme Dateien
├── main.py         # Hauptprogramm
├── README.md       # Dieses Dokument
└── dist/           # Kompilierte .exe-Datei nach Build
```

## 📌 Hinweise

- Das Projekt ist für Windows entwickelt worden  
- Für die Ausführung ist keine Python-Installation notwendig, sobald die `.exe` gebaut ist  
- Der Build-Ordner kann nach dem Kompilieren gelöscht werden

---

Mit **GameStat** liefern wir ein einfaches, aber funktionales Tool zur Organisation von Spieldaten. Ideal für kleine Turniere, Gaming-Events oder einfach zum Spaß.
