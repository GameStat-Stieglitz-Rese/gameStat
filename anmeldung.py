import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from functools import partial # Zum ausführen von Commands in einem Tkinter Element. Syntax: partial({Funktion}, {Argument})
import objektTestAnzeige

class Nutzer(): # Diese Klasse legt bei Aufruf ein Objekt mit allen relevanten Benutzerdaten an.
    def __init__(self):
        self.nutzername = "Lester"#None
        self.passwort = "1234"#None
        self.vorname = "Lester"#None
        self.email = "lester@tester.com"#None
        self.land = "Lesterwald"#None
        self.sprache = "Lestisch"#None
        self.geschlecht = "Lestisch"#None
        self.geburtsdatum = "ll"#None

def clearwdw(): # Löscht den gesamten Inhalt eines Fensters!
    for widget in root_login.winfo_children():
        widget.destroy()

def home(nutzer):
    clearwdw()
    def anmelden_check(nutzer):
        global loggedin # Globale Variable als Rückmeldung, ob Login erfolgreich war
        nutzer.nutzername = tf_nutzername.get()
        nutzer.passwort = tf_nutzerpasswort.get()
        if nutzer.nutzername != "" and nutzer.passwort != "": # Prüfung, ob Benutzer etwas eingegeben hat
            if nutzer.nutzername == "test" and nutzer.passwort == "test":                                               # Testzweck, bitte löschen Entfernen
                messagebox.showinfo("Anmeldung", "Anmeldung erfolgreich!")                                              # Testzweck, bitte löschen Entfernen
                loggedin = True # Globale Variable als Rückmeldung, ob Login erfolgreich war
                root_login.destroy()
                objektTestAnzeige.useranzeigen(nutzer)
#  SQL          +++ +++ +++ Hier Aufruf des SQL Befehls und deklaration rueckmeldung! (Prüfung Benutzerdaten) +++ +++ +++
#            if rueckmeldung == True:
#  SQL              +++ +++ +++ Hier Aufruf des SQL Befehls! (Abrufen vollständige Benutzerdaten) +++ +++ +++
        else:
            print("Fehler: Benutzer hat nicht alle erforderlichen Daten eingegeben.")
            messagebox.showerror("Eingabefehler", "Bitte geben Sie Benutzernamen und Passwort ein.")

    # Deklaration Buttons Anmeldeseite
    bn_anmelden = tk.Button(root_login, text="Anmelden", command=partial(anmelden_check, nutzer))
    bn_abbrechen = tk.Button(root_login, text="Abbruch", command=exit, width=19)
    bn_registrieren = tk.Button(root_login, text="Registrieren", command=partial(registrieren, nutzer))

    # Deklaration Textfelder Anmeldeseite
    tf_nutzername = tk.Entry(root_login)
    tf_nutzerpasswort = tk.Entry(root_login, show="*")

    # Deklaration Labels Anmeldeseite
    lb_info = tk.Label(root_login, text="Bitte Benutzerdaten eingeben", bg="yellow")
    lb_nutzername = tk.Label(root_login, text="Benutzername:")
    lb_nutzerpasswort = tk.Label(root_login, text="Passwort:")
    lb_rueckmeldung = tk.Label(root_login, text="")

    # Startwerte / Standardwerte für die Anordnung von Objekten
    a = 60 # Startwert Objektplatzierung horizontal
    b = 100 # Startwert Objektplatzierung vertikal
    abstand = 20 # Standardwert Objektabstände
    # Eingabefelder Benutzername und Passwort Anordnung mit Label:
    lb_info.place(x=a, y=b)
    b+= abstand + 3
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
    a += 73
    bn_registrieren.place(x=a, y=b)
    a -= 73
    b += abstand
    bn_abbrechen.place(x=a, y=b)
    b += abstand
    lb_rueckmeldung.place(x=a, y=b)

    if loggedin == True:
        return True

