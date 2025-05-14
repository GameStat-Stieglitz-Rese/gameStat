import mariadb
from mariadb import Error

class Testobjekt:
    def __init__(self):
        self.nutzername = None
        self.passwort = None
        self.vorname = None
        self.email = None
        self.land = None
        self.sprache = None
        self.geschlecht = None
        self.geburtsdatum = None

def create_connection():
    try:
        connection = mariadb.connect(
            host="172.0.0.1",  # oder Server-IP
            user="admin",
            password="MaximMarc1324",
            database="gamestat version2",
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
            INSERT INTO users 
            (username, password_hash, email, geburtsdatum, geschlecht, land, sprache)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            nutzer.nutzername,
            #generate_password_hash(nutzer.passwort),
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

nutzer = Testobjekt()
rueckgabe = registrieren_ausfuehren(nutzer)
print(rueckgabe)