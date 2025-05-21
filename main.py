import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import elemente # Hier sind die Elemente im Fenster (Knöpfe und co. gespeichert)
from functools import partial
import anmeldung
#from PIL import Image, ImageTk
import z_Datenuebertragung_SQL

class Testobjekt_main: # Klasse fliegt nach Entwicklungsphase raus. Entfernen
    def __init__(self):
        self.benutzer = "MaximalBaum34"
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

def uebersicht(nutzer): # Zeigt eine Tabelle mit allen Spielständen / Games an
    print("Übersicht geklickt")

def bewertungen(nutzer): # Zeigt eine Tabelle mit allen Spielen mit aufsteigender Bewertung an
    print("Bewertungen geklickt")
    label.gen_title("Bewertungen")

def durchgespielt(nutzer): # Zeigt eine Tabelle mit allen durchgespielten Spielen an
    print("Durchgespielt geklickt")

def empfohlen(nutzer): # Zeigt eine Tabelle mit allen empfohlenen Games an
    print("Empfohlen geklickt")

def spiel_bearbeiten():
    def aendern(): # Zeigt nach der Eingabe eines Spiels die Oberfläche zur änderung der Daten an
        def check(): # Speicherung neuer Eingaben (Weiter Button)
            lvl = tf_level.get()
            spz = tf_spielzeit.get()
            bwt = tf_bewertung.get()
            esp = tf_startdatum.get()
            dgw = dg_wahl.get()
            emw = empf_wahl.get()

            # Prüfung, ob die Angaben aus Spiel bearbeiten gültig sind
            if checkvalue.intager(lvl, "Level") == False:
                print("Fehler Benutzereingabe")
            elif checkvalue.intager(spz, "Spielzeit") == False:
                print("Fehler Benutzereingabe")
            elif checkvalue.rang(bwt, 1, 10, "Bewertung") == False:
                print("Fehler Benutzereingabe")
            elif checkvalue.datum(esp, "Startdatum") == False:
                print("Fehler Benutzereingabe")
            elif dgw == 0 or emw == 0:
                messagebox.showerror("Eingabefehler", "Bitte wählen Sie auch aus, ob Sie bereits angefangen und / oder durchgespielt haben.")
            else:
                print("Eingaben korrekt.")

                print(dgw, emw)

                # Konvertierung und speicherung in Objekt
                spdaten.level = int(lvl)
                spdaten.spielzeit = int(lvl)
                spdaten.bewertung = int(bwt)
                spdaten.startdatum = esp
                spdaten.durchgespielt = dgw
                spdaten.empfohlen = emw

                # Übergabe per SQL Befehl an die Datenbank
                #rw2 = z_Datenuebertragung_SQL.spiel_bearbeiten_speichern(spdaten)
                rw2 = True # ENTFERNEN! und Zeite darüber "Einkommentieren"
                if rw2 == True:
                    messagebox.showinfo("Speicherung", "Die Speicherung war erfolgreich! Sie gelangen nun in das Hauptmenü.")
                    main()
                else:
                    messagebox.showerror("Speicherung", "Leider gab es ein Problem mit der Speicherung der Spieldaten. Bitte versuchen Sie es erneut.")
                    check()

        game = cb_spielname.get()
        if game != "":
            main_clearwdw()
            spid = game[0]
            #spdaten, rw1 = z_Datenuebertragung_SQL.spieldaten_abrufen(spid)
            rw1 = True # ENTFERNEN!!
            if rw1 == False:
                messagebox.showerror("MariaDB Fehler", "Fehler bei dem Abrufen von Daten. Sie gelangen nun in das Hauptmenü.")
                main()

            button.gen_abmelden()
            button.gen_return()

            xwert = 500
            ywert = 90
            xadd = 150
            yadd = 20

            label.gen_title(f"Bearbeiten von {game}")

            tk.Label(root, text="Level").place(x=xwert, y=ywert)
            ywert += yadd
            tf_level = ttk.Entry(root)
            tf_level.place(x=xwert, y=ywert)
            ywert += yadd * 2

            tk.Label(root, text="Spielzeit (in Std.)").place(x=xwert, y=ywert)
            ywert += yadd
            tf_spielzeit = ttk.Entry(root)
            tf_spielzeit.place(x=xwert, y=ywert)
            ywert += yadd * 2
            
            tk.Label(root, text="Eigenbewertung (1-10)").place(x=xwert, y=ywert)
            ywert += yadd
            tf_bewertung = ttk.Entry(root)
            tf_bewertung.place(x=xwert, y=ywert)
            ywert += yadd * 2
            
            tk.Label(root, text="Erster Spieltag").place(x=xwert, y=ywert)
            ywert += yadd
            tf_startdatum = ttk.Entry(root)
            tf_startdatum.place(x=xwert, y=ywert)
            ywert += yadd * 3

            xwert -= 30
            tk.Label(root, text="Durchgespielt?").place(x=xwert, y=ywert)
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

            tk.Label(root, text="Empfehlung?").place(x=xwert, y=ywert)
            ywert += yadd
            empf_wahl = tk.IntVar(value=0)
            ttk.Radiobutton(root, text="Ja", variable=empf_wahl, value=1).place(x=xwert, y=ywert)
            ywert += yadd + 5
            ttk.Radiobutton(root, text="Nein", variable=empf_wahl, value=2).place(x=xwert, y=ywert)
            ywert += yadd + 5
            ttk.Radiobutton(root, text="Keine Angabe", variable=empf_wahl, value=3).place(x=xwert, y=ywert)

            ttk.Button(root, text="Speichern", command=check).place(x=500, y=700, width=200)

        else:
            messagebox.showinfo("Eingabe", "Bitte wählen Sie ein Spiel aus. Sofern nicht vorhanden, bitte anlegen.")

    main_clearwdw()
    #spielliste, rw = z_Datenuebertragung_SQL.spiele_abrufen(spdaten)
    rw = True # ENTFERNEN
    spielliste = ["1, GTA5, 12", "2, Minecraft, 55"]
    if rw == False:
        messagebox.showerror("MariaDB Fehler", "Es gab einen Fehler bei der Datenübertragung. Sie gelangen zurück zum Hauptmenü.")
        main()
    else:
        button.gen_return()
        label.gen_title("Spiel bearbeiten")
        xwert = 500
        ywert = 90
        xadd = 150
        yadd = 20

        tk.Label(root, text="Spielname").place(x=xwert, y=ywert)
        ywert += yadd
        cb_spielname = ttk.Combobox(root, values=spielliste, state="readonly")
        cb_spielname.place(x=xwert, y=ywert)
        ywert += yadd * 2

        ttk.Button(root, text="Weiter", command=aendern).place(x=500, y=700, width=200)


