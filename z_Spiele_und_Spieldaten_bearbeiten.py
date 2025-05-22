import mariadb

# 📡 Verbindung
def create_connection():
    try:
        return mariadb.connect(
            host="localhost",
            user="team03",
            password="V6W92",
            database="team03",
            port=3306
        )
    except mariadb.Error as e:
        print(f"Verbindungsfehler: {e}")
        return None

# 🔍 Alle Spiele und Plattformen ausgeben
def spiele_und_plattformen_anzeigen():
    connection = create_connection()
    if not connection:
        return [], []

    try:
        cursor = connection.cursor()
        cursor.execute("SELECT ID, Spielname FROM spiele")
        spiele = cursor.fetchall()

        cursor.execute("SELECT ID, Name FROM platform")
        plattformen = cursor.fetchall()

        return spiele, plattformen

    except mariadb.Error as e:
        print(f"Fehler beim Laden der Listen: {e}")
        return [], []

    finally:
        connection.close()

# ➕ Spieldaten anlegen
def spieldaten_anlegen(nutzer_id):
    spiele, plattformen = spiele_und_plattformen_anzeigen()

    print("\n🎮 Spiel auswählen:")
    for s in spiele:
        print(f"{s[0]} - {s[1]}")
    spiel_id = int(input("Spiel-ID: "))

    print("\n🖥️ Plattform auswählen:")
    for p in plattformen:
        print(f"{p[0]} - {p[1]}")
    plattform_id = int(input("Plattform-ID: "))

    level = int(input("Level: "))
    spielzeit = float(input("Spielzeit in Stunden: "))
    bewertung = int(input("Bewertung (1–10): "))
    startdatum = input("Startdatum (YYYY-MM-DD): ")
    durchgespielt = input("Durchgespielt am (YYYY-MM-DD, leer lassen = nicht): ") or None
    empfohlen = int(input("Empfohlen? (1 = ja, 0 = nein): "))

    connection = create_connection()
    if not connection:
        return

    try:
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO spieldaten 
            (Spiel_ID, Benutzer_ID, Plattform_ID, Level, Spielzeit, Eigenbewertung, Startdatum, Durchgespielt, Empfohlen)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (spiel_id, nutzer_id, plattform_id, level, spielzeit, bewertung, startdatum, durchgespielt, empfohlen))
        connection.commit()
        print("✅ Spieldaten gespeichert.")

    except mariadb.Error as e:
        print(f"Fehler beim Speichern: {e}")
    finally:
        connection.close()

# 🛠️ Spieldaten bearbeiten
def spieldaten_bearbeiten(nutzer_id):
    connection = create_connection()
    if not connection:
        return

    try:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT spieldaten.ID, spiele.Spielname, platform.Name
            FROM spieldaten
            JOIN spiele ON spieldaten.Spiel_ID = spiele.ID
            JOIN platform ON spieldaten.Platform_ID = platform.ID
            WHERE spieldaten.Benutzer_ID = ?
        """, (nutzer_id,))
        daten = cursor.fetchall()

        if not daten:
            print("⚠️ Keine Spieldaten vorhanden.")
            return

        print("\n📝 Deine gespeicherten Spieldaten:")
        for d in daten:
            print(f"{d[0]} - Spiel: {d[1]}, Plattform: {d[2]}")

        eintrag_id = int(input("Welche ID willst du bearbeiten? "))

        level = int(input("Neues Level: "))
        spielzeit = float(input("Neue Spielzeit: "))
        bewertung = int(input("Neue Bewertung: "))
        empfohlen = int(input("Empfohlen? (1 = ja, 0 = nein): "))

        cursor.execute("""
            UPDATE spieldaten
            SET Level = ?, Spielzeit = ?, Eigenbewertung = ?, Empfohlen = ?
            WHERE ID = ? AND Benutzer_ID = ?
        """, (level, spielzeit, bewertung, empfohlen, eintrag_id, nutzer_id))
        connection.commit()
        print("✅ Spieldaten aktualisiert.")

    except mariadb.Error as e:
        print(f"Fehler beim Bearbeiten: {e}")
    finally:
        connection.close()

# ▶️ Hauptmenü
if __name__ == "__main__":
    nutzer_id = int(input("Deine Benutzer-ID: "))

    while True:
        print("\n📌 Menü:")
        print("1 - Spieldaten anlegen")
        print("2 - Spieldaten bearbeiten")
        print("0 - Beenden")
        wahl = input("Auswahl: ")

        if wahl == "1":
            spieldaten_anlegen(nutzer_id)
        elif wahl == "2":
            spieldaten_bearbeiten(nutzer_id)
        elif wahl == "0":
            break
        else:
            print("❌ Ungültige Eingabe.")
