import mariadb
from z_Datenuebertragung_SQL import zeige_spieldaten

# 💾 Benutzerobjekt-Klasse zur Datenübernahme
class BenutzerObjekt:
    def __init__(self, id, vorname, benutzername, email, sprache, land, geschlecht, geburtsdatum, bildnummer):
        self.id = id
        self.vorname = vorname
        self.benutzername = benutzername
        self.email = email
        self.sprache = sprache
        self.land = land
        self.geschlecht = geschlecht
        self.geburtsdatum = geburtsdatum
        self.bildnummer = bildnummer

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
        print(f"Verbindungsfehler: {e}")
        return None

# 🔐 Anmeldung mit Rückgabe eines BenutzerObjekts
def nutzer_anmelden(benutzername, passwort):
    connection = create_connection()
    if not connection:
        return None

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
            return BenutzerObjekt(*result)
        else:
            print("❌ Benutzername oder Passwort ist falsch.")
            return None

    except mariadb.Error as e:
        print(f"Fehler bei der Anmeldung: {e}")
        return None

    finally:
        connection.close()

# ▶️ Hauptprogramm
if __name__ == "__main__":
    benutzername = input("Benutzername: ")
    passwort = input("Passwort: ")

    nutzer = nutzer_anmelden(benutzername, passwort)

    if nutzer:
        # 🧾 Profil anzeigen
        print("\n📋 Benutzerprofil:")
        print("Vorname:", nutzer.vorname)
        print("Benutzername:", nutzer.benutzername)
        print("E-Mail:", nutzer.email)
        print("Sprache:", nutzer.sprache)
        print("Land:", nutzer.land)
        print("Geschlecht:", nutzer.geschlecht)
        print("Geburtsdatum:", nutzer.geburtsdatum)
        print("Bildnummer:", nutzer.bildnummer)

        # 🎮 Spieldaten anzeigen
        zeige_spieldaten(nutzer.id)