def spiel_hinzufg():
    def check():
        dg = dg_wahl.get()
        empf = empf_wahl.get()
        spname = cb_spielname.get()

        print(empf)
        print(dg)
    
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
    ttk.Entry(root).place(x=xwert, y=ywert)
    ywert += yadd * 2

    tk.Label(root, text="Spielzeit (in Std.)").place(x=xwert, y=ywert)
    ywert += yadd
    ttk.Entry(root).place(x=xwert, y=ywert)
    ywert += yadd * 2
    
    tk.Label(root, text="Eigenbewertung (1-10)").place(x=xwert, y=ywert)
    ywert += yadd
    ttk.Entry(root).place(x=xwert, y=ywert)
    ywert += yadd * 2
    
    tk.Label(root, text="Erster Spieltag").place(x=xwert, y=ywert)
    ywert += yadd
    ttk.Entry(root).place(x=xwert, y=ywert)
    ywert += yadd * 3

    xwert -= 30
    tk.Label(root, text="Durchgespielt?").place(x=xwert, y=ywert)
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

    tk.Label(root, text="Empfehlung?").place(x=xwert, y=ywert)
    ywert += yadd
    empf_wahl = tk.IntVar(value=0)
    ttk.Radiobutton(root, text="Ja", variable=empf_wahl, value=1).place(x=xwert, y=ywert)
    ywert += yadd + 5
    ttk.Radiobutton(root, text="Nein", variable=empf_wahl, value=2).place(x=xwert, y=ywert)
    ywert += yadd + 5
    ttk.Radiobutton(root, text="Keine Angabe", variable=empf_wahl, value=3).place(x=xwert, y=ywert)

    ttk.Button(root, text="Weiter", command=check).place(x=500, y=700, width=200)

def nutzer_verwaltung(nutzer):
    print("Nutzer verwalten geklickt")

def abmelden(nutzer):
    return
    
def main(): # Das "eigentliche" Programm, bzw. Ablauf des Programms
    main_clearwdw()
    button.gen_hauptmenue(50, 110, 200, 0, 35) # Übergabe x,y,l
#    img_logo.place(x=100, y=100, relwidth=1, relheight=1)
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
checkvalue = elemente.Check()
spdaten = elemente.Spieldaten()
nutzer = anmeldung.Nutzer() # ENTFERNEN!!, ist nur da, weil ich faul bin.

nutzer, login_status = anmeldung.start()
#nutzer, login_status = anmeldung.bypass()

if login_status == True:
    root = tk.Tk()
    root.geometry("1200x800")
    root.title("GameStat - Dein Spielmanager")

    # Einstellung des Aussehens der Benutzeroberfläche
    root.tk.call("source", "themes/azure/azure.tcl")
    root.tk.call("set_theme", "light")
    style = ttk.Style()
    style.theme_use("azure-light")
    style.configure("Accent.TButton", foreground="white", background="#007BFF")
    style.map("Accent.TButton", background=[("active", "#0056b3")], foreground=[("disabled", "gray")])

    # Deklaration der Bilder
    # hint_bild = Image.open("images/Bild1.jpg") # Setzen eines potentiellen Hintergrundbildes
    # hint_bild = ImageTk.PhotoImage(hint_bild)
    # new_logo = Image.open("images/logo.png") # Deklaration des Programmlogos
    # skal_logo = new_logo.resize((500, 500))
    # img1_logo = ImageTk.PhotoImage(skal_logo)
    # img_logo = tk.Label(root, image=img1_logo)

    # hb_canvas = tk.Canvas(root, width=1200, height=800)
    # hb_canvas.pack(fill="both", expand=True)
    # hb_canvas.create_image(0, 0, image=hint_bild, anchor="nw")

    button = elemente.HauptBedienung(root, nutzer, callbacks) # Buttons werden aus elemente.py generiert.
    label = elemente.HauptLabel(root) # Labels werden aus elemente.py generiert.
    main()
    root.mainloop()