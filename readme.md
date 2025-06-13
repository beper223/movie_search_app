# 📘 Filmsuchsystem

## 🖥️ Allgemeine Beschreibung

Dieses Programm ist eine Konsolenanwendung zur Filmsuche. Es bietet dem Benutzer die Möglichkeit, Filme zu suchen nach:

- Stichwörtern,
- Genres,
- Schauspielern,
- Erscheinungsjahren

sowie die **beliebtesten Suchanfragen** einzusehen.

---

## 🔧 Programmstart

Das Programm wird mit folgendem Befehl gestartet:

```
python main.py
```

Möglicherweise muss vor dem Start das virtuelle Environment aktiviert werden:

```
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
.venv\Scripts\activate
```

Nach dem Start erscheint im Terminal die Eingabeaufforderung:

```
Geben Sie einen Befehl ein (m — Menü, q — Beenden):
```

---

## 📜 Verfügbare Befehle

Um alle verfügbaren Befehle anzuzeigen, geben Sie ein:

```
m
```

Dann erscheint eine Liste:

```
Verfügbare Befehle:
  search keyword <Wort> — Suche nach einem Stichwort im Filmtitel
  search genre — Suche nach Genre
  search actor <Name des Schauspielers> — Suche nach Schauspieler
  search year <Jahr> — Suche nach Erscheinungsjahr
  p — beliebteste Suchanfragen
  q — Beenden
```

---

## 🔍 Filmsuche

### 🔑 Suche nach Stichwort

```
search keyword <Wort>
```

**Beispiel:**
```
search keyword matrix
```

Zeigt alle Filme an, in deren Titel „matrix“ vorkommt.

---

### 🎭 Suche nach Genre

```
search genre
```

1. Eine Liste der Genres wird angezeigt.
2. Geben Sie die **Nummer des Genres** ein (z. B. `3`), um nach diesem zu filtern.

---

### 🎬 Suche nach Schauspieler

```
search actor <Name des Schauspielers>
```

**Beispiel:**
```
search actor Tom Hanks
```

1. Eine Liste mit passenden Schauspielern wird angezeigt.
2. Wählen Sie den gewünschten Schauspieler durch Eingabe der Nummer.
3. Die Filme mit diesem Schauspieler werden angezeigt.

---

### 📆 Suche nach Jahr

```
search year <Jahr>
```

**Beispiel:**
```
search year 1999
```

Zeigt alle Filme, die im Jahr 1999 erschienen sind.

---

## 📈 Beliebte Suchanfragen

```
popular
```

Zeigt eine Tabelle der beliebtesten Suchanfragen: Typ, Suchtext, Anzahl der Anfragen.

---

## 📄 Navigation in den Ergebnissen

### Beim Durchblättern von Filmen oder Schauspielern:

- `n` — nächste Seite
- `p` — vorherige Seite
- `q` — Liste verlassen (für Filme), Auswahl abbrechen (für Schauspieler)
- `<Nummer>` — gewünschten Schauspieler auswählen

---

## ❌ Programm beenden

Zum Beenden des Programms geben Sie ein:

```
q
```

---

## ⚠️ Mögliche Fehler

- ❗ Leerer Befehl
- ❗ Ungültiges Befehlsformat
- ❗ Ungültige Eingabedaten (z. B. Text statt Zahl)
- ❗ Keine Ergebnisse gefunden

Fehlermeldungen werden farbig mit Erläuterung angezeigt.

---

## 🧩 Installation des Programms

1. Installieren Sie die Pakete aus `requirements.txt`:

```
pip install -r requirements.txt
```

2. Erstellen Sie die Datei `db/local_settings.py` mit folgendem Inhalt:

```python
dbconfig = {'host': 'host_name',
            'user': 'user_name',
            'port': '3306',
            'password': 'pass',
            'database': 'database_name'}
```

---