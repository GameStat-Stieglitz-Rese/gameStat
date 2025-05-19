import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from functools import partial
from datetime import datetime


# Diese Klasse generiert die Hauptbedienelemente samt zugehörigen Funktionen zur Generierung vor Ort.
class HauptBedienung:
    def __init__(self, root, nutzer, callbacks):
        # Buttons Hauptmenü
        #self.callbacks = callbacks # Verzeichnis der Funktionen  (Unnötig?)
        self.bn_uebersicht = ttk.Button(root, text="Übersicht", command=partial(callbacks["uebersicht"], nutzer))
        self.bn_bewertungen = ttk.Button(root, text="Bewertungen", command=partial(callbacks["bewertungen"], nutzer))
        self.bn_durchgespielt = ttk.Button(root, text="Durchgespielt", command=partial(callbacks["durchgespielt"], nutzer))
        self.bn_empfohlen = ttk.Button(root, text="Empfohlen", command=partial(callbacks["empfohlen"], nutzer))
        self.bn_spiel_hinzufg = ttk.Button(root, text="Spiel hinzufügen", command=partial(callbacks["spiel_hinzufg"], nutzer))
        self.bn_nutzer_verwaltung = ttk.Button(root, text="Benutzer verwalten", command=partial(callbacks["nutzer_verwaltung"], nutzer))
        self.bn_abmeldung = ttk.Button(root, text="<- Abmelden", style="Accent.TButton", command=partial(callbacks["abmelden"], nutzer))
        self.bn_return = ttk.Button(root, text="Hauptmenü", command=partial(callbacks["main"], nutzer))
        self.bn_spiel_bearbeiten = ttk.Button(root, text="Spiel bearbeiten", command=partial(callbacks["spiel_bearbeiten"], nutzer))

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


class Check:
    def __init__(self):
        self.here = None

    def intager(self, wert, name): # Prüft ob Eingabe ein Intager ist
        if isinstance(wert, int) == False:
            messagebox.showinfo("Falsche Eingabe", f"Bitte geben Sie in dem Feld {name} nur Zahlen ein.")
            return False
        else:
            return True
    
    def string(self, wert, name): # Prüft ob die Eingabe ein String ist
        for a in wert:
            if a.isalpha() == False:
                messagebox.showinfo("Falsche Eingabe", f"Bitte geben Sie in dem Feld {name} nur Buchstaben ein.")
                return False
        return True
    
    def rang(self, wert, startrange, lastrange, name): # Prüft, ob der angegebene Zahlenbereich eingehalten wurde
        wert = int(wert)
        if wert >= startrange and wert <= lastrange:
            return True
        else:
            messagebox.showinfo("Falsche eingabe", f"Bitte geben Sie in dem Feld {name} einen Wert zwischen {startrange} und {lastrange}")
            return False
        
    def datum(self, datum_str, name):
        try:
            datetime.strptime(datum_str, "%Y-%m-%d")
            return True
        except ValueError:
            messagebox.showinfo("Falsche Eingabe", f"Bitte geben Sie in dem Feld {name} ein Datum im Format JJJJ-MM-DD ein.")
            return False