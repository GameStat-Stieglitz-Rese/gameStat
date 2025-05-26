import mariadb
from z_Datenuebertragung_SQL import zeige_spieldaten

# 💾 Benutzerobjekt-Klasse zur Datenübernahme
class BenutzerObjekt:
    def __init__(self):
        self.id = None
        self.vorname = None
        self.nutzername = None
        self.email = None
        self.sprache = None
        self.land = None
        self.geschlecht = None
        self.geburtsdatum = None
        self.bildnummer = None

# 🔌 Verbindung zur Datenbank
def create_connection():
    try:
        connection = mariadb.connect(
            host="localhost",#"10.80.0.206",
            user="team03",
            password="V6W92",
            database="team03",
            port=3306
        )
        return connection
    except mariadb.Error as e:
        print(f"Verbindungsfehler: {e}")
        return None

# 🔐 Anmeldung mit Datenübertragung in `nutzer`
def nutzer_anmelden(nutzer):
    benutzername = nutzer.nutzername
    passwort = nutzer.passwort
    connection = create_connection()
    if not connection:
        return False, nutzer  # Rückmeldung: keine DB-Verbindung

    try:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT 
                b.ID, b.Vorname, b.Benutzername, b.E_Mail, s.Name AS Sprache,
                l.Name AS Land, g.Name AS Geschlecht, b.Geburtsdatum, b.Bildnummer
            FROM benutzer b
            JOIN sprache s ON b.Sprache = s.ID
            JOIN land l ON b.Land_ID = l.ID
            JOIN geschlecht g ON b.Geschlecht_ID = g.ID
            WHERE b.Benutzername = ? AND b.Passwort = ?
        """, (benutzername, passwort))

        result = cursor.fetchone()
        if result:
            print(f"✅ Anmeldung erfolgreich. Willkommen, {result[1]}!")

            nutzer.id = result[0]
            nutzer.vorname = result[1]
            nutzer.nutzername = result[2]
            nutzer.email = result[3]
            nutzer.sprache = result[4]
            nutzer.land = result[5]
            nutzer.geschlecht = result[6]
            nutzer.geburtsdatum = result[7]
            nutzer.bildnummer = result[8]

            return 0, nutzer  # ✅ Erfolg
        else:
            print("❌ Benutzername oder Passwort ist falsch.")
            return 1, nutzer  # ❌ Login fehlgeschlagen

    except mariadb.Error as e:
        print(f"Fehler bei der Anmeldung: {e}")
        return 2, nutzer  # ❌ DB-Fehler

    finally:
        connection.close()


# ▶️ Hauptprogramm (Test)
if __name__ == "__main__":
    class DummyNutzer(BenutzerObjekt):
        def __init__(self):
            super().__init__()
            self.nutzername = input("Benutzername: ")
            self.passwort = input("Passwort: ")

    nutzer = DummyNutzer()
    nutzer = nutzer_anmelden(nutzer)

    if nutzer:
        print("\n📋 Benutzerprofil:")
        print("Vorname:", nutzer.vorname)
        print("Benutzername:", nutzer.nutzername)
        print("E-Mail:", nutzer.email)
        print("Sprache:", nutzer.sprache)
        print("Land:", nutzer.land)
        print("Geschlecht:", nutzer.geschlecht)
        print("Geburtsdatum:", nutzer.geburtsdatum)
        print("Bildnummer:", nutzer.bildnummer)

        # 🎮 Spieldaten anzeigen
        zeige_spieldaten(nutzer.id)
