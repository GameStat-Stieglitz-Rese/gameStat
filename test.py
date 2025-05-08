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

main()
root.mainloop()