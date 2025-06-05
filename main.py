import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import elemente # Hier sind die Elemente im Fenster (Knöpfe und co. gespeichert)
from functools import partial
import anmeldung
from PIL import Image, ImageTk
import z_Datenuebertragung_SQL
import z_Spieldaten
import check_var
import test_objektTestAnzeige
import z_Abfragen
import os


def main_clearwdw(): # Löscht den gesamten Inhalt eines Fensters!
    for widget in root.winfo_children():
        widget.place_forget()
    button.gen_abmelden()

def uebersicht(nutzer): # Zeigt eine Tabelle mit allen Spielständen / Games an
    label.gen_title("Alle Spielstände")
    liste = z_Abfragen.gesamtuebersicht_abrufen(nutzer) # SQL Befehl, der anhand der Benutzer ID eine Gesamtliste abruft 
    elemente.tbl_spdaten(root, liste)

def bewertungen(nutzer): # Zeigt eine Tabelle mit allen Spielen mit aufsteigender Bewertung an
    label.gen_title("Spielstände sortiert nach Bewertung")
    liste = z_Abfragen.sort_bewertung_abrufen(nutzer) # SQL Befehl, der anhand der Benutzer ID eine Gesamtliste abruft 
    elemente.tbl_spdaten(root, liste)

def durchgespielt(nutzer): # Zeigt eine Tabelle mit allen durchgespielten Spielen an
    label.gen_title("Durchgespielte Spiele")
    liste = z_Abfragen.durchgespielt_abrufen(nutzer) # SQL Befehl, der anhand der Benutzer ID eine Gesamtliste abruft 
    elemente.tbl_spdaten(root, liste)

def empfohlen(nutzer): # Zeigt eine Tabelle mit allen empfohlenen Games an
    label.gen_title("Von dir empfohlene Spiele")
    liste = z_Abfragen.empfohlen_abrufen(nutzer) # SQL Befehl, der anhand der Benutzer ID eine Gesamtliste abruft 
    elemente.tbl_spdaten(root, liste)

