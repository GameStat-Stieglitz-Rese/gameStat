import tkinter as tk
from tkinter import ttk

# Erzeugen des Fensters (Stieglitz)
root = tk.Tk()
root.title("GameStat - Anmeldung")
root.geometry("400x500")

def registrieren(root):
    root = tk.Tk()
    root.title("Gamestat - Registrieren")
    root.geometry("500x600")
    
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
    bt_bestaetigen = tk.Button(root, text="Bestätigen", command="")

    # Einfügen von Elementen
    tf_vorname.place(x=20, y=20)
    tf_benutzername.place(x=20, y=50)

    root.mainloop()

registrieren(root)
# Elemente
bt_anmelden = tk.Button(root, text="Anmelden", command="")
bt_abbrechen = tk.Button(root, text="Abbruch", command=exit())
bt_registrieren = tk.Button(root, text="Registrieren")