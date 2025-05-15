import tkinter as tk
from tkinter import ttk
#import elemente # Hier sind die Elemente im Fenster (Klöpfe und co. gespeichert)
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
        self.bn_uebersicht = ttk.Button(root, text="Übersicht", command=partial(uebersicht, nutzer))
        self.bn_bewertungen = ttk.Button(root, text="Bewertungen", command=partial(bewertungen, nutzer))
        self.bn_durchgespielt = ttk.Button(root, text="Durchgespielt", command=partial(durchgespielt, nutzer))
        self.bn_empfohlen = ttk.Button(root, text="Empfohlene Spiele", command=partial(empfohlen, nutzer))
        self.bn_spiel_hinzufg = ttk.Button(root, text="Spiel Hinzufügen", command=partial(spiel_hinzufg, nutzer))
        self.bn_nutzer_verwaltung = ttk.Button(root, text="Benutzer verwalten", command=partial(nutzer_verwaltung, nutzer))
        self.bn_abmeldung = tk.Button(root, text="<- Abmelden", fg="red", command=partial(abmelden, nutzer))

    def gen_bn_hauptmenue(self, xwert, ywert, lwert, xadd, yadd):
        self.bn_uebersicht.place(x=xwert, y=ywert, width=lwert)
        ywert += yadd
        self.bn_bewertungen.place(x=xwert , y=ywert, width=lwert)
        ywert += yadd
        self.bn_durchgespielt.place(x=xwert, y=ywert, width=lwert)
        ywert += yadd
        self.bn_empfohlen.place(x=xwert, y=ywert, width=lwert)
        ywert += yadd
        self.bn_spiel_hinzufg.place(x=xwert, y=ywert, width=lwert)
        ywert += yadd
        self.bn_nutzer_verwaltung.place(x=xwert, y=ywert, width=lwert)

    def gen_bn_abmelden(self, xwert, ywert, lwert):
        self.bn_abmeldung.place(x=xwert, y=ywert, width=lwert)

def clearwdw(): # Löscht den gesamten Inhalt eines Fensters!
    for widget in root.winfo_children():
        widget.destroy

def uebersicht(nutzer):
    print("Übersicht geklickt")

def bewertungen(nutzer):
    print("Bewertungen geklickt")

def durchgespielt(nutzer):
    print("Durchgespielt geklickt")

def empfohlen(nutzer):
    print("Empfohlen geklickt")

def spiel_hinzufg(nutzer):
    print("Spiel Hinzufügen geklickt")
    def gen_gui_oberflaeche():
        lb_spielname = tk.Label(root, text="Spielname")
        lb_plattform = tk.Label(root, text="Plattform")
        lb_kategorie = tk.Label(root, text="Spielgategorie")
        lb_level = tk.Label(root, text="Level")
        lb_spielzeit = tk.Label(root, text="Spielzeit (in Std.)")

def nutzer_verwaltung(nutzer):
    print("Nutzer verwalten geklickt")
    clearwdw()


def abmelden(nutzer):
    print("Abmelden gedrückt")
    

root = tk.Tk()
root.geometry("1200x800")
root.title("GameStat - Dein Spielemanager")

nutzer = Testobjekt_main()
buttons = HauptBedienung(root, nutzer)
buttons.gen_bn_hauptmenue(50, 50, 200, 0, 25) # Übergabe x,y,l
buttons.gen_bn_abmelden(50, 750, 200)
root.mainloop()