def spiel_bearbeiten(): # Bearbeiten vorhandener Spielstände
    def aendern(): # Zeigt nach der Eingabe eines Spiels die Oberfläche zur änderung der Daten an
        def check(): # Speicherung neuer Eingaben (Weiter Button)
            lvl = tf_level.get()
            spz = tf_spielzeit.get()
            bwt = tf_bewertung.get()
            esp = tf_startdatum.get()
            dgw = dg_wahl.get()
            emw = empf_wahl.get()

            # Prüfung, ob die Angaben aus Spiel bearbeiten gültig sind
            if check_var.check_int(lvl, "Level", False) == False:
                print("Fehler Benutzereingabe lvl")
            elif check_var.check_int(spz, "Spielzeit", True) == False:
                print("Fehler Benutzereingabe spz")
            elif check_var.check_range(bwt, 1, 10, "Bewertung", True) == False:
                print("Fehler Benutzereingabe bwt")
            elif check_var.check_datum(esp, "Startdatum", False) == False:
                print("Fehler Benutzereingabe esp")
            elif dgw == 0 or emw == 0:
                messagebox.showerror("Eingabefehler", "Bitte wählen Sie auch aus, ob Sie bereits angefangen und / oder durchgespielt haben.")
            else:
                print("Eingaben korrekt.")

                print(dgw, emw)

                # Konvertierung und speicherung in Objekt
                spdaten.level = int(lvl) if lvl != "" else None
                spdaten.spielzeit = int(spz)
                spdaten.bewertung = int(bwt)
                spdaten.startdatum = esp if esp != "" else None
                spdaten.durchgespielt = dgw
                spdaten.empfohlen = emw

                # Übergabe per SQL Befehl an die Datenbank
                rw2 = z_Spieldaten.spiel_bearbeiten_speichern(spdaten)
                if rw2 == True:
                    messagebox.showinfo("Speicherung", "Die Speicherung war erfolgreich! Sie gelangen nun in das Hauptmenü.")
                    main()
                else:
                    messagebox.showerror("Speicherung", "Leider gab es ein Problem mit der Speicherung der Spieldaten. Bitte versuchen Sie es erneut.")
                    aendern()

        wahl = cb_spielname.get()
        #print(game)
        if wahl != "":
            main_clearwdw()
            spdaten.eintragid = int(wahl[0]) # Eintrag ID ist immer am Anfang des jeweiligen Eintrags und wird hier abgerufen und zu INT umgewandelt
            #print(eintragid)
            #spdaten, rw1 = z_Spieldaten.spieldaten_abrufen(eintragid)
            rw1 = True
            if rw1 == False:
                messagebox.showerror("MariaDB Fehler", "Fehler bei dem Abrufen von Daten. Sie gelangen nun in das Hauptmenü.")
                main()

            button.gen_abmelden()
            button.gen_return()

            xwert = 750
            ywert = 90
            xadd = 150
            yadd = 20

            label.gen_title(f"Bearbeiten von {wahl}")
            pic_background2.place(x=0, y=80, relwidth=1, relheight=1)

            tk.Label(root, text="Level").place(x=xwert, y=ywert)
            ywert += yadd
            tf_level = ttk.Entry(root, text=123)
            tf_level.place(x=xwert, y=ywert)
            ywert += yadd * 2

            tk.Label(root, text="Spielzeit (in Std.) *").place(x=xwert, y=ywert)
            ywert += yadd
            tf_spielzeit = ttk.Entry(root)
            tf_spielzeit.place(x=xwert, y=ywert)
            ywert += yadd * 2
            
            tk.Label(root, text="Eigenbewertung (1-10) *").place(x=xwert, y=ywert)
            ywert += yadd
            tf_bewertung = ttk.Entry(root)
            tf_bewertung.place(x=xwert, y=ywert)
            ywert += yadd * 2
            
            tk.Label(root, text="Erster Spieltag (JJJJ-MM-TT)").place(x=xwert, y=ywert)
            ywert += yadd
            tf_startdatum = ttk.Entry(root)
            tf_startdatum.place(x=xwert, y=ywert)
            ywert += yadd * 3

            xwert -= 30
            tk.Label(root, text="Durchgespielt? *").place(x=xwert, y=ywert)
            ywert += yadd
            dg_wahl = tk.IntVar(value=0)
            ttk.Radiobutton(root, text="Ja", variable=dg_wahl, value=1).place(x=xwert, y=ywert)
            ywert += yadd + 5
            ttk.Radiobutton(root, text="Nein", variable=dg_wahl, value=2).place(x=xwert, y=ywert)
            ywert += yadd + 5
            ttk.Radiobutton(root, text="Nicht Angefangen", variable=dg_wahl, value=3).place(x=xwert, y=ywert)
            ywert -= yadd * 3
            ywert -= 10
            xwert += xadd

            tk.Label(root, text="Empfehlung? *").place(x=xwert, y=ywert)
            ywert += yadd
            empf_wahl = tk.IntVar(value=0)
            ttk.Radiobutton(root, text="Ja", variable=empf_wahl, value=1).place(x=xwert, y=ywert)
            ywert += yadd + 5
            ttk.Radiobutton(root, text="Nein", variable=empf_wahl, value=2).place(x=xwert, y=ywert)
            ywert += yadd + 5
            ttk.Radiobutton(root, text="Keine Angabe", variable=empf_wahl, value=3).place(x=xwert, y=ywert)

            ttk.Button(root, text="Speichern", command=check).place(x=730, y=700, width=200)

        else:
            messagebox.showwarning("Eingabe", "Bitte wählen Sie ein Spiel aus. Sofern nicht vorhanden, bitte anlegen.")

    main_clearwdw()
    spielliste, rw = z_Spieldaten.spiele_liste_fuer_bearbeitung(nutzer.id) # Erstellung einer liste mit allen Spielen und den jeweiligen Plattformen

    if rw == 1:
        messagebox.showerror("MariaDB Fehler", "Es gab einen Fehler bei der Datenübertragung. Sie gelangen zurück zum Hauptmenü.")
        main()
    elif rw == 2:
        messagebox.showerror("Kein Spielstand", "Sie haben noch keine Spielstände angelegt. Bitte legen Sie sich zuvor einen an. Sie gelangen zurück zum Hauptmenü.")
        main()
    else:
        button.gen_return()
        label.gen_title("Spiel bearbeiten")
        xwert = 750
        ywert = 90
        xadd = 150
        yadd = 20

        pic_background2.place(x=0, y=80, relwidth=1, relheight=1)
        tk.Label(root, text="Spielname").place(x=xwert, y=ywert)
        ywert += yadd
        cb_spielname = ttk.Combobox(root, values=spielliste, state="readonly")
        cb_spielname.place(x=xwert, y=ywert)
        ywert += yadd * 2

        ttk.Button(root, text="Weiter", command=aendern).place(x=730, y=700, width=200)

