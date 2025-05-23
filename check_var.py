import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Prüfung, ob der Übergebene Wert mit der Anforderung übereinstimmt. Falls nicht, wird direkt auch eine Fehlermeldung ausgegeben.

def check_int(wert, name, erforderlich): # Prüft ob Eingabe ein Intager ist
    if erforderlich == True and wert == "":
        messagebox.showerror("Fehlende Eingabe", f"Das Feld {name} ist ein Pflichtfeld!")
        return False    
    elif erforderlich == True or wert != "":
        if wert.isdigit() == False:
            messagebox.showerror("Falsche Eingabe", f"Bitte geben sie in dem Feld {name} nur Ganzzahlen ein.")
            return False
        else:
            return True
    else:
        return True
    
def check_str(wert, name, erforderlich): # Prüft ob die Eingabe ein String ist
    if erforderlich == True and wert == "":
        messagebox.showerror("Fehlende Eingabe", f"Das Feld {name} ist ein Pflichtfeld!")
        return False
    elif erforderlich == True or wert != "":
        for a in wert:
            if a.isalpha() == False:
                messagebox.showerror("Falsche Eingabe", f"Bitte geben Sie in dem Feld {name} nur Buchstaben ein.")
                return False
        return True
    else:
        return True

def check_range(wert, startrange, lastrange, name, erforderlich): # Prüft, ob der angegebene Zahlenbereich eingehalten wurde
    if erforderlich == True and wert == "":
        messagebox.showerror("Fehlende Eingabe", f"Das Feld {name} ist ein Pflichtfeld!")
        return False
    elif erforderlich == True or wert != "":
        if wert.isdigit():    
            wert = int(wert)
            if wert >= startrange and wert <= lastrange:
                return True
            else:
                messagebox.showerror("Ungültiger Bereich", f"Bitte geben Sie in dem Feld {name} einen Wert zwischen {startrange} und {lastrange}")
                return False
        else:
            messagebox.showerror("Falsche Eingabe", f"Bitte geben Sie in dem Feld {name} eine Zahl ein.")
            return False
    else:
        return True
    
def check_datum(datum_str, name, erforderlich): # Prüft, ob die Eingaabe dem amerikanischen Datumsformat entspricht
    if erforderlich == True and datum_str == "":
        messagebox.showerror("Fehlende Eingabe", f"Das Feld {name} ist ein Pflichtfeld!")
        return False
    elif erforderlich == True or datum_str != "":
        try:
            datetime.strptime(datum_str, "%Y-%m-%d")
            return True
        except ValueError:
            messagebox.showerror("Falsche Eingabe", f"Bitte geben Sie in dem Feld {name} ein Datum im Format JJJJ-MM-DD ein.")
            return False
    else:
        return True