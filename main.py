import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import elemente # Hier sind die Elemente im Fenster (Klöpfe und co. gespeichert)
#from elemente import HauptBedienung, HauptLabel
from functools import partial
import anmeldung
from PIL import Image, ImageTk

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
    def check():
        def aenderung_game(): # Speicherung neuer Eingaben
            print("123")

        game = cb_spielname.get()
        
        if game != "":
            print(game)
            main_clearwdw()
            button.gen_abmelden()
            button.gen_return()

            xwert = 500
            ywert = 90
            xadd = 150
            yadd = 20

            tk.Label(root, text="Level").place(x=xwert, y=ywert)
            ywert += yadd
            tf_level = ttk.Entry(root).place(x=xwert, y=ywert)
            ywert += yadd * 2

            tk.Label(root, text="Spielzeit (in Std.)").place(x=xwert, y=ywert)
            ywert += yadd
            tf_spielzeit = ttk.Entry(root).place(x=xwert, y=ywert)
            ywert += yadd * 2
            
            tk.Label(root, text="Eigenbewertung (1-10)").place(x=xwert, y=ywert)
            ywert += yadd
            ttk.Entry(root).place(x=xwert, y=ywert)
            ywert += yadd * 2
            
            tk.Label(root, text="Erster Spieltag").place(x=xwert, y=ywert)
            ywert += yadd
            tf_startdatum = ttk.Entry(root).place(x=xwert, y=ywert)
            ywert += yadd * 3

            xwert -= 30
            tk.Label(root, text="Durchgespielt?").place(x=xwert, y=ywert)
            ywert += yadd
            dg_wahl = tk.IntVar(value=0)
            rb_dg_ja = ttk.Radiobutton(root, text="Ja", variable=dg_wahl, value=1).place(x=xwert, y=ywert)
            ywert += yadd + 5
            rb_dg_nein = ttk.Radiobutton(root, text="Nein", variable=dg_wahl, value=2).place(x=xwert, y=ywert)
            ywert += yadd + 5
            rb_dg_nicht_angef = ttk.Radiobutton(root, text="Nicht Angefangen", variable=dg_wahl, value=3).place(x=xwert, y=ywert)
            ywert -= yadd * 3
            ywert -= 10
            xwert += xadd

            tk.Label(root, text="Empfehlung?").place(x=xwert, y=ywert)
            ywert += yadd
            empf_wahl1 = tk.IntVar(value=0)
            rb_empf_ja = ttk.Radiobutton(root, text="Ja", variable=empf_wahl1, value=1).place(x=xwert, y=ywert)
            ywert += yadd + 5
            rb_empf_nein = ttk.Radiobutton(root, text="Nein", variable=empf_wahl1, value=2).place(x=xwert, y=ywert)
            ywert += yadd + 5
            rb_dg_keine_ang = ttk.Radiobutton(root, text="Keine Angabe", variable=empf_wahl1, value=3).place(x=xwert, y=ywert)

            bn_weiter = ttk.Button(root, text="Weiter", command=check).place(x=500, y=700, width=200)

        else:
            messagebox.showinfo("Eingabe", "Bitte wählen Sie ein Spiel aus. Sofer nicht vorhanden, bitte anlegen.")
    main_clearwdw()
    button.gen_return()
    label.gen_title("Spiel bearbeiten")
    xwert = 500
    ywert = 90
    xadd = 150
    yadd = 20

    tk.Label(root, text="Spielname").place(x=xwert, y=ywert)
    ywert += yadd
    cb_spielname = ttk.Combobox(root, values=daten.user_spiele, state="readonly")#.place(x=xwert, y=ywert)
    cb_spielname.place(x=xwert, y=ywert)
    ywert += yadd * 2

    bn_weiter = ttk.Button(root, text="Weiter", command=check).place(x=500, y=700, width=200)


