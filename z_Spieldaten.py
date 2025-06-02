import mariadb
from tkinter import ttk
from tkinter import messagebox

# ===================== #
#   DB-Verbindung       #
# ===================== #
def verbinden():
    try:
        connection = mariadb.connect(
            host="10.80.0.206",
            user="team03",
            password="V6W92",
            database="team03",
            port=3306
        )
        return connection
    except mariadb.Error as e:
        print(f"Fehler beim Verbinden zur MariaDB: {e}")
        return None

# ===================== #
#   Spiel anlegen       #
# ===================== #
def hinzufuegen(spieldaten):
    try:
        verbindung = verbinden()
        if verbindung is None:
            return 1  # Verbindungsfehler

        cursor = verbindung.cursor()

        #print(spieldaten.benutzerid)

        sql_check = """
            SELECT COUNT(*) FROM spieldaten
            WHERE Benutzer_ID = ? AND Spiel_ID = ? AND Platform_ID = ?
        """
        daten = (spieldaten.benutzerid, spieldaten.spielid, spieldaten.plattformid)
        cursor.execute(sql_check, daten)
        vorhanden = cursor.fetchone()[0]

        #print(spieldaten.benutzerid)

        if vorhanden > 0:
            return 2  # Eintrag bereits vorhanden

        sql_insert = """
            INSERT INTO spieldaten
            (Benutzer_ID, Spiel_ID, Platform_ID, Level, Spielzeit, Eigenbewertung, Startdatum, Durchgespielt, Empfohlen)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        werte = (
            spieldaten.benutzerid,
            spieldaten.spielid,
            spieldaten.plattformid,
            spieldaten.level,
            spieldaten.spielzeit,
            spieldaten.bewertung,
            spieldaten.startdatum,
            spieldaten.durchgespielt,
            spieldaten.empfohlen
        )
        #rint(spieldaten.benutzerid)

        cursor.execute(sql_insert, werte)
        verbindung.commit()
        return 0  # Erfolg

    except mariadb.Error as e:
        print(f"Fehler beim Einfügen: {e}")
        return 1
    finally:
        if verbindung:
            cursor.close()
            verbindung.close()

# ===================== #
#   Spiel bearbeiten    #
# ===================== #
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

# ===================== #
#   Spiele anzeigen     #
# ===================== #
def spiele_liste_fuer_bearbeitung(nutzer_id):
    try:
        verbindung = verbinden()
        if verbindung is None:
            return [], False

        cursor = verbindung.cursor()
        cursor.execute("""
            SELECT spieldaten.ID, spiele.Spielname, platform.Name
            FROM spieldaten
            JOIN spiele ON spieldaten.spielid = spiele.ID
            JOIN platform ON spieldaten.plattformid = platform.ID
            WHERE spieldaten.benutzerid = ?
        """, (nutzer_id,))

        daten = cursor.fetchall()
        if not daten:
            return [], False

        spielliste = [f"{row[0]} - {row[1]} ({row[2]})" for row in daten]
        return spielliste, True

    except mariadb.Error as e:
        print(f"Fehler beim Laden der Spieleliste: {e}")
        return [], False
    finally:
        if verbindung:
            cursor.close()
            verbindung.close()

# ===================== #
#   TEST-FENSTER START  #
# ===================== #
if __name__ == "__main__":
    import tkinter as tk
    from tkinter import ttk, messagebox

    class DummyNutzer:
        def __init__(self):
            self.id = 2

    nutzer = DummyNutzer()

    root = tk.Tk()
    root.title("Spieldaten bearbeiten")
    root.geometry("800x600")

    spielliste, erfolg = spiele_liste_fuer_bearbeitung(nutzer.id)

    if erfolg:
        cb_spielname = ttk.Combobox(root, values=spielliste, state="readonly")
        cb_spielname.place(x=500, y=150)
    else:
        messagebox.showerror("Fehler", "Konnte Spieleliste nicht laden.")

    root.mainloop()
