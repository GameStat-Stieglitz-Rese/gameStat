import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from functools import partial
from datetime import datetime

class Spieldaten:
    def __init__(self):
        self.eintragid = "" # Wird von der Datenbank vergeben
        self.spielid = ""
        self.benutzerid = ""
        self.plattformid = ""
        self.kategorieid = ""
        self.level = ""
        self.spielzeit = ""
        self.bewertung = ""
        self.startdatum = ""
        self.durchgespielt = "" # 1 = Ja, 2 = Nein, 3 = Keine Angabe
        self.empfohlen = "" # 1 = Ja, 2 = Nein, 3 = Keine Angabe


# Diese Klasse generiert die Hauptbedienelemente samt zugehörigen Funktionen zur Generierung vor Ort.
class HauptBedienung:
    def __init__(self, root, nutzer, callbacks):
        # Buttons Hauptmenü
        #self.callbacks = callbacks # Verzeichnis der Funktionen  (Unnötig?)
        self.bn_uebersicht = ttk.Button(root, text="Übersicht", command=partial(callbacks["uebersicht"], nutzer))
        self.bn_bewertungen = ttk.Button(root, text="Bewertungen", command=partial(callbacks["bewertungen"], nutzer))
        self.bn_durchgespielt = ttk.Button(root, text="Durchgespielt", command=partial(callbacks["durchgespielt"], nutzer))
        self.bn_empfohlen = ttk.Button(root, text="Empfohlen", command=partial(callbacks["empfohlen"], nutzer))
        self.bn_spiel_hinzufg = ttk.Button(root, text="Spielstand hinzufügen", command=partial(callbacks["spiel_hinzufg"]))
        self.bn_nutzer_verwaltung = ttk.Button(root, text="Benutzer verwalten", command=partial(callbacks["nutzer_verwaltung"], nutzer))
        self.bn_abmeldung = ttk.Button(root, text="<- Abmelden", style="Accent.TButton", command=partial(callbacks["abmelden"], nutzer))
        self.bn_return = ttk.Button(root, text="Hauptmenü", command=partial(callbacks["main"]))
        self.bn_spiel_bearbeiten = ttk.Button(root, text="Spielstand bearbeiten", command=partial(callbacks["spiel_bearbeiten"]))

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
        self.bn_spiel_bearbeiten.place(x=xwert, y=ywert, width=lwert)
        ywert += yadd
        self.bn_spiel_hinzufg.place(x=xwert, y=ywert, width=lwert)
        ywert += yadd
        self.bn_nutzer_verwaltung.place(x=xwert, y=ywert, width=lwert)

    def gen_abmelden(self): # Generierung des Abmeldebuttons (Übergabe: X-Pos, Y-Pos, Länge)
        self.bn_abmeldung.place(x=50, y=70, width=200)

    def gen_return(self):
        self.bn_return.place(x=50, y=110, width=200)


# Diese Klasse generiert ein Obkejt, in dem wichtige Labels gespeichert sind und direkt dank der Funktion generiert werden können
class HauptLabel:
    def __init__(self, root):
        self.lb_title = tk.Label(root, text="Ueberschrift", font=("Arial", 20))

    def gen_title(self, name):
        self.lb_title.config(text=name) # Ändern des Textes der Überschrift zu den übergebenen String
        self.lb_title.place(x=50, y=10)


# Klasse Generiert das Objekt, worin grundsätzlich alle Spieldaten des Nutzers Abrufbar sind. Es wird gespeichert, welche Spiele und co. vorhanden sind.
class Daten:
    def __init__(self):
        self.spiele = ["Testspiel 1", "Testspiel 2", "Testspiel 3"]
        self.kategorien = ["Testkategorie 1", "Testkategorie 2", "Testkategorie 3"]
        self.plattform = ["Testplattform 1", "Testplattform 2", "Testplattform 3"]
        self.user_spiele = [["GTA5", "PC"], ["Minecraft", "PC"]]
        

