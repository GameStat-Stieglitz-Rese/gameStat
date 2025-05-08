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
    clearwdw()   
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
    lb_reginfo = tk.Label(root, text="Bitte geben Sie hier folgende Daten ein. Beachten Sie, dass jedes Feld ausgefüllt sein muss.")
    lb_vorname = tk.Label(root, text="Vorname")
    lb_benutzername = tk.Label(root, text="Benutzername")
    lb_pw = tk.Label(root, text="Passwort")
    lb_pw_best = tk.Label(root, text="Passwort bestätigen")
    lb_email = tk.Label(root, text="E-Mail Adresse")
    lb_land = tk.Label(root, text="Land")
    lb_sprache = tk.Label(root, text="Sprache")
    lb_geschlecht = tk.Label(root, text="Geschlecht")
    lb_geburtsdatum = tk.Label(root, text="Geburtsdatum")
    bt_bestaetigen = tk.Button(root, text="Bestätigen", command="")
    bt_zurueck = tk.Button(root, text="Zurück", command=home)

    # Einfügen von Elementen
    tf_vorname.place(x=20, y=20)
    tf_benutzername.place(x=20, y=50)
    bt_zurueck.place(x=20, y=80)


# Deklaration der Variablen
nutzer = Nutzer()

# Erzeugen des Fensters
root = tk.Tk()
root.title("GameStat - Anmeldung")
root.geometry("400x500")
home()
root.mainloop()


# To-Do: Registrierung Fenster designen, Anmeldung gestalten, Begrüßung schreiben, SQL Befehle (Funktionen) einpflegen 