def spiel_hinzufg(): # Hinzufügen neuer Spielstände
    def check():
        dg = dg_wahl.get()
        empf = empf_wahl.get()
        spname = cb_spielname.get()
        pltfrm = cb_plattform.get()
        lvl = tf_level.get()
        spz = tf_spielzeit.get()
        ebw = tf_bewertung.get()
        esp = tf_erstSpieltag.get()

        # Prüfung, ob die nötigen Felder ausgefüllt und die Datentypen eingehalten wurden
        if spname == "" or pltfrm == "":
            messagebox.showinfo("Fehlende Eingabe", "Bitte geben Sie Spielnamen und Plattform ein.")
        elif dg == 0 or empf == 0:
            messagebox.showinfo("Fehlende Eingabe", "Bitte wählen Sie auch aus, ob Sie bereits angefangen und / oder durchgespielt haben.")
        elif check_var.check_int(lvl, "Level", False) == False:
            print("Fehler Benutzereingabe lvl")
        elif check_var.check_int(spz, "Spielzeit", True) == False:
            print("Fehler Benutzereingabe spz")
        elif check_var.check_range(ebw, 1, 10, "Bewertung", True) == False:
            print("Fehler Benutzereingabe bwt")
        elif check_var.check_datum(esp, "Erster Spieltag", False) == False:
            print("Fehler Benutzereingabe esp")
        else:
            spdaten = elemente.Spieldaten() # Liste leeren bzw. mit leerer Liste überschreiben

            # Ablegung der Daten in das Objekt (nur geprüft)
            print(f"Benutzer ID = {nutzer.id}")
            spdaten.benutzerid = nutzer.id
            spdaten.spielid = idlist.dict_spiele(spname)
            spdaten.plattformid = idlist.dict_plattformen(pltfrm)
            spdaten.level = int(lvl) if lvl != "" else None
            spdaten.spielzeit = int(spz)
            spdaten.bewertung = int(ebw)
            spdaten.startdatum = esp if esp != "" else None
            spdaten.durchgespielt = dg
            spdaten.empfohlen = empf

            spBear_rm = z_Spieldaten.hinzufuegen(spdaten) # Speicherung der Daten auf der Datenbank
            if spBear_rm == 1: # Wenn allgemeine Probleme bei der Speicherung der Daten
                messagebox.showerror("Störung MariaDB", "Es gab bei der speicherung der Daten ein Problem. Sie gelangen nun in das Hauptmenü.")
                main() # Springt bei kritischem Fehler in das Hauptmenü
            elif spBear_rm == 2: # Gleicher Datensatz bereits vorhanden (Spielid, Plattformid sind auf der DB ein gemeinsames Unique)
                messagebox.showerror("Störung MariaDB", "Es existiert bereits ein gleicher Eintrag.")
            elif spBear_rm == 0: # Wenn erfolgreich
                messagebox.showinfo("Speicherung erfolgreich", "Die Spieldaten wurden erfolgreich gespeichert. Sie gelangen nun zum Homescreen")
                #print(spdaten.spielid, spdaten.benutzerid, spdaten.kategorieid, spdaten.plattformid, spdaten.level)
                main() # Springt zurück in das Hauptmenü
            else:
                messagebox.showerror("Störung MariaDB", "Fataler Fehler.")
                print("Irgendwas stimmt mit dem SQL Befehl nicht :c Sie gelangen nun in das Hauptmenü.")
                main() # Springt bei kritischem Fehler in das Hauptmenü

    main_clearwdw()
    button.gen_return()
    label.gen_title("Spiel hinzufügen")
    xwert = 750
    ywert = 90
    xadd = 150
    yadd = 20

    pic_background2.place(x=0, y=80, relwidth=1, relheight=1)
    tk.Label(root, text="Spielname *").place(x=xwert, y=ywert)
    ywert += yadd
    cb_spielname = ttk.Combobox(root, values=idlist.spiele, state="readonly")#.place(x=xwert, y=ywert)
    cb_spielname.place(x=xwert, y=ywert)
    ywert += yadd * 2

    tk.Label(root, text="Plattform *").place(x=xwert, y=ywert)
    ywert += yadd
    cb_plattform = ttk.Combobox(root, values=idlist.plattformen, state="readonly")#.place(x=xwert, y=ywert)
    cb_plattform.place(x=xwert, y=ywert)
    ywert += yadd * 2
    
    tk.Label(root, text="Level").place(x=xwert, y=ywert)
    ywert += yadd
    tf_level = ttk.Entry(root)
    tf_level.place(x=xwert, y=ywert)
    ywert += yadd * 2

    tk.Label(root, text="Spielzeit (in Std.) *").place(x=xwert, y=ywert)
    ywert += yadd
    tf_spielzeit = ttk.Entry(root)
    tf_spielzeit.place(x=xwert, y=ywert)
    ywert += yadd * 2
    
    tk.Label(root, text="Eigenbewertung (1-10) *").place(x=xwert, y=ywert)
    ywert += yadd
    tf_bewertung = ttk.Entry(root)
    tf_bewertung.place(x=xwert, y=ywert)
    ywert += yadd * 2
    
    tk.Label(root, text="Erster Spieltag (JJJJ-MM-TT)").place(x=xwert, y=ywert)
    ywert += yadd
    tf_erstSpieltag = ttk.Entry(root)
    tf_erstSpieltag.place(x=xwert, y=ywert)
    ywert += yadd * 3

    xwert -= 30
    tk.Label(root, text="Durchgespielt? *").place(x=xwert, y=ywert)
    ywert += yadd
    dg_wahl = tk.IntVar(value=0)
    ttk.Radiobutton(root, text="Ja", variable=dg_wahl, value=1).place(x=xwert, y=ywert)
    ywert += yadd + 5
    ttk.Radiobutton(root, text="Nein", variable=dg_wahl, value=2).place(x=xwert, y=ywert)
    ywert += yadd + 5
    ttk.Radiobutton(root, text="Nicht Angefangen", variable=dg_wahl, value=3).place(x=xwert, y=ywert)
    ywert -= yadd * 3
    ywert -= 10
    xwert += xadd

    tk.Label(root, text="Empfehlung? *").place(x=xwert, y=ywert)
    ywert += yadd
    empf_wahl = tk.IntVar(value=0)
    ttk.Radiobutton(root, text="Ja", variable=empf_wahl, value=1).place(x=xwert, y=ywert)
    ywert += yadd + 5
    ttk.Radiobutton(root, text="Nein", variable=empf_wahl, value=2).place(x=xwert, y=ywert)
    ywert += yadd + 5
    ttk.Radiobutton(root, text="Keine Angabe", variable=empf_wahl, value=3).place(x=xwert, y=ywert)

    ttk.Button(root, text="Speichern", command=check).place(x=730, y=700, width=200)

