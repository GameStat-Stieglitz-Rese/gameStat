import mariadb

# 🔁 Hilfsfunktion zum Umwandeln von 1/2/3 in Text

def konvertiere_booleans(eintraege):
    def ja_nein(wert):
        if wert == 1:
            return "Ja"
        elif wert == 2:
            return "Nein"
        else:
            return "K.A."
        
    def check_none(wert):
        if wert == None:
            return "K.A."
        else:
            return wert

    return [
        (
            eintrag[0],  # ID
            eintrag[1],  # Spielname
            eintrag[2],  # Plattform
            eintrag[3],  # Kategorie
            check_none(eintrag[4]),  # Level
            eintrag[5],  # Spielzeit
            eintrag[6],  # Eigenbewertung
            check_none(eintrag[7]),  # Startdatum
            ja_nein(eintrag[8]),  # Durchgespielt
            ja_nein(eintrag[9]),  # Empfohlen
            eintrag[10]  # Herausgeber
        )
        for eintrag in eintraege
    ]

# 🔎 Gesamtliste aller Spiele des Nutzers
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
                spieldaten.ID,
                spiele.Spielname,
                platform.Name,
                spielkategorie.Name,
                spieldaten.Level,
                spieldaten.Spielzeit,
                spieldaten.Eigenbewertung,
                spieldaten.Startdatum,
                spieldaten.Durchgespielt,
                spieldaten.Empfohlen,
                herausgeber.Name
            FROM spieldaten
            JOIN spiele ON spieldaten.Spiel_ID = spiele.ID
            JOIN platform ON spieldaten.Platform_ID = platform.ID
            JOIN spielkategorie ON spiele.Kategorie_ID = spielkategorie.ID
            JOIN herausgeber ON spiele.Herausgeber_ID = herausgeber.ID
            WHERE spieldaten.Benutzer_ID = ?
        """, (nutzer.id,))

        return konvertiere_booleans(cursor.fetchall())

    except mariadb.Error as e:
        print(f"Fehler bei der Datenabfrage: {e}")
        return []

    finally:
        if 'connection' in locals():
            connection.close()

# 🔎 Nach Bewertung sortiert
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
                spieldaten.ID,
                spiele.Spielname,
                platform.Name,
                spielkategorie.Name,
                spieldaten.Level,
                spieldaten.Spielzeit,
                spieldaten.Eigenbewertung,
                spieldaten.Startdatum,
                spieldaten.Durchgespielt,
                spieldaten.Empfohlen,
                herausgeber.Name
            FROM spieldaten
            JOIN spiele ON spieldaten.Spiel_ID = spiele.ID
            JOIN platform ON spieldaten.Platform_ID = platform.ID
            JOIN spielkategorie ON spiele.Kategorie_ID = spielkategorie.ID
            JOIN herausgeber ON spiele.Herausgeber_ID = herausgeber.ID
            WHERE spieldaten.Benutzer_ID = ?
            ORDER BY spieldaten.Eigenbewertung ASC
        """, (nutzer.id,))

        return konvertiere_booleans(cursor.fetchall())

    except mariadb.Error as e:
        print(f"Fehler beim Abrufen der Bewertungen: {e}")
        return []

    finally:
        if 'connection' in locals():
            connection.close()

# 🔎 Nur durchgespielte
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
                spieldaten.ID,
                spiele.Spielname,
                platform.Name,
                spielkategorie.Name,
                spieldaten.Level,
                spieldaten.Spielzeit,
                spieldaten.Eigenbewertung,
                spieldaten.Startdatum,
                spieldaten.Durchgespielt,
                spieldaten.Empfohlen,
                herausgeber.Name
            FROM spieldaten
            JOIN spiele ON spieldaten.Spiel_ID = spiele.ID
            JOIN platform ON spieldaten.Platform_ID = platform.ID
            JOIN spielkategorie ON spiele.Kategorie_ID = spielkategorie.ID
            JOIN herausgeber ON spiele.Herausgeber_ID = herausgeber.ID
            WHERE spieldaten.Benutzer_ID = ? AND spieldaten.Durchgespielt = 1
        """, (nutzer.id,))

        return konvertiere_booleans(cursor.fetchall())

    except mariadb.Error as e:
        print(f"Fehler beim Abrufen durchgespielter Spiele: {e}")
        return []

    finally:
        if 'connection' in locals():
            connection.close()

# 🔎 Nur empfohlene
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
                spieldaten.ID,
                spiele.Spielname,
                platform.Name,
                spielkategorie.Name,
                spieldaten.Level,
                spieldaten.Spielzeit,
                spieldaten.Eigenbewertung,
                spieldaten.Startdatum,
                spieldaten.Durchgespielt,
                spieldaten.Empfohlen,
                herausgeber.Name
            FROM spieldaten
            JOIN spiele ON spieldaten.Spiel_ID = spiele.ID
            JOIN platform ON spieldaten.Platform_ID = platform.ID
            JOIN spielkategorie ON spiele.Kategorie_ID = spielkategorie.ID
            JOIN herausgeber ON spiele.Herausgeber_ID = herausgeber.ID
            WHERE spieldaten.Benutzer_ID = ? AND spieldaten.Empfohlen = 1
        """, (nutzer.id,))

        return konvertiere_booleans(cursor.fetchall())

    except mariadb.Error as e:
        print(f"Fehler beim Abrufen empfohlener Spiele: {e}")
        return []

    finally:
        if 'connection' in locals():
            connection.close()
