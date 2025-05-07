import tkinter as tk
from tkinter import ttk

def registrieren():
    root_register = tk.Tk()
    root_register.title("Gamestat - Registrieren")
    root_register.geometry("500x600")
    
    # Registrieren GUI Elemente (tf = Textfeld)
    tf_vorname = tk.Entry(root_register)
    tf_benutzername = tk.Entry(root_register)
    tf_pw = tk.Entry(root_register)
    tf_pw_best = tk.Entry(root_register)
    tf_email = tk.Entry(root_register)
    tf_land = tk.Entry(root_register)
    tf_sprache = tk.Entry(root_register)
    # Geschlecht in Klärung!
    tf_geburtsdatum = tk.Entry(root_register)
    bt_bestaetigen = tk.Button(root_register, text="Bestätigen", command="")

    # Einfügen von Elementen
    tf_vorname.place(x=20, y=20)
    tf_benutzername.place(x=20, y=50)

    root_register.mainloop()

registrieren()


# import tkinter as tk

# root = tk.Tk()
# tk.Label(root, text="Name:").grid(row=0, column=0)
# tk.Entry(root).grid(row=0, column=1)
# tk.Button(root, text="Absenden").grid(row=1, column=0, columnspan=2)
# root.mainloop()




# import tkinter as tk

# root = tk.Tk()
# button = tk.Button(root, text="Exakt platziert")
# button.place(x=50, y=100)  # Position in Pixeln
# root.mainloop()