def nutzer_verwaltung(nutzer):
    print("Nutzer verwalten geklickt")

def abmelden(nutzer):
    exit()
    
def main(): # Das "eigentliche" Programm, bzw. Ablauf des Programms
    main_clearwdw()
    button.gen_hauptmenue(50, 110, 200, 0, 35) # Übergabe x,y,l
    pic_background.place(x=0, y=80, relwidth=1, relheight=1)
    button.gen_abmelden()
    label.gen_title("Hauptmenü")

callbacks = { # Verzeichnis zum Aufrufen der Funktionen nach Betätigung eines Buttons (Übergabewert "uebersicht" ruft uebersicht auf)
    "uebersicht": uebersicht,
    "bewertungen": bewertungen,
    "durchgespielt": durchgespielt,
    "empfohlen": empfohlen,
    "spiel_hinzufg": spiel_hinzufg,
    "nutzer_verwaltung": nutzer_verwaltung,
    "abmelden": abmelden,
    "main": main,
    "spiel_bearbeiten" : spiel_bearbeiten
}

# Deklaration der Pfade
azure = os.path.join(os.path.dirname(__file__), "themes", "azure", "azure.tcl")
pic_logo = os.path.join(os.path.dirname(__file__), "images", "logo.png")
pic_background = os.path.join(os.path.dirname(__file__), "images", "gameStatLogoMain2.png")
pic_background2 = os.path.join(os.path.dirname(__file__), "images", "hintergrundAllgemein.png")

