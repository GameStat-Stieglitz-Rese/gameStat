import mariadb

# 👤 Klasse mit allen Benutzerdaten
class Nutzer:
    def __init__(self):
        self.nutzername = "Lester"
        self.passwort = "1234"
        self.vorname = None
        self.email = None
        self.land = None
        self.sprache = None
        self.geschlecht = None
        self.geburtsdatum = None

# 🔌 Verbindung zur Datenbank
def create_connection():
    try:
        connection = mariadb.connect(
            host="localhost",
            user="team03",
            password="V6W92",
            database="team03",
            port=3306
        )
        return connection
    except mariadb.Error as e:
        print(f"❌ Verbindungsfehler: {e}")
        return None

# 🔐 Login prüfen & Objekt mit Daten füllen
def nutzer_anmelden(nutzer):
    connection = create_connection()
    if not connection:
        return False

    try:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT 
                b.Vorname, b.E_Mail, b.Geburtsdatum,
                l.Name AS Land,
                s.Name AS Sprache,
                g.Name AS Geschlecht
            FROM benutzer b
            JOIN land l ON b.Land_ID = l.ID
            JOIN sprache s ON b.Sprache = s.ID
            JOIN geschlecht g ON b.Geschlecht_ID = g.ID
            WHERE b.Benutzername = ? AND b.Passwort = ?
        """, (nutzer.nutzername, nutzer.passwort))

        result = cursor.fetchone()
        if result:
            # ✅ Daten ins Objekt schreiben
            nutzer.vorname = result[0]
            nutzer.email = result[1]
            nutzer.geburtsdatum = result[2]
            nutzer.land = result[3]
            nutzer.sprache = result[4]
            nutzer.geschlecht = result[5]
            print(f"✅ Anmeldung erfolgreich. Willkommen, {nutzer.vorname}!")
            return True
        else:
            print("❌ Benutzername oder Passwort ist falsch.")
            return False

    except mariadb.Error as e:
        print(f"❌ Fehler bei der Anmeldung: {e}")
        return False

    finally:
        connection.close()

# ▶️ Hauptprogramm
if __name__ == "__main__":
    nutzer = Nutzer()  # erstellt Objekt mit Standarddaten

    if nutzer_anmelden(nutzer):
        print("\n📋 Benutzerprofil:")
        print("Vorname:", nutzer.vorname)
        print("Benutzername:", nutzer.nutzername)
        print("E-Mail:", nutzer.email)
        print("Sprache:", nutzer.sprache)
        print("Land:", nutzer.land)
        print("Geschlecht:", nutzer.geschlecht)
        print("Geburtsdatum:", nutzer.geburtsdatum)
