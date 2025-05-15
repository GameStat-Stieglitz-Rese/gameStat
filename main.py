import tkinter as tk
from tkinter import ttk
#import elemente # Hier sind die Elemente im Fenster (Klöpfe und co. gespeichert)
from functools import partial
#import anmeldung # Testweise

class Testobjekt_main:
    def __init__(self):
        self.benutzer = "maxim"
        self.passwort = "1234"
        self.vorname = "Maxim"
        self.email = "maxim@gmail.com"
        self.land = "Deutschland"
        self.sprache = "deutsch"
        self.geschlecht = "Männlich"
        self.geburtsdatum = "1234"

class HauptBedienung:
    def __init__(self, nutzer):
        # Buttons Hauptmenü
        self.bn_uebersicht = ttk.Button(root, text="Übersicht", command=partial(uebersicht, nutzer))
        self.bn_bewertungen = ttk.Button(root, text="Bewertungen", command=partial(bewertungen, nutzer))
        self.bn_durchgespielt = ttk.Button(root, text="Durchgespielt", command=partial(durchgespielt, nutzer))
        self.bn_empfohlen = ttk.Button(root, text="Empfohlene Spiele", command=partial(empfohlen, nutzer))
        self.bn_spiel_hinzufg = ttk.Button(root, text="Spiel Hinzufügen", command=partial(spiel_hinzufg, nutzer))
        self.bn_nutzer_verwaltung = ttk.Button(root, text="Benutzer verwalten", command=partial(nutzer_verwaltung, nutzer))
        self.bn_abmeldung = tk.Button(root, text="<- Abmelden", fg="red", command=partial(abmelden, nutzer))
        self.bn_return = ttk.Button(root, text="Hauptmenü", command=partial(main, nutzer))

    def gen_hauptmenue(self, xwert, ywert, lwert, xadd, yadd): 
        # Generierung des Hauptmenüs(Übergabe: X-Pos, Y-Pos, Länge, Abstand vertikal, Abstand horizontal)
        self.bn_uebersicht.place(x=xwert, y=ywert, width=lwert)
        ywert += yadd
        self.bn_bewertungen.place(x=xwert, y=ywert, width=lwert)
        ywert += yadd
        self.bn_durchgespielt.place(x=xwert, y=ywert, width=lwert)
        ywert += yadd
        self.bn_empfohlen.place(x=xwert, y=ywert, width=lwert)
        ywert += yadd
        self.bn_spiel_hinzufg.place(x=xwert, y=ywert, width=lwert)
        ywert += yadd
        self.bn_nutzer_verwaltung.place(x=xwert, y=ywert, width=lwert)

    def gen_abmelden(self): # Generierung des Abmeldebuttons (Übergabe: X-Pos, Y-Pos, Länge)
        self.bn_abmeldung.place(x=50, y=750, width=200)

    def gen_return(self):
        self.bn_return.place(x=50, y=720, width=200)


class HauptLabel:
    def __init__(self):
        self.lb_title = tk.Label(root, text="Ueberschrift", font=("Arial", 20))

    def gen_title(self, name):
        self.lb_title.config(text=name) # Ändern des Textes der Überschrift zu den übergebenen String
        self.lb_title.place(x=50, y=10)

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

def spiel_hinzufg(nutzer):
    main_clearwdw()
    button.gen_return()
    label.gen_title("Spiel Hinzufügen")
    def gen_gui_oberflaeche():
        xwert = 230
        ywert = 90
        xadd = 150
        yadd = 20

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

        lb_durchgespielt.place(x=xwert, y=ywert)
        ywert += yadd
        rb_dg_ja.place(x=xwert, y=ywert)
        ywert += yadd
        rb_dg_nein.place(x=xwert, y=ywert)
        ywert -= yadd * 2
        xwert += xadd

        lb_empfohlen.place(x=xwert, y=ywert)
        ywert += yadd
        rb_empf_ja.place(x=xwert, y=ywert)
        ywert += yadd
        rb_empf_nein.place(x=xwert, y=ywert)
        ywert += yadd * 2

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

    empf_wahl = tk.IntVar(value=2)
    rb_empf_ja = ttk.Radiobutton(root, text="Ja", variable=empf_wahl, value=1)
    rb_empf_nein = ttk.Radiobutton(root, text="Nein", variable=empf_wahl, value=0)

    # Buttons
    bn_weiter = ttk.Button(root, text="Weiter", command=check).place(x=500, y=500)

    gen_gui_oberflaeche()

def nutzer_verwaltung(nutzer):
    print("Nutzer verwalten geklickt")

def abmelden(nutzer):
    print("Abmelden gedrückt")
    
def main(nutzer): # Das "eigentliche" Programm, bzw. Ablauf des Programms
    main_clearwdw()
    button.gen_hauptmenue(50, 60, 200, 0, 25) # Übergabe x,y,l
    button.gen_abmelden()
    label.gen_title("Hauptmenü")

root = tk.Tk()
root.geometry("1200x800")
root.title("GameStat - Dein Spielemanager")

nutzer = Testobjekt_main() # Testnutzer nur während der Entwicklung
button = HauptBedienung(nutzer)
label = HauptLabel()

main(nutzer)
root.mainloop()