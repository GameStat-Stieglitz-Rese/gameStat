import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

todos = []

def update_listbox():
    listbox.delete(0, tk.END)
    for eingabe in todos:
        listbox.insert(tk.END, eingabe)

def addTask():
    eingabe = entry.get()
    if eingabe:
        todos.append(eingabe)
        update_listbox()
        entry.delete(0, tk.END)
        # listbox.insert(tk.END, eingabe)
    else:
        messagebox.showerror("Eingabefeld leer", "Bitte geben Sie eine Aufgabe ein!")
    # listbox.delete(0, tk.END)

def removeTask():
    print("removeTask")
    cursor = listbox.curselection()[0]
    print(cursor)
    todos.pop(cursor)
    update_listbox()

def clearList():
    print("clearList")
    #listbox.delete(0, tk.END)
    todos.clear()
    update_listbox()

# Fenster erzeugen
root = tk.Tk()
root.title("ToDo App von Marc")
root.geometry("400x500")

# Eingabefeld
entry = tk.Entry(root)

# Hinzufügen add Button
bt_add = tk.Button(root, text="Hinzufügen", command=addTask)

# Hinzufügen bt_remove
bt_remove = tk.Button(root, text="Erledigt / Entfernen", command=removeTask)

# Hinzufügen bt_clear
bt_clear = tk.Button(root, text="Zurücksetzen", command=clearList)

# Listbox
listbox = tk.Listbox(root)
listbox.insert(tk.END, todos)

entry.pack()
bt_add.pack()
listbox.pack()
bt_remove.pack()
bt_clear.pack()

root.mainloop()