import mariadb
 
def verbinden():
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
        print(f"Fehler beim Verbinden zur MariaDB: {e}")
        return None
 
def hinzufuegen(spieldaten):
    try:
        verbindung = verbinden()
        if verbindung is None:
            return 1  # Verbindungsfehler
 
        cursor = verbindung.cursor()
 
        # Prüfung auf vorhandenen Eintrag
        sql_check = """
            SELECT COUNT(*) FROM spieldaten
            WHERE benutzerid = ? AND spielid = ? AND plattformid = ? AND kategorieid = ?
        """
        daten = (spieldaten.benutzerid, spieldaten.spielid, spieldaten.plattformid, spieldaten.kategorieid)
        cursor.execute(sql_check, daten)
        vorhanden = cursor.fetchone()[0]
 
        if vorhanden > 0:
            return 2  # Eintrag bereits vorhanden
 
        sql_insert = """
            INSERT INTO spieldaten
            (benutzerid, spielid, plattformid, kategorieid, level, spielzeit, bewertung, startdatum, durchgespielt, empfohlen)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        werte = (
            spieldaten.benutzerid,
            spieldaten.spielid,
            spieldaten.plattformid,
            spieldaten.kategorieid,
            spieldaten.level,
            spieldaten.spielzeit,
            spieldaten.bewertung,
            spieldaten.startdatum,
            spieldaten.durchgespielt,
            spieldaten.empfohlen
        )
 
        cursor.execute(sql_insert, werte)
        verbindung.commit()
        return 0  # Erfolg
 
    except mariadb.Error as e:
        print(f"Fehler beim Einfügen: {e}")
        return 1  # Allgemeiner Fehler
    finally:
        if verbindung:
            cursor.close()
            verbindung.close()
 
def spiel_bearbeiten_speichern(spieldaten):
    try:
        verbindung = verbinden()
        if verbindung is None:
            return False
 
        cursor = verbindung.cursor()
 
        sql_update = """
            UPDATE spieldaten
            SET level = ?,
                spielzeit = ?,
                bewertung = ?,
                startdatum = ?,
                durchgespielt = ?,
                empfohlen = ?
            WHERE id = ?
        """
        werte = (
            spieldaten.level,
            spieldaten.spielzeit,
            spieldaten.bewertung,
            spieldaten.startdatum,
            spieldaten.durchgespielt,
            spieldaten.empfohlen,
            spieldaten.eintragid
        )
 
        cursor.execute(sql_update, werte)
        verbindung.commit()
        return True
 
    except mariadb.Error as e:
        print(f"Fehler beim Bearbeiten: {e}")
        return False
    finally:
        if verbindung:
            cursor.close()
            verbindung.close()
 