def spiel_hinzufg(nutzer):
    def check():
        dg = dg_wahl.get()
        empf = empf_wahl.get()
        spname = cb_spielname.get()

        print(empf)
        print(dg)
    
    def fehler_mitteilung():
        messagebox.showwarning("Bitte füllen Sie die mit * Markierten Felder vollständig aus.")
    
    main_clearwdw()
    button.gen_return()
    label.gen_title("Spiel hinzufügen")
    xwert = 500
    ywert = 90
    xadd = 150
    yadd = 20

    tk.Label(root, text="Spielname").place(x=xwert, y=ywert)
    ywert += yadd
    cb_spielname = ttk.Combobox(root, values=daten.spiele, state="readonly")#.place(x=xwert, y=ywert)
    cb_spielname.place(x=xwert, y=ywert)
    ywert += yadd * 2

    tk.Label(root, text="Plattform").place(x=xwert, y=ywert)
    ywert += yadd
    cb_plattform = ttk.Combobox(root, values=daten.plattform, state="readonly")#.place(x=xwert, y=ywert)
    cb_plattform.place(x=xwert, y=ywert)
    ywert += yadd * 2
    
    tk.Label(root, text="Spielgategorie").place(x=xwert, y=ywert)
    ywert += yadd
    cb_kategorie = ttk.Combobox(root, values=daten.kategorien, state="readonly")#.place(x=xwert, y=ywert) # Noch schauen wegen Mehrfachauswahl!! (ggf Combobox!)
    cb_kategorie.place(x=xwert, y=ywert)
    ywert += yadd * 2
    
    tk.Label(root, text="Level").place(x=xwert, y=ywert)
    ywert += yadd
    tf_level = ttk.Entry(root).place(x=xwert, y=ywert)
    ywert += yadd * 2

    tk.Label(root, text="Spielzeit (in Std.)").place(x=xwert, y=ywert)
    ywert += yadd
    tf_spielzeit = ttk.Entry(root).place(x=xwert, y=ywert)
    ywert += yadd * 2
    
    tk.Label(root, text="Eigenbewertung (1-10)").place(x=xwert, y=ywert)
    ywert += yadd
    ttk.Entry(root).place(x=xwert, y=ywert)
    ywert += yadd * 2
    
    tk.Label(root, text="Erster Spieltag").place(x=xwert, y=ywert)
    ywert += yadd
    tf_startdatum = ttk.Entry(root).place(x=xwert, y=ywert)
    ywert += yadd * 3

    xwert -= 30
    tk.Label(root, text="Durchgespielt?").place(x=xwert, y=ywert)
    ywert += yadd
    dg_wahl = tk.IntVar(value=0)
    rb_dg_ja = ttk.Radiobutton(root, text="Ja", variable=dg_wahl, value=1).place(x=xwert, y=ywert)
    ywert += yadd + 5
    rb_dg_nein = ttk.Radiobutton(root, text="Nein", variable=dg_wahl, value=2).place(x=xwert, y=ywert)
    ywert += yadd + 5
    rb_dg_nicht_angef = ttk.Radiobutton(root, text="Nicht Angefangen", variable=dg_wahl, value=3).place(x=xwert, y=ywert)
    ywert -= yadd * 3
    ywert -= 10
    xwert += xadd

    tk.Label(root, text="Empfehlung?").place(x=xwert, y=ywert)
    ywert += yadd
    empf_wahl = tk.IntVar(value=0)
    rb_empf_ja = ttk.Radiobutton(root, text="Ja", variable=empf_wahl, value=1).place(x=xwert, y=ywert)
    ywert += yadd + 5
    rb_empf_nein = ttk.Radiobutton(root, text="Nein", variable=empf_wahl, value=2).place(x=xwert, y=ywert)
    ywert += yadd + 5
    rb_dg_keine_ang = ttk.Radiobutton(root, text="Keine Angabe", variable=empf_wahl, value=3).place(x=xwert, y=ywert)

    bn_weiter = ttk.Button(root, text="Weiter", command=check).place(x=500, y=700, width=200)

def nutzer_verwaltung(nutzer):
    print("Nutzer verwalten geklickt")

def abmelden(nutzer):
    return
    
def main(nutzer): # Das "eigentliche" Programm, bzw. Ablauf des Programms
    main_clearwdw()
    button.gen_hauptmenue(50, 110, 200, 0, 35) # Übergabe x,y,l
    img_logo.place(x=100, y=100, relwidth=1, relheight=1)
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

daten = elemente.Daten()

#nutzer, login_status = anmeldung.start()
nutzer, login_status = anmeldung.bypass()
#nutzer = Testobjekt_main()
#login_status = True

if login_status == True:
    # Erzeugen des Fensters
    root = tk.Tk()
    root.geometry("1200x800")
    root.title("GameStat - Dein Spielmanager")

    # Einstellung des Aussehens der Benutzeroberfläche
    root.tk.call("source", "themes/forest-light.tcl")
    style = ttk.Style()
    style.theme_use("forest-light")
    style.configure("Accent.TButton", foreground="white", background="#007BFF")
    style.map("Accent.TButton", background=[("active", "#0056b3")], foreground=[("disabled", "gray")])

    # Deklaration der Bilder
    hint_bild = Image.open("images/Bild1.jpg") # Setzen eines potentiellen Hintergrundbildes
    hint_bild = ImageTk.PhotoImage(hint_bild)
    new_logo = Image.open("images/logo.png") # Deklaration des Programmlogos
    skal_logo = new_logo.resize((500, 500))
    img1_logo = ImageTk.PhotoImage(skal_logo)
    img_logo = tk.Label(root, image=img1_logo)

    # hb_canvas = tk.Canvas(root, width=1200, height=800)
    # hb_canvas.pack(fill="both", expand=True)
    # hb_canvas.create_image(0, 0, image=hint_bild, anchor="nw")

    button = elemente.HauptBedienung(root, nutzer, callbacks) # Buttons werden aus elemente.py generiert.
    label = elemente.HauptLabel(root) # Labels werden aus elemente.py generiert.
    main(nutzer)
    root.mainloop()