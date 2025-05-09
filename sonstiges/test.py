import tkinter as tk
from tkinter import ttk

# Erzeugen des Fensters (Stieglitz)
root = tk.Tk()
root.title("GameStat - Anmeldung")
root.geometry("400x500")

def clearnwdw():
    for widget in root.winfo_children():
        widget.destroy()

def registrieren():
    clearnwdw()
    tf_test = tk.Entry(root)
    tf_abbruch = tk.Button(root, text="Abbruch", command=main)

    tf_test.pack()
    tf_abbruch.pack()
    #root.mainloop()

def main():
    clearnwdw()
    bt_anmelden = tk.Button(root, text="Anmelden", command=registrieren)
    bt_abbrechen = tk.Button(root, text="Abbruch", command=exit)
    bt_registrieren = tk.Button(root, text="Registrieren")
    bt_test = tk.Button(root, text="Hallo")

    bt_anmelden.pack()
    bt_abbrechen.pack()
# Elemente


#root.mainloop()





# Ausgelagert (Archiv). Ausgelagert, da Funktion nun anders bearbeitet wird (Nicht mehr ein einziges Formular, sondern mehrere Seiten.)

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


lb_land = tk.Label(root, text="AAA")
lb_land.text = "ABC"


print(lb_land.text)