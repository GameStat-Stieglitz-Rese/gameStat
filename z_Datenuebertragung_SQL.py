import mariadb

# Verbindung zur Datenbank
def create_connection():
    return mariadb.connect(
        host="localhost",
        user="team03",
        password="V6W92",
        database="team03",
        port=3306
    )

def zeige_spieldaten(benutzer_id):
    try:
        connection = create_connection()
        cursor = connection.cursor()

        # 🧠 Vorname des Benutzers abfragen
        cursor.execute("SELECT Vorname FROM benutzer WHERE ID = ?", (benutzer_id,))
        benutzer = cursor.fetchone()
        vorname = benutzer[0] if benutzer else "Unbekannt"

        # 🎮 Spieldaten abfragen
        cursor.execute("""
            SELECT spiele.Spielname, platform.Name, spieldaten.Level, spieldaten.Spielzeit, spieldaten.Eigenbewertung
            FROM spieldaten
            JOIN spiele ON spieldaten.Spiel_ID = spiele.ID
            JOIN platform ON spieldaten.Platform_ID = platform.ID
            WHERE spieldaten.Benutzer_ID = ?
        """, (benutzer_id,))

        daten = cursor.fetchall()

        print(f"\n🎮 Spieldaten für {vorname}")  # ← zeigt den Namen statt ID
        #print("Rohdaten:", daten)  # ← kannst du später entfernen

        if daten:
            for eintrag in daten:
                print(f"- Spiel: {eintrag[0]}, Plattform: {eintrag[1]}, Level: {eintrag[2]}, Spielzeit: {eintrag[3]} Std., Bewertung: {eintrag[4]}/10")
        else:
            print("ℹ️ Keine Spieldaten gefunden.")

    except mariadb.Error as e:
        print(f"Fehler beim Abrufen der Spieldaten: {e}")

    finally:
        connection.close()
