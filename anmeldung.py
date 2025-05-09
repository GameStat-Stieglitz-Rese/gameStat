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
    bn_registrieren = tk.Button(root, text="Registrieren", command=partial(registrieren, nutzer))
    tf_nutzername = tk.Entry(root)
    tf_nutzerpasswort = tk.Entry(root, show="*")
    lb_nutzername = tk.Label(root, text="Benutzername:")
    lb_nutzerpasswort = tk.Label(root, text="Passwort:")
    lb_rueckmeldung = tk.Label(root, text="")

    a = 75 # Startwert Objektplatzierung horizontal
    b = 50 # Startwert Objektplatzierung vertikal
    abstand = 20 # Standardwert Objektabstände
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

def registrieren(nutzer):
    def page1(nutzer): # Benutzername und Passwort eingabe
        def checkp1(nutzer): # Prüfung, ob der Benutzer alle erforderlichen Daten eingegeben hat + Speicherung Daten.
            print("Prüfung Eingabe Seite 1")
            uname = tf_feld1.get()
            p1 = tf_feld2.get()
            p2 = tf_feld3.get()
            #print(uname)
            if uname == "": # Wenn Benutzername leer ist
                print("Benutzername fehlt")
                messagebox.showwarning("Eingabe Benutzerdaten", "Bitte geben Sie auch den Benutzernamen ein!")
            elif p1 == "" or p2 == "": # Wenn ein Passwortfeld leer ist
                print("Passwörter nicht eingegeben")
                messagebox.showwarning("Eingabe Benutzerdaten", "Bitte geben Sie Ihr Passwort 2x ein!")
            elif p1 != p2: # Wenn Passwörter nicht übereinstimmen
                print("Passwort fehler")
                messagebox.showwarning("Eingabe Benutzerdaten", "Die Passwörter stimmen nicht überein!")
            elif p1 == p2 and uname != "": # Wenn Benutzername eingegeben und Passwörter übereinstimmen
                nutzer.nutzername = uname
                nutzer.passwort = p1
                print("Benutzerdaten wurden angelegt.")
                page2(nutzer)
            else: # Sonstige Fehler
                print("Fataler Fehler Benutzerdatenanlegung")
                messagebox.showwarning("Schwerwiegender Fehler", "Es ist ein Programmfehler aufgetreten.")
            
        print("Seite 1 ausführung")
        # Deklaration Label
        lb_1 = tk.Label(root, text="Bitte geben Sie Ihre gewünschten Logindaten ein")
        lb_2 = tk.Label(root, text="Benutzername")
        lb_3 = tk.Label(root, text="Passwort")
        lb_4 = tk.Label(root, text="Passwort bestätigen")

        # Deklaration Button
        bn_zurueck = tk.Button(root, text="Zurück", command=home)
        bn_weiter = tk.Button(root, text="Weiter", command=partial(checkp1, nutzer))

        # Deklaration Textfelder
        tf_feld1 = tk.Entry(root)
        tf_feld2 = tk.Entry(root, show="*")
        tf_feld3 = tk.Entry(root, show="*")
        
        # Definition von Abständen (einheitlich)
        a = 75
        b = 50
        abstand = 20

        # Platzierung der Elemente in dem Fenster
        lb_1.place(x=a, y=b)
        b += abstand
        lb_2.place(x=a, y=b)
        b += abstand
        tf_feld1.place(x=a, y=b)
        b += abstand
        lb_3.place(x=a, y=b)
        b += abstand
        tf_feld2.place(x=a, y=b)
        b += abstand
        lb_4.place(x=a, y=b)
        b += abstand
        tf_feld3.place(x=a, y=b)
        b += abstand + 10
        bn_zurueck.place(x=a, y=b)
        a += 80
        bn_weiter.place(x=a, y=b)

    def page2(nutzer): # Eingabe Name, Geschlecht, E-Mail und Geburtsdatum
        print(f"Seite 2 ausführung")
    def page3(): # Eingabe Land und Sprache
        print("Seite 3 ausführung")

    clearwdw()
    page1(nutzer)


# Deklaration der Variablen
nutzer = Nutzer()

# Erzeugen des Fensters
root = tk.Tk()
root.title("GameStat - Anmeldung")
root.geometry("400x500")
home() # Starten des Anmeldebildschirms (Startwert)
root.mainloop()