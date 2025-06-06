import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from functools import partial # Zum ausführen von Commands in einem Tkinter Element. Syntax: partial({Funktion}, {Argument})
import test_objektTestAnzeige
import z_Anmeldung_SQL
import z_Registrierung_SQL
from PIL import Image, ImageTk
import elemente
import hashlib
import check_var
import os
import sys

class Nutzer(): # Diese Klasse legt bei Aufruf ein Objekt mit allen relevanten Benutzerdaten an.
    def __init__(self):
        self.id = ""
        self.nutzername = None
        self.passwort = None
        self.vorname = None
        self.email = None
        self.land = None
        self.sprache = None
        self.geschlecht = None
        self.geburtsdatum = None

def logo_place():
    lb_logo.place(x=27, y=-55)

def clearwdw(): # Löscht den gesamten Inhalt eines Fensters!
        for widget in root_login.winfo_children():
            widget.place_forget()

def home():
    clearwdw()
    def anmelden_check(nutzer):
        global loggedin # Globale Variable als Rückmeldung, ob Login erfolgreich war
        nutzername = tf_nutzername.get()
        passwort = tf_nutzerpasswort.get()

        # Prüfung, ob der Nutzer einen SQL Befehl eingegeben hat.
        if check_var.check_sqlblock(nutzername, "Nutzername") == False:
            return
        if check_var.check_sqlblock(passwort, "Passwort") == False:
            return
        
        nutzer.nutzername = nutzername
        nutzer.passwort = hashlib.sha256(passwort.encode()).hexdigest()

        if nutzer.nutzername != "" and nutzer.passwort != "": # Prüfung, ob Benutzer etwas eingegeben hat
            rm_anmeldung, nutzer = z_Anmeldung_SQL.nutzer_anmelden(nutzer)
            if rm_anmeldung == 0:
                loggedin = True # Globale Variable als Rückmeldung, ob Login erfolgreich war
                root_login.destroy()
                #test_objektTestAnzeige.useranzeigen(nutzer) # Für Test, aktivieren, wenn Nutzerdaten in Konsole Printen
            elif rm_anmeldung == 1:
                print("Login nicht ok")
                messagebox.showwarning("Anmeldung", "Die Logindaten waren ungültig. Bitte wiederholen.")
                home()
            else:
                print("MariaDB Fehler")
                messagebox.showerror("Störung MariaDB", "Es besteht ein Problem mit der Datenbank.")
                home()
        else:
            print("Fehler: Benutzer hat nicht alle erforderlichen Daten eingegeben.")
            messagebox.showerror("Eingabefehler", "Bitte geben Sie Benutzernamen und Passwort ein.")

    # Deklaration Buttons Anmeldeseite
    bn_anmelden = tk.Button(root_login, text="Anmelden", command=partial(anmelden_check, nutzer), bg="aqua")
    bn_abbrechen = tk.Button(root_login, text="Abbruch", command=sys.exit, width=19)
    bn_registrieren = tk.Button(root_login, text="Registrieren", command=partial(registrieren, nutzer))

    # Deklaration Textfelder Anmeldeseite
    tf_nutzername = tk.Entry(root_login, width=23)
    tf_nutzerpasswort = tk.Entry(root_login, show="*", width=23)

    # Deklaration Labels Anmeldeseite
    #lb_info = tk.Label(root_login, text="Bitte Benutzerdaten eingeben", fg="azure")
    lb_nutzername = tk.Label(root_login, text="Benutzername")
    lb_nutzerpasswort = tk.Label(root_login, text="Passwort")
    lb_rueckmeldung = tk.Label(root_login, text="")

    # Startwerte / Standardwerte für die Anordnung von Objekten
    a = 60 # Startwert Objektplatzierung horizontal
    b = 100 # Startwert Objektplatzierung vertikal
    abstand = 21 # Standardwert Objektabstände
    # Eingabefelder Benutzername und Passwort Anordnung mit Label:
    
    # Startseite generieren / Elemente platzieren
    logo_place()
    #lb_info.place(x=a, y=b)
    b+= abstand + 3
    lb_nutzername.place(x=a, y=b)
    b += abstand
    tf_nutzername.place(x=a, y=b)
    b += abstand
    lb_nutzerpasswort.place(x=a, y=b)
    b += abstand
    tf_nutzerpasswort.place(x=a, y=b)
    b = b + abstand + 20 # Abschluss mit zusätzlichem Abstand
    
    abstand = 30
    # Buttons Anordnung:
    bn_anmelden.place(x=a, y=b)
    #b += abstand
    a += 71
    bn_registrieren.place(x=a, y=b)
    a -= 71
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

            # Prüfung, ob Nutzer einen SQL Befehl eingegeben hat
            if check_var.check_sqlblock(uname, "Benutzername") == False:
                return
            if check_var.check_sqlblock(p1, "Passwort") == False: # P2 test unnötig, da p1 = p2 sein muss und fehler ausgelöst wird.
                return

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
                nutzer.passwort = hashlib.sha256(p1.encode()).hexdigest()
                print("Benutzerdaten wurden angelegt.")
                page2(nutzer)
                #return
            else: # Sonstige Fehler
                print("Fataler Fehler Benutzeranlegung")
                messagebox.showerror("Schwerwiegender Fehler", "Es ist ein Programmfehler aufgetreten.")
            
        clearwdw()
        print("Seite 1 ausführung")
        # Deklaration Labels Seite 1
        lb_1 = tk.Label(root_login, text="Neuen Benutzer anlegen")
        lb_2 = tk.Label(root_login, text="Benutzername")
        lb_3 = tk.Label(root_login, text="Passwort")
        lb_4 = tk.Label(root_login, text="Passwort bestätigen")

        # Deklaration Button Seite 1
        bn_zurueck = tk.Button(root_login, text="Zurück", command=home, width=8)
        bn_weiter = tk.Button(root_login, text="Weiter", command=partial(checkp1, nutzer), width=8)

        # Deklaration Textfelder Seite 1
        tf_feld1 = tk.Entry(root_login, width=23)
        tf_feld2 = tk.Entry(root_login, show="*", width=23)
        tf_feld3 = tk.Entry(root_login, show="*", width=23)
        
        # Definition von Abständen (einheitlich)
        a = 60
        b = 100
        abstand = 21

        # Platzierung der Elemente in dem Fenster
        logo_place()
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
        a += 76
        bn_weiter.place(x=a, y=b)

    def page2(nutzer): # Eingabe Name, Geschlecht, E-Mail und Geburtsdatum
        def checkp2(nutzer): # Überprüfung der Benutzereingabe (vollständigkeit)
            print("Prüfung Eingabe Seite 2")
            eml = tf_feld1.get()
            gbd = tf_feld2.get()
            ges = cb_box1.get()

            # Prüft, ob Nutzer einen SQL Befehl eingegeben hat
            if check_var.check_sqlblock(eml, "E-Mail") == False:
                return
            if check_var.check_sqlblock(gbd, "Geburtsdatum") == False:
                return

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
                rm_gbd = check_var.check_datum(gbd, "Geburtsdatum", True)
                if rm_gbd:
                    nutzer.email = eml
                    nutzer.geburtsdatum = gbd
                    nutzer.geschlecht = idlist.dict_geschlecht(ges)
                    print("Benutzerdaten erfolgreich erweitert")
                    page3(nutzer)

            else:
                print("Fataler Fehler Benutzeranlegung")
                messagebox.showerror("Schwerwiegender Fehler", "Es ist ein Programmfehler aufgetreten.")

        print(f"Seite 2 ausführung")
        clearwdw()
        # Deklaration Labels Seite 2
        lb_1 = tk.Label(root_login, text="Neuen Benutzer anlegen")
        lb_2 = tk.Label(root_login, text="E-Mail Adresse")
        lb_4 = tk.Label(root_login, text="Geschlecht")
        lb_3 = tk.Label(root_login, text="Geburtsdatum (JJJJ-MM-TT)")

        # Deklaration Buttons Seite 2
        bn_zurueck = tk.Button(root_login, text="Zurück", command=home, width=8)
        bn_weiter = tk.Button(root_login, text="Weiter", command=partial(checkp2, nutzer), width=8)

        # Deklaration Textfelder Seite 2
        tf_feld1 = tk.Entry(root_login, width=23)
        tf_feld2 = tk.Entry(root_login, width=23)

        # Deklaration weitere Elemente Seite 2
        cb_box1 = ttk.Combobox(root_login, values=idlist.geschlecht, state="readonly")
        
        # Definition von Abständen (einheitlich)
        a = 60
        b = 100
        abstand = 21

        # Platzierung der Elemente in dem Fenster
        logo_place()
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
        a += 76
        bn_weiter.place(x=a, y=b)


    def page3(nutzer): # Eingabe Land und Sprache
        def checkp3(nutzer):
            print("Prüfung Eingabe Seite 3")
            land = cb_box1.get()
            sprache = cb_box2.get()
            vname = tf_1.get()

            # Prüfung, ob Nutzer einen SQL Befehl eingegeben hat
            if check_var.check_sqlblock(vname, "Vorname") == False:
                return

            if land == "" or sprache == "" or vname == "":
                print("Eingabe fehlt")
                messagebox.showwarning("Eingabe Benutzerdaten", "Bitte geben Sie Vorname, Land und Sprache ein!")
            elif land != "" and sprache != "" and vname != "": # Wenn alles richtig eingegeben wurde
                nutzer.vorname = vname
                nutzer.land = idlist.dict_laender(land)
                nutzer.sprache = idlist.dict_sprache(sprache)
                rm_registrierung = z_Registrierung_SQL.registrieren_ausfuehren(nutzer)
                if rm_registrierung:
                    print("Registrierung erfolgreich.")
                    messagebox.showinfo("Registrierung", "Die Registrierung war erfolgreich. Sie gelangen nun zur Anmeldung.")
                    home()
                else:
                    messagebox.showerror("Fehler Datenspeicherung", "Es gab einen Fehler bei der Speicherung Iher Daten. Bitte wiederholen Sie den Vorgang!")
                    page1(nutzer)

        print("Seite 3 ausführung")
        clearwdw()

        # Deklaration Labels Seite 3
        lb_1 = tk.Label(root_login, text="Neuen Benutzer anlegen")
        lb_2 = tk.Label(root_login, text="Land")
        lb_3 = tk.Label(root_login, text="Sprache")
        lb_4 = tk.Label(root_login, text="Vorname")

        # Deklaration Buttons Seite 3
        bn_zurueck = tk.Button(root_login, text="Zurück", command=home, width=8)
        bn_weiter = tk.Button(root_login, text="Fertig", command=partial(checkp3, nutzer), width=8)

        # Deklaration weiterer Elemente Seite 3
        tf_1 = tk.Entry(root_login, width=23)
        cb_box1 = ttk.Combobox(root_login, values=idlist.laender, state="readonly") # state=readonly bedeutet, dass nur die eingegebenen Optionen gewählt werden können.
        cb_box2 = ttk.Combobox(root_login, value=idlist.sprache, state="readonly")
        
        # Definition von Abständen (einheitlich)
        a = 60
        b = 100
        abstand = 21

        # Platzierung der Elemente in dem Fenster
        logo_place()
        lb_1.place(x=a, y=b)
        b += abstand + 3
        lb_4.place(x=a, y=b)
        b += abstand
        tf_1.place(x=a, y=b)
        b += abstand
        lb_2.place(x=a, y=b)
        b += abstand
        cb_box1.place(x=a, y=b)
        b += abstand
        lb_3.place(x=a, y=b)
        b += abstand
        cb_box2.place(x=a, y=b)
        b += abstand + 10
        bn_zurueck.place(x=a, y=b)
        a += 76
        bn_weiter.place(x=a, y=b)

    #clearwdw()
    page1(nutzer) # Start unmittelbar nach Aufruf der "registrieren" Funktion mit der ersten Seite.

# Deklaration Pfad für Medien
pic_logo = os.path.join(os.path.dirname(__file__), "images", "logo.png")

root_login = tk.Tk()
root_login.title("GameStat Launcher")
root_login.geometry("280x330")
nutzer = Nutzer()
idlist = elemente.Idlist()
#check_var = elemente.Check()

# Erzeugen des Fensters
def start():
    global loggedin, nutzer, lb_logo # Macht folgende Variablen auf gesamtem Skript nutzbar.
    loggedin = False # Globale Variable als Rückmeldung, ob Login erfolgreich war
    nutzer = Nutzer()
    new_logo = Image.open(pic_logo) # Deklaration des Programmlogos
    skal_logo = new_logo.resize((200, 200))
    img1_logo = ImageTk.PhotoImage(skal_logo)
    lb_logo = tk.Label(root_login, image=img1_logo)
    home() # Starten des Anmeldebildschirms (Startwert)
    root_login.mainloop()
    return nutzer, loggedin

def bypass():
    loggedin = True
    nutzer = Nutzer()
    root_login.mainloop()
    return nutzer, loggedin