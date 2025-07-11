import mariadb
from mariadb import Error



#WILLKOMMEN BEI DER REGISTRIERUNG - SQL ;)




# Verbindung zur Datenbank aufbauen
def create_connection():
    try:
        connection = mariadb.connect(
            host="10.80.0.206",
            user="team03",
            password="V6W92",
            database="team03",
            port=3306
        )
        return connection
    except Error as e:
        print(f"Fehler bei der Verbindung zur MariaDB: {e}")
        return None

# Holt die ID zu einem bestimmten Namen (z. B. "Männlich" → 1)
def get_id_by_name(connection, table, name):
    try:
        cursor = connection.cursor()
        cursor.execute(f"SELECT ID FROM {table} WHERE Name = ?", (name,))
        result = cursor.fetchone()
        return result[0] if result else None
    except mariadb.Error as e:
        print(f"Fehler beim Abrufen der ID aus {table}: {e}")
        return None

# Führt die Registrierung mit ID-Suche durch
def registrieren_ausfuehren(nutzer):
    connection = create_connection()
    if not connection:
        return False

    try:
        cursor = connection.cursor()

        geschlecht_id = nutzer.geschlecht#get_id_by_name(connection, "geschlecht", nutzer.geschlecht)
        land_id = nutzer.land#get_id_by_name(connection, "land", nutzer.land)

        if geschlecht_id is None or land_id is None:
            print("Fehler: Land oder Geschlecht nicht gefunden.")
            return False

        cursor.execute("""
            INSERT INTO benutzer 
            (Vorname, Benutzername, Passwort, E_Mail, Geburtsdatum, Geschlecht_ID, Land_ID, Sprache, Bildnummer)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            nutzer.vorname,
            nutzer.nutzername,
            nutzer.passwort,
            nutzer.email,
            nutzer.geburtsdatum,
            geschlecht_id,
            land_id,
            nutzer.sprache,
            1  # Beispiel-Bildnummer
        ))

        connection.commit()
        print("✅ Registrierung erfolgreich.")
        return True

    except mariadb.Error as e:
        print(f"Registrierungsfehler: {e}")
        return False

    finally:
        connection.close()

# Nutzer anlegen und Funktion aufrufen
# nutzer = Testobjekt()
# rueckgabe = registrieren_ausfuehren(nutzer)
# print("Rückgabe:", rueckgabe)