# Listen der IDs für die Datenbank
class Idlist:
    def __init__(self):
        self.laender = ["Deutschland", "England", "USA", "Russland", "Frankreich", "Spanien", "Polen", "Niederlande"]
        self.sprache = ["deutsch", "englisch", "russisch", "französisch", "spanisch", "polnisch", "niederländisch"]
        self.geschlecht = ["Männlich", "Weiblich"]
        self.herausgeber = ["Rockstar Games", "EA Games", "Ubisoft", "Valve Games", "Microsoft", "Sony",
                            "Activision Blizzard", "Epic Games", "CD Projekt", "SEGA", "BANDAI Namco", "Sonstige"]
        self.plattformen = ["Playstation 3", "Xbox 360", "PC", "Playstation 4", "Playstation 5", "Xbox One", "Xbox Serie S", "Xbox Serie X"]
        self.spiele = ["Counter Strike 2", "Call of Duty: Black Ops 6", "Need for Speed: Heat", "GTA IV", "Red Dead Redemption 2", "Bully",
                       "GTA V", "Cyberpunk 2077", "Gran Turismo 7", "Gran Turismo Sport", "Gran Turismo 6", "Forza Horizon 5", "TETRIS", "Portal 2", "Minecraft"]
        self.kategorien = ["Action", "Adventure", "Rollenspiel (RPG)", "Strategie", "Simulation", "Rennspiel", "Sport", "Denkspiel", "Open-World", "Shooter"]

 
    # Änderung der Eingaben zu dem jeweiligen Zahlenwert in der Datenbank
    def dict_laender(self, land):
        if land in self.laender:
            return self.laender.index(land) + 1
        return None
 
    def dict_sprache(self, sprache):
        if sprache in self.sprache:
            return self.sprache.index(sprache) + 1
        return None
 
    def dict_geschlecht(self, geschlecht):
        if geschlecht in self.geschlecht:
            return self.geschlecht.index(geschlecht) + 1
        return None
 
    def dict_herausgeber(self, herausgeber):
        if herausgeber in self.herausgeber:
            return self.herausgeber.index(herausgeber) + 1
        return None
    
    def dict_plattformen(self, plattformen):
        if plattformen in self.plattformen:
            return self.plattformen.index(plattformen) + 1
        return None
    
    def dict_spiele(self, spiele):
        if spiele in self.spiele:
            return self.spiele.index(spiele) + 1
        return None
    
    def dict_kategorien(self, kategorien):
        if kategorien in self.kategorien:
            return self.kategorien.index(kategorien) + 1
        return None
    

# Funktion, die eine Tabelle generiert
def tbl_spdaten(root, liste):
    #liste = [[4, "GTA5", "PC", 122, 123, 10, "2025-12-12", "Nein", "Ja"]] # Nur für Testzwecke

    # Treeview-Widget erstellen
    tree = ttk.Treeview(root, columns=("ID", "Spiel", "Plattform", "Level", "Spielzeit", "Eigenbewertung", "Startdatum", "Durchgespielt", "Empfehlung"), show="headings")

    # Spaltenüberschriften definieren
    tree.heading("ID", text="ID")
    tree.heading("Spiel", text="Spiel")
    tree.heading("Plattform", text="Plattform")
    tree.heading("Level", text="Level")
    tree.heading("Spielzeit", text="Spielzeit")
    tree.heading("Eigenbewertung", text="Eigenbewertung")
    tree.heading("Startdatum", text="Startdatum")
    tree.heading("Durchgespielt", text="Durchgespielt")
    tree.heading("Empfehlung", text="Empfehlung")

    # Spaltenbreiten
    tree.column("ID", width=7)
    tree.column("Spiel", width=100)
    tree.column("Plattform", width=100)
    tree.column("Level", width=50)
    tree.column("Spielzeit", width=55)
    tree.column("Eigenbewertung", width=100)
    tree.column("Startdatum", width=100)
    tree.column("Durchgespielt", width=100)
    tree.column("Empfehlung", width=100)

    # Daten einfügen
    for eintrag in liste:
        tree.insert("", "end", values=eintrag)

    tree.place(x=350, y=70)


# liste = 0
# root = tk.Tk()
# root.title("Test")
# root.geometry("1000x1000")
# tbl_spdaten(root, liste)
# root.mainloop()