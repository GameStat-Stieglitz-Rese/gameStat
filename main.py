import tkinter as tk
from tkinter import ttk
import elemente # Hier sind die Elemente im Fenster (Klöpfe und co. gespeichert)
from functools import partial
import anmeldung # Testweise


class HauptBedienung(tk.Frame):
    def __init__(self, root, user):
        self.uebersicht = ttk.Button(root, text="Übersicht", command=partial(self.uebersicht, user))
        self.bewertungen = ttk.Button(root, text="Bewertungen", command=1)
        self.durchgespielt = ttk.Button(root, text="Durchgespielt", command=1)
        self.empfohlen = ttk.Button(root, text="Empfohlene Spiele", command=1)
        self.spiel_hinzufg = ttk.Button(root, text="Spiel Hinzufügen", command=1)

    def generieren(self, xstart, ystart):
        xwert = xstart
        ywert = ystart
        xadd = 0
        yadd = 25
        self.uebersicht.place(x=xwert, y=ywert)
        ywert += yadd
        self.bewertungen.place(x=xwert , y=ywert )
        ywert += yadd
        self.durchgespielt.place(x=xwert, y=ywert)
        ywert += yadd
        self.empfohlen.place(x=xwert, y=ywert)
        ywert += yadd
        self.spiel_hinzufg.place(x=xwert, y=ywert)


root = tk.Tk()
root.geometry("900x700")
root.title("GameStat - Dein Spielemanager")

user = anmeldung.Nutzer()

menue_buttons = HauptBedienung(root, user)

menue_buttons.generieren(50, 50)

root.mainloop()