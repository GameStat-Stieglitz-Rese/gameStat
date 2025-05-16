import tkinter as tk
from tkinter import ttk
from functools import partial


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
        self.bn_abmeldung = tk.Button(root, text="<- Abmelden", fg="red", command=partial(callbacks["abmelden"], nutzer))
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
        self.bn_abmeldung.place(x=50, y=750, width=200)

    def gen_return(self):
        self.bn_return.place(x=50, y=720, width=200)


# Diese Klasse generiert ein Obkejt, in dem wichtige Labels gespeichert sind und direkt dank der Funktion generiert werden können
class HauptLabel:
    def __init__(self, root):
        self.lb_title = tk.Label(root, text="Ueberschrift", font=("Arial", 20))

    def gen_title(self, name):
        self.lb_title.config(text=name) # Ändern des Textes der Überschrift zu den übergebenen String
        self.lb_title.place(x=50, y=10)