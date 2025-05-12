import mariadb
from mariadb import Error

def create_connection():
    try:
        connection = mariadb.connect(
            host="localhost",  # oder Server-IP
            user="dein_user",
            password="dein_passwort",
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