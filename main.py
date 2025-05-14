import tkinter as tk
from tkinter import ttk
import elemente # Hier sind die Elemente im Fenster (Klöpfe und co. gespeichert)
from functools import partial
#import anmeldung # Testweise

class Testobjekt_main:
    def __init__(self):
        self.benutzer = "maxim"
        self.passwort = "1234"
        self.vorname = "Maxim"
        self.email = "maxim@gmail.com"
        self.land = "Deutschland"
        self.sprache = "deutsch"
        self.geschlecht = "Männlich"
        self.geburtsdatum = "1234"

class HauptBedienung:
    def __init__(self, root, nutzer):
        self.bn_uebersicht = ttk.Button(root, text="Übersicht", command=partial(self.uebersicht, nutzer))
        self.bn_bewertungen = ttk.Button(root, text="Bewertungen", command=1)
        self.bn_durchgespielt = ttk.Button(root, text="Durchgespielt", command=1)
        self.bn_empfohlen = ttk.Button(root, text="Empfohlene Spiele", command=1)
        self.bn_spiel_hinzufg = ttk.Button(root, text="Spiel Hinzufügen", command=1)

    def generieren(self, xstart, ystart):
        xwert = xstart
        ywert = ystart
        xadd = 0
        yadd = 25
        self.bn_uebersicht.place(x=xwert, y=ywert)
        ywert += yadd
        self.bn_bewertungen.place(x=xwert , y=ywert )
        ywert += yadd
        self.bn_durchgespielt.place(x=xwert, y=ywert)
        ywert += yadd
        self.bn_empfohlen.place(x=xwert, y=ywert)
        ywert += yadd
        self.bn_spiel_hinzufg.place(x=xwert, y=ywert)

    def uebersicht(nutzer):
        print("Übersicht")


root = tk.Tk()
root.geometry("900x700")
root.title("GameStat - Dein Spielemanager")

nutzer = Testobjekt_main()
menue_buttons = HauptBedienung(root, nutzer)
menue_buttons.generieren(50, 50)

root.mainloop()