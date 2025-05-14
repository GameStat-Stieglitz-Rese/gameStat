import mariadb
from mariadb import Error

class Testobjekt:
    def __init__(self):
        self.benutzer = "maxim"
        self.passwort = "1234"
        self.vorname = "Maxim"
        self.email = "maxim@gmail.com"
        self.land = "Deutschland"
        self.sprache = "deutsch"
        self.geschlecht = "Männlich"
        self.geburtsdatum = "1234"

def create_connection():
    try:
        connection = mariadb.connect(
            host="localhost",  # oder Server-IP
            user="MaximMarc",
            password="MaximMarc1312",
            database="gamestat_version2",
            port=3306  # Standard-Port für MariaDB
        )
        return connection
    except Error as e:
        print(f"Fehler bei der Verbindung zur MariaDB: {e}")
        return None
    
def registrieren_ausfuehren(nutzer):
    connection = create_connection()
    if not connection:
        return False
        
    try:
        cursor = connection.cursor()
        cursor.execute("""
        INSERT INTO benutzer 
        (Benutzername, Passwort, E_Mail, Geburtsdatum, Geschlecht_ID, Land_ID, Sprache)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
        nutzer.benutzer,
        nutzer.passwort,
        nutzer.email,
        nutzer.geburtsdatum,
        nutzer.geschlecht,
        nutzer.land,
        nutzer.sprache
        ))
        connection.commit()
        return True
        
    except mariadb.Error as e:
        print(f"Registrierungsfehler: {e}")
        return False
        
    finally:
        connection.close()


#################################

def anmeldung_abrufen(nutzer):
    connection = create_connection()
    if not connection:
        return False
        
    try:
        cursor = connection.cursor()
        cursor.execute("""
        INSERT INTO benutzer 
        (Benutzername, Passwort, E_Mail, Geburtsdatum, Geschlecht_ID, Land_ID, Sprache)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
        nutzer.benutzer,
        nutzer.passwort,
        nutzer.email,
        nutzer.geburtsdatum,
        nutzer.geschlecht,
        nutzer.land,
        nutzer.sprache
        ))
        connection.commit()
        return True
        
    except mariadb.Error as e:
        print(f"Registrierungsfehler: {e}")
        return False
        
    finally:
        connection.close()

#########################################

nutzer = Testobjekt()
rueckgabe = registrieren_ausfuehren(nutzer)
print(rueckgabe)