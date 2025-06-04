import mariadb


def umwandeln(liste):
    if liste.durchgespielt == 0:
        liste.durchgespielt = "K.A."
    elif liste.durchgespielt == 1:
        liste.durchgespielt = "Nein"
    elif liste.durchgespielt == 2:
        liste.durchgespielt = "Ja"
    else:
        liste.durchgespielt = "E1"

    if liste.empfohlen == 0:
        liste.empfohlen = "K.A."
    elif liste.empfohlen == 1:
        liste.empfohlen = "Nein"
    elif liste.empfohlen == 2:
        liste.empfohlen = "Ja"
        
#GESAMTÜBERSICHT ABRUFEN
def gesamtuebersicht_abrufen(nutzer):
    try:
        connection = mariadb.connect(
            host="10.80.0.206",
            user="team03",
            password="V6W92",
            database="team03",
            port=3306
        )
        cursor = connection.cursor()

        cursor.execute("""
            SELECT 
                spiele.Spielname,
                platform.Name,
                spielkategorie.Name,
                spieldaten.Level,
                spieldaten.Spielzeit,
                spieldaten.Eigenbewertung,
                spieldaten.Startdatum,
                spieldaten.Durchgespielt,
                spieldaten.Empfohlen
            FROM spieldaten
            JOIN spiele ON spieldaten.Spiel_ID = spiele.ID
            JOIN platform ON spieldaten.Platform_ID = platform.ID
            JOIN spielkategorie ON spiele.Kategorie_ID = spielkategorie.ID
            WHERE spieldaten.Benutzer_ID = ?
        """, (nutzer.id,))

        return cursor.fetchall()

    except mariadb.Error as e:
        print(f"Fehler bei der Datenabfrage: {e}")
        return []

    finally:
        if connection:
            connection.close()


#SORT-BEWERTUNG-ABRUFEN

def sort_bewertung_abrufen(nutzer):
    try:
        connection = mariadb.connect(
            host="10.80.0.206",
            user="team03",
            password="V6W92",
            database="team03",
            port=3306
        )
        cursor = connection.cursor()

        cursor.execute("""
            SELECT 
                spiele.Spielname,
                platform.Name,
                spielkategorie.Name,
                spieldaten.Level,
                spieldaten.Spielzeit,
                spieldaten.Eigenbewertung,
                spieldaten.Startdatum,
                spieldaten.Durchgespielt,
                spieldaten.Empfohlen
            FROM spieldaten
            JOIN spiele ON spieldaten.Spiel_ID = spiele.ID
            JOIN platform ON spieldaten.Platform_ID = platform.ID
            JOIN spielkategorie ON spiele.Kategorie_ID = spielkategorie.ID
            WHERE spieldaten.Benutzer_ID = ?
            ORDER BY spieldaten.Eigenbewertung ASC
        """, (nutzer.id,))

        return cursor.fetchall()

    except mariadb.Error as e:
        print(f"Fehler beim Abrufen der Bewertungen: {e}")
        return []

    finally:
        if connection:
            connection.close()


#DURCHGESPIELT ABRUFEN
def durchgespielt_abrufen(nutzer):
    try:
        connection = mariadb.connect(
            host="10.80.0.206",
            user="team03",
            password="V6W92",
            database="team03",
            port=3306
        )
        cursor = connection.cursor()

        cursor.execute("""
            SELECT 
                spiele.Spielname,
                platform.Name,
                spielkategorie.Name,
                spieldaten.Level,
                spieldaten.Spielzeit,
                spieldaten.Eigenbewertung,
                spieldaten.Startdatum,
                spieldaten.Durchgespielt,
                spieldaten.Empfohlen
            FROM spieldaten
            JOIN spiele ON spieldaten.Spiel_ID = spiele.ID
            JOIN platform ON spieldaten.Platform_ID = platform.ID
            JOIN spielkategorie ON spiele.Kategorie_ID = spielkategorie.ID
            WHERE spieldaten.Benutzer_ID = ? AND spieldaten.Durchgespielt = 1
        """, (nutzer.id,))

        return cursor.fetchall()

    except mariadb.Error as e:
        print(f"Fehler beim Abrufen durchgespielter Spiele: {e}")
        return []

    finally:
        if connection:
            connection.close()


#EMPFOHLEN ABRUFEN
def empfohlen_abrufen(nutzer):
    try:
        connection = mariadb.connect(
            host="10.80.0.206",
            user="team03",
            password="V6W92",
            database="team03",
            port=3306
        )
        cursor = connection.cursor()

        cursor.execute("""
            SELECT 
                spiele.Spielname,
                platform.Name,
                spielkategorie.Name,
                spieldaten.Level,
                spieldaten.Spielzeit,
                spieldaten.Eigenbewertung,
                spieldaten.Startdatum,
                spieldaten.Durchgespielt,
                spieldaten.Empfohlen
            FROM spieldaten
            JOIN spiele ON spieldaten.Spiel_ID = spiele.ID
            JOIN platform ON spieldaten.Platform_ID = platform.ID
            JOIN spielkategorie ON spiele.Kategorie_ID = spielkategorie.ID
            WHERE spieldaten.Benutzer_ID = ? AND spieldaten.Empfohlen = 1
        """, (nutzer.id,))

        return cursor.fetchall()

    except mariadb.Error as e:
        print(f"Fehler beim Abrufen empfohlener Spiele: {e}")
        return []

    finally:
        if connection:
            connection.close()