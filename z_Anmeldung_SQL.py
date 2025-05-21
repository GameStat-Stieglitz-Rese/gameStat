import mariadb
from z_Datenuebertragung_SQL import zeige_spieldaten

# Verbindung zur Datenbank
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

# Anmeldefunktion → gibt Benutzer-ID zurück!
def nutzer_anmelden(benutzername, passwort):
    connection = create_connection()
    if not connection:
        return None

    try:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT ID, Vorname FROM benutzer
            WHERE Benutzername = ? AND Passwort = ?
        """, (benutzername, passwort))

        result = cursor.fetchone()
        if result:
            print(f"✅ Anmeldung erfolgreich. Willkommen, {result[1]}!")
            return result[0]  # Benutzer-ID zurückgeben
        else:
            print("❌ Benutzername oder Passwort ist falsch.")
            return None

    except mariadb.Error as e:
        print(f"Fehler bei der Anmeldung: {e}")
        return None

    finally:
        connection.close()

# Eingabe & Aufruf
if __name__ == "__main__":
    benutzername = input("Benutzername: ")
    passwort = input("Passwort: ")

    benutzer_id = nutzer_anmelden(benutzername, passwort)
    #print("Erfolgreich angemeldet:", benutzer_id) #REIN TECHNISCH UM ZU SEHEN OB ERFOLGREICH ANGEMELDET WURDE

    if benutzer_id:
        zeige_spieldaten(benutzer_id)
