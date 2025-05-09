import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
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
    clearwdw()
    def bn_anmelden_check(nutzer):
        nutzer.nutzername = tf_nutzername.get()
        nutzer.passwort = tf_nutzerpasswort.get()
        if nutzer.nutzername != "" and nutzer.passwort != "": # Prüfung, ob Benutzer etwas eingegeben hat
            objektTestAnzeige.useranzeigen(nutzer)
#            +++ +++ +++ Hier Aufruf des SQL Befehls und deklaration rueckmeldung! (Prüfung Benutzerdaten) +++ +++ +++
#            if rueckmeldung == True:
#                +++ +++ +++ Hier Aufruf des SQL Befehls! (Abrufen vollständige Benutzerdaten) +++ +++ +++
        else:
            print("Fehler: Benutzer hat nicht alle erforderlichen Daten eingegeben.")
            messagebox.showerror("Eingabefehler", "Bitte geben Sie Benutzernamen und Passwort ein.")

    bn_anmelden = tk.Button(root, text="Anmelden", command=partial(bn_anmelden_check, nutzer))
    bn_abbrechen = tk.Button(root, text="Abbruch", command=exit)
    bn_registrieren = tk.Button(root, text="Registrieren", command=registrieren)
    tf_nutzername = tk.Entry(root, textvariable=nutzer.nutzername)
    tf_nutzerpasswort = tk.Entry(root, textvariable=nutzer.passwort, show="*")
    lb_nutzername = tk.Label(root, text="Benutzername:")
    lb_nutzerpasswort = tk.Label(root, text="Passwort:")
    lb_rueckmeldung = tk.Label(root, text="")

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
    #b += abstand
    a += 100
    bn_registrieren.place(x=a, y=b)
    a -= 100
    b += abstand
    bn_abbrechen.place(x=a, y=b)
    b += abstand
    lb_rueckmeldung.place(x=a, y=b)

def registrieren(): 
    def page1(nutzer): # Benutzername und Passwort eingabe
        print("Seite 1 ausführung")
    def page2(nutzer):
        print("Seite 2 ausführung")
    def page3(nutzer):
        print("Seite 3 ausführung")
    
    clearwdw()
    # Labels
    lb_1 = tk.Label(root)
    lb_2 = tk.Label(root)
    lb_3 = tk.Label(root)
    lb_4 = tk.Label(root)
    # Buttons
    bt_bestaetigen = tk.Button(root, text="Bestätigen", command="")
    bt_zurueck = tk.Button(root, text="Zurück", command=home)
    # Textfelder
    tf_feld1 = tk.Entry(root)
    tf_feld2 = tk.Entry(root)
    tf_feld3 = tk.Entry(root)
    # Sonstige Elemente
    # Hier noch Radiobutton und Combobox einfügen

# Deklaration der Variablen
nutzer = Nutzer()

# Erzeugen des Fensters
root = tk.Tk()
root.title("GameStat - Anmeldung")
root.geometry("400x500")
home()
root.mainloop()


# To-Do: Registrierung Fenster designen, Anmeldung gestalten, Begrüßung schreiben, SQL Befehle (Funktionen) einpflegen 