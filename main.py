import tkinter as tk
from tkinter import ttk
import elemente # Hier sind die Elemente im Fenster (Klöpfe und co. gespeichert)
#from elemente import HauptBedienung, HauptLabel
from functools import partial
import anmeldung

class Testobjekt_main: # Klasse fliegt nach Entwicklungsphase raus. Entfernen
    def __init__(self):
        self.benutzer = "maxim"
        self.passwort = "1234"
        self.vorname = "Maxim"
        self.email = "maxim@gmail.com"
        self.land = "Deutschland"
        self.sprache = "deutsch"
        self.geschlecht = "Männlich"
        self.geburtsdatum = "1234"


def main_clearwdw(): # Löscht den gesamten Inhalt eines Fensters!
    for widget in root.winfo_children():
        widget.place_forget()
    button.gen_abmelden()

def uebersicht(nutzer):
    print("Übersicht geklickt")

def bewertungen(nutzer):
    print("Bewertungen geklickt")
    label.gen_title("Bewertungen")

def durchgespielt(nutzer):
    print("Durchgespielt geklickt")

def empfohlen(nutzer):
    print("Empfohlen geklickt")

def spiel_bearbeiten(nutzer):
    print("Spiel Bearbeiten geklickt")

def spiel_hinzufg(nutzer):
    main_clearwdw()
    button.gen_return()
    label.gen_title("Spiel Hinzufügen")
    def gen_gui_oberflaeche():
        xwert = 500
        ywert = 90
        xadd = 150
        yadd = 20
        
        # Textfelder und Comboboxen
        lb_spielname.place(x=xwert, y=ywert)
        ywert += yadd
        tf_spielname.place(x=xwert, y=ywert)
        ywert += yadd * 2

        lb_plattform.place(x=xwert, y=ywert)
        ywert += yadd
        tf_plattform.place(x=xwert, y=ywert)
        ywert += yadd * 2

        lb_kategorie.place(x=xwert, y=ywert)
        ywert += yadd
        tf_kategorie.place(x=xwert, y=ywert)
        ywert += yadd * 2

        lb_level.place(x=xwert, y=ywert)
        ywert += yadd
        tf_level.place(x=xwert, y=ywert)
        ywert += yadd * 2

        lb_spielzeit.place(x=xwert, y=ywert)
        ywert += yadd
        tf_spielzeit.place(x=xwert, y=ywert)
        ywert += yadd * 2

        lb_eigenbewertung.place(x=xwert, y=ywert)
        ywert += yadd
        tf_eigenbewertung.place(x=xwert, y=ywert)
        ywert += yadd * 2

        lb_startdatum.place(x=xwert, y=ywert)
        ywert += yadd
        tf_startdatum.place(x=xwert, y=ywert)
        ywert += yadd * 2

        # Radiobuttons
        xwert -= 30
        lb_durchgespielt.place(x=xwert, y=ywert)
        ywert += yadd
        rb_dg_ja.place(x=xwert, y=ywert)
        ywert += yadd + 5
        rb_dg_nein.place(x=xwert, y=ywert)
        ywert -= yadd * 2
        ywert -= 5
        xwert += xadd

        lb_empfohlen.place(x=xwert, y=ywert)
        ywert += yadd
        rb_empf_ja.place(x=xwert, y=ywert)
        ywert += yadd + 5
        rb_empf_nein.place(x=xwert, y=ywert)
        #ywert += yadd * 2 - 5

    def check():
        dg = dg_wahl.get() # 1=Ja, 0=Nein
        empf = empf_wahl.get() # 1=Ja, 0=Nein

        print(empf)
        print(dg)

    # Labels
    lb_spielname = tk.Label(root, text="Spielname")
    lb_plattform = tk.Label(root, text="Plattform")
    lb_kategorie = tk.Label(root, text="Spielgategorie")
    lb_level = tk.Label(root, text="Level")
    lb_spielzeit = tk.Label(root, text="Spielzeit (in Std.)")
    lb_eigenbewertung = tk.Label(root, text="Eigenbewertung (1-10)")
    lb_startdatum = tk.Label(root, text="Erster Spieltag")
    lb_durchgespielt = tk.Label(root, text="Durchgespielt?")
    lb_empfohlen = tk.Label(root, text="Empfehlung?")

    # Eingabefelder
    tf_spielname = ttk.Entry(root)
    tf_plattform = ttk.Entry(root)
    tf_kategorie = ttk.Entry(root) # Noch schauen wegen Mehrfachauswahl!! (ggf Combobox!)
    tf_level = ttk.Entry(root)
    tf_spielzeit = ttk.Entry(root)
    tf_eigenbewertung = ttk.Entry(root)
    tf_startdatum = ttk.Entry(root)

    # Radio Buttons
    dg_wahl = tk.IntVar(value=2)
    rb_dg_ja = ttk.Radiobutton(root, text="Ja", variable=dg_wahl, value=1)
    rb_dg_nein = ttk.Radiobutton(root, text="Nein", variable=dg_wahl, value=0)
    rb_dg_nicht_angef = ttk.Radiobutton(root, text="Nicht Angefangen", variable=dg_wahl, value=2)

    empf_wahl = tk.IntVar(value=2)
    rb_empf_ja = ttk.Radiobutton(root, text="Ja", variable=empf_wahl, value=1)
    rb_empf_nein = ttk.Radiobutton(root, text="Nein", variable=empf_wahl, value=0)
    rb_dg_keine_ang = ttk.Radiobutton(root, text="Keine Angabe", variable=dg_wahl, value=2)

    # Buttons
    bn_weiter = ttk.Button(root, text="Weiter", command=check).place(x=500, y=700, width=200) # Button wird hier sofort platziert.

    gen_gui_oberflaeche()

def nutzer_verwaltung(nutzer):
    print("Nutzer verwalten geklickt")

def abmelden(nutzer):
    return
    
def main(nutzer): # Das "eigentliche" Programm, bzw. Ablauf des Programms
    main_clearwdw()
    button.gen_hauptmenue(50, 110, 200, 0, 35) # Übergabe x,y,l
    button.gen_abmelden()
    label.gen_title("Hauptmenü")

callbacks = { # Verzeichnis zum Aufrufen der Funktionen nach betätigung eines Buttons (Übergabewert "uebersicht" ruft uebersicht auf)
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

#nutzer, login_status = anmeldung.start()
nutzer, login_status = anmeldung.bypass()
#nutzer = Testobjekt_main()
#login_status = True

if login_status == True:
    root = tk.Tk()
    style = ttk.Style()
    root.tk.call("source", "themes/forest-light.tcl")
    root.geometry("1200x800")
    root.title("GameStat - Dein Spielmanager")
    style.theme_use("forest-light")

    button = elemente.HauptBedienung(root, nutzer, callbacks) # Buttons werden aus elemente.py generiert.
    label = elemente.HauptLabel(root) # Labels werden aus elemente.py generiert.
    main(nutzer)
    root.mainloop()