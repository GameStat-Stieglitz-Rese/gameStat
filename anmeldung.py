import tkinter as tk
from tkinter import ttk
from functools import partial # Zum ausführen von Commands in einem Tkinter Element. Syntax: partial({Funktion}, {Argument})
import objektTestAnzeige

class Nutzer(): # Diese Klasse legt bei Aufruf ein Objekt mit allen relevanten Benutzerdaten an.
    def __init__(self):
        self.nutzername = None
        self.passwort = None
        self.vorname = None
        self.email = None
        self.land = None
        self.sprache = None
        self.geschlecht = None
        self.geburtsdatum = None

def clearwdw(): # Löscht den gesamten Inhalt eines Fensters!
    for widget in root.winfo_children():
        widget.destroy()

def home():
    bn_anmelden = tk.Button(root, text="Anmelden", command=partial(objektTestAnzeige.useranzeigen, nutzer))
    bn_abbrechen = tk.Button(root, text="Abbruch", command=exit)
    bn_registrieren = tk.Button(root, text="Registrieren")
    tf_nutzername = tk.Entry(root, textvariable=nutzer.nutzername)
    tf_nutzerpasswort = tk.Entry(root, textvariable=nutzer.passwort, show="*")
    lb_nutzername = tk.Label(root, text="Benutzername:")
    lb_nutzerpasswort = tk.Label(root, text="Passwort:")

    a = 100
    b = 50
    abstand=20
    # Eingabefelder Benutzername und Passwort Anordnung mit Label:
    lb_nutzername.place(x=a, y=b)
    b += abstand + 2
    tf_nutzername.place(x=a, y=b)
    b += abstand
    lb_nutzerpasswort.place(x=a, y=b)
    b += abstand + 2
    tf_nutzerpasswort.place(x=a, y=b)
    b = b + abstand + 20 # Abschluss mit zusätzlichem Abstand
    
    abstand = 30
    # Buttons Anordnung:
    bn_anmelden.place(x=a, y=b)
    b += abstand
    bn_registrieren.place(x=a, y=b)
    b += abstand
    bn_abbrechen.place(x=a, y=b)

def registrieren():    
    # Registrieren GUI Elemente (tf = Textfeld)
    tf_vorname = tk.Entry(root)
    tf_benutzername = tk.Entry(root)
    tf_pw = tk.Entry(root)
    tf_pw_best = tk.Entry(root)
    tf_email = tk.Entry(root)
    tf_land = tk.Entry(root)
    tf_sprache = tk.Entry(root)
    # Geschlecht in Klärung!
    tf_geburtsdatum = tk.Entry(root)
    bt_bestaetigen = tk.Button(root, text="Bestätigen", command="")

    # Einfügen von Elementen
    tf_vorname.place(x=20, y=20)
    tf_benutzername.place(x=20, y=50)


# Deklaration der Variablen
nutzer = Nutzer()
#nutzername = ""
#nutzerpasswort = ""

# Erzeugen des Fensters
root = tk.Tk()
root.title("GameStat - Anmeldung")
root.geometry("400x500")
home()
root.mainloop()