daten = elemente.Daten()
spdaten = elemente.Spieldaten()
idlist = elemente.Idlist()

nutzer, login_status = anmeldung.start()
#nutzer, login_status = anmeldung.bypass()
#test_objektTestAnzeige.useranzeigen(nutzer) Nur zum Testen

if login_status == True:
    root = tk.Tk()
    root.geometry("1920x1080")
    #root.attributes("-fullscreen", True) # Vollbildansicht
    root.title("GameStat - Dein Spielmanager")

    # Einstellung des Aussehens der Benutzeroberfläche
    #root.tk.call("source", "themes/azure/azure.tcl")
    root.tk.call("source", azure) # Direkter Pfad hat nicht richtig funktioniert
    root.tk.call("set_theme", "light")
    style = ttk.Style()
    style.theme_use("azure-light")
    style.configure("Accent.TButton", foreground="white", background="#007BFF")
    style.map("Accent.TButton", background=[("active", "#0056b3")], foreground=[("disabled", "gray")])

    # Deklaration der Bilder
    #hint_bild = Image.open("images/Bild1.jpg") # Setzen eines potentiellen Hintergrundbildes
    #hint_bild = ImageTk.PhotoImage(hint_bild)
    background = Image.open(pic_background) # Deklaration des Programmlogos
    background = background.resize((1750, 900)) # Einstellung der größe
    background = ImageTk.PhotoImage(background) # Macht es zu einem TKinter Bild
    pic_background = tk.Label(root, image=background) # Speichert das Bild in ein Label

    print(pic_background2)
    background2 = Image.open(pic_background2)
    background2 = background2.resize((2000, 800))
    background2 = ImageTk.PhotoImage(background2)
    pic_background2 = tk.Label(root, image=background2)

    # hb_canvas = tk.Canvas(root, width=1200, height=800)
    # hb_canvas.pack(fill="both", expand=True)
    # hb_canvas.create_image(0, 0, image=hint_bild, anchor="nw")

    button = elemente.HauptBedienung(root, nutzer, callbacks) # Buttons werden aus elemente.py generiert.
    label = elemente.HauptLabel(root) # Labels werden aus elemente.py generiert.
    main()
    root.mainloop()