def registrieren(nutzer):
    def page1(nutzer): # Benutzername und Passwort eingabe
        def pw_check(pw): # Prüfung auf Länge, Alpha- und Sonderzeichen, Zahlen und Länge des Passworts
            def sz(pw): # Prüfung, ob Sonderzeichen vorhanden sind
                for char in pw:
                    if not char.isalpha() and not char.isdigit(): # Ausschlussverfahren, kein Buchstabe aus Alphabet und Zahlen
                        return True
                return False
            def al(pw): # Prüfung, ob Alphazeichen vorhanden sind
                for char in pw:
                    if char.isalpha():
                        return True
                return False
            def nm(pw): # Prüfung, ob Zahlen vorhanden sind
                for char in pw:
                    if char.isdigit():
                        return True
                return False
            def pwl(pw): # Prüfung, ob Passwort mindestens 8 Zeichen lang ist
                laenge = len(pw)
                if laenge >= 8:
                    return True
                else:
                    return False

            if sz(pw) == True and al(pw) == True and nm(pw) == True and pwl(pw) == True: # Prüfung, ob alle Bedingungen (Nummer, Sonderzeichen, 8 Zeichen) erfüllt sind
                return True
            else:
                return False
            
        def checkp1(nutzer): # Prüfung, ob der Benutzer alle erforderlichen Daten eingegeben hat + Speicherung Daten.
            print("Prüfung Eingabe Seite 1")
            uname = tf_feld1.get()
            p1 = tf_feld2.get()
            p2 = tf_feld3.get()
            p_anforderung = pw_check(p1)
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
            elif p_anforderung == False:
                print("Keine Sonderzeichen oder Zahlen")
                messagebox.showwarning("Eingabe Benutzerdaten", "Für das Passwort sind Sonderzeichen und Zahlen erforderlich. Das Passwort muss 8 Zeichen lang sein!")
            elif p1 == p2 and uname != "": # Wenn Benutzername eingegeben und Passwörter übereinstimmen
                nutzer.nutzername = uname
                nutzer.passwort = p1
                print("Benutzerdaten wurden angelegt.")
                page2(nutzer)
                #return
            else: # Sonstige Fehler
                print("Fataler Fehler Benutzeranlegung")
                messagebox.showerror("Schwerwiegender Fehler", "Es ist ein Programmfehler aufgetreten.")
            
        clearwdw()
        print("Seite 1 ausführung")
        # Deklaration Labels Seite 1
        lb_1 = tk.Label(root_login, text="Bitte füllen Sie alle Felder aus", bg="yellow")
        lb_2 = tk.Label(root_login, text="Benutzername")
        lb_3 = tk.Label(root_login, text="Passwort")
        lb_4 = tk.Label(root_login, text="Passwort bestätigen")

        # Deklaration Button Seite 1
        bn_zurueck = tk.Button(root_login, text="Zurück", command=home)
        bn_weiter = tk.Button(root_login, text="Weiter", command=partial(checkp1, nutzer))

        # Deklaration Textfelder Seite 1
        tf_feld1 = tk.Entry(root_login)
        tf_feld2 = tk.Entry(root_login, show="*")
        tf_feld3 = tk.Entry(root_login, show="*")
        
        # Definition von Abständen (einheitlich)
        a = 60
        b = 100
        abstand = 20

        # Platzierung der Elemente in dem Fenster
        lb_1.place(x=a, y=b)
        b += abstand + 3
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
        def checkp2(nutzer): # Überprüfung der Benutzereingabe (vollständigkeit)
            print("Prüfung Eingabe Seite 2")
            eml = tf_feld1.get()
            gbd = tf_feld2.get()
            ges = cb_box1.get()
            #print(ges)
            if eml == "":
                print("Email Feld leer")
                messagebox.showwarning("Eingabe Benutzerdaten", "Bitte geben Sie eine E-Mail Adresse ein!")
            elif "@"  not in eml:
                print("Keine gültige E-Mail Adresse")
                messagebox.showwarning("Eingabe Benutzerdaten", "Bitte geben Sie eine richtige E-Mail Adresse ein!")
            elif gbd == "":
                print("Geburtsdatum Feld leer")
                messagebox.showwarning("Eingabe Benutzerdaten", "Bitte geben Sie ein Geburtsdatum ein!")
            elif ges == "":
                print("Geschlecht nicht ausgewählt")
                messagebox.showwarning("Eingabe Benutzerdaten", "Bitte geben Sie Ihr Geschlecht ein!")
            elif eml != "" and gbd != "" and ges != "": # Alles wurde eingegeben
                nutzer.email = eml
                nutzer.geburtsdatum = gbd
                nutzer.geschlecht = ges
                print("Benutzerdaten erfolgreich erweitert")
                page3(nutzer)
            else:
                print("Fataler Fehler Benutzeranlegung")
                messagebox.showerror("Schwerwiegender Fehler", "Es ist ein Programmfehler aufgetreten.")

        print(f"Seite 2 ausführung")
        clearwdw()
        # Deklaration Labels Seite 2
        lb_1 = tk.Label(root_login, text="Bitte füllen Sie alle Felder aus:", bg="yellow")
        lb_2 = tk.Label(root_login, text="E-Mail Adresse")
        lb_4 = tk.Label(root_login, text="Geschlecht")
        lb_3 = tk.Label(root_login, text="Geburtsdatum")

        # Deklaration Buttons Seite 2
        bn_zurueck = tk.Button(root_login, text="Zurück", command=home)
        bn_weiter = tk.Button(root_login, text="Weiter", command=partial(checkp2, nutzer))

        # Deklaration Textfelder Seite 2
        tf_feld1 = tk.Entry(root_login)
        tf_feld2 = tk.Entry(root_login)

        # Deklaration weitere Elemente Seite 2
        geschlecht = ["Männlich", "Weiblich"]
        cb_box1 = ttk.Combobox(root_login, values=geschlecht, state="readonly")
        
        # Definition von Abständen (einheitlich)
        a = 60
        b = 100
        abstand = 20

        # Platzierung der Elemente in dem Fenster
        lb_1.place(x=a, y=b)
        b += abstand + 3
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
        cb_box1.place(x=a, y=b)
        b += abstand + 10
        bn_zurueck.place(x=a, y=b)
        a += 80
        bn_weiter.place(x=a, y=b)


    def page3(nutzer): # Eingabe Land und Sprache
        def checkp3(nutzer):
            print("Prüfung Eingabe Seite 3")
            land = cb_box1.get()
            sprache = cb_box2.get()
            if land == "" or sprache == "":
                print("Eingabe fehlt")
                messagebox.showwarning("Eingabe Benutzerdaten", "Bitte geben Sie Land und Sprache ein!")
            elif land != "" and sprache != "": # Wenn alles richtig eingegeben wurde
                nutzer.land = land
                nutzer.sprache = sprache
#  SQL              +++ Hier SQL Befehl (Aufruf), der die erfassten Daten in die Datenbank einbindet und eine Rückmeldung über erfolg gibt.
#  SQL              Wenn erfolgreich, dann zurück zur Anmeldeseite, wenn nicht erfolgreich, dann zurück zur Seite 1.
                if 0 != 0: # "0" durch Variable ersetzen, die die Rückmeldung der Datenbank beinhaltet # Prüfung, ob Speicherung erfolgreich
                    print("Land und Sprache gespeichert.")
                else:
                    messagebox.showerror("Fehler Datenspeicherung", "Es gab einen Fehler bei der Speicherung Iher Daten. Bitte wiederholen Sie den Vorgang!")
                    page1(nutzer)

        print("Seite 3 ausführung")
        clearwdw()

        # Deklaration Labels Seite 3
        lb_1 = tk.Label(root_login, text="Bitte füllen Sie alle Felder aus:", bg="yellow")
        lb_2 = tk.Label(root_login, text="Land")
        lb_3 = tk.Label(root_login, text="Sprache")

        # Deklaration Buttons Seite 3
        bn_zurueck = tk.Button(root_login, text="Zurück", command=home)
        bn_weiter = tk.Button(root_login, text="Fertig", command=partial(checkp3, nutzer))

        # Deklaration weiterer Elemente Seite 3
        land = ["Deutschland", "England", "USA", "Russland", "Frankreich", "Spanien", "Polen", "Niederlande"]
        sprache = ["deutsch", "englisch", "russisch", "französisch", "spanisch", "polnisch", "niederländisch"]
        cb_box1 = ttk.Combobox(root_login, values=land, state="readonly") # state=readonly bedeutet, dass nur die eingegebenen Optionen gewählt werden können.
        cb_box2 = ttk.Combobox(root_login, value=sprache, state="readonly")
        
        # Definition von Abständen (einheitlich)
        a = 60
        b = 100
        abstand = 20

        # Platzierung der Elemente in dem Fenster
        lb_1.place(x=a, y=b)
        b += abstand + 3
        lb_2.place(x=a, y=b)
        b += abstand
        cb_box1.place(x=a, y=b)
        b += abstand
        lb_3.place(x=a, y=b)
        b += abstand
        cb_box2.place(x=a, y=b)
        b += abstand + 10
        bn_zurueck.place(x=a, y=b)
        a += 80
        bn_weiter.place(x=a, y=b)

    #clearwdw()
    page1(nutzer) # Start unmittelbar nach Aufruf der "registrieren" Funktion mit der ersten Seite.
    #page2(nutzer)
    #page3(nutzer)


root_login = tk.Tk()
root_login.title("GameStat Launcher")
root_login.geometry("280x330")
nutzer = Nutzer()

# Erzeugen des Fensters
def start():
    global loggedin
    loggedin = False # Globale Variable als Rückmeldung, ob Login erfolgreich war
    nutzer = Nutzer()
    home(nutzer) # Starten des Anmeldebildschirms (Startwert)
    root_login.mainloop()
    return nutzer, loggedin

def bypass():
    loggedin = True
    nutzer = Nutzer()
    root_login.mainloop()
    return nutzer, loggedin