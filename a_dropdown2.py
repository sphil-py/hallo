import tkinter as tk
from tkinter import ttk
from pathlib import Path

# ========================
# Konfiguration
# ========================
VERZEICHNIS = r"C:\Users\Sven\Qsync\MyProgram\data\gly_wb"  # Ändere diesen Pfad!
VORGABE_DATEI = "docx-start"  # Name der vorausgewählten Datei (ohne .docx)

# ========================
# Hauptfenster erstellen
# ========================
root = tk.Tk()
root.title("Wählen Sie eine .docx-Datei")
root.geometry("400x200")
root.resizable(False, False)


# ========================
# Funktion: Dropdown-Optionen laden
# ========================
def lade_dateien():
    dateien = []
    pfad = Path(VERZEICHNIS)

    # Filter: nur .docx-Dateien
    for datei in pfad.glob("*.docx"):
        name = datei.stem  # Ohne Erweiterung
        dateien.append(name)

    return sorted(dateien)


# ========================
# Funktion: Bei Auswahl
# ========================
def auf_aktualisieren(event):
    ausgewaehlt = dropdown.get()


# ========================
# Dropdown-Menü erstellen
# ========================
label = tk.Label(root, text="Wählen Sie eine Datei:", font=("Arial", 12))
label.pack(pady=20)

# Dateien laden
dateien = lade_dateien()

# Dropdown-Menü
dropdown = ttk.Combobox(root, values=dateien, font=("Arial", 12), state="readonly", width=30)
dropdown.pack(pady=10)

# Vorgabewert setzen
if VORGABE_DATEI in dateien:
    dropdown.set(VORGABE_DATEI)
else:
    if dateien:
        dropdown.set(dateien[0])  # Erste Datei als Vorgabe
    else:
        dropdown.set("Keine .docx-Dateien gefunden")

# Event-Handler für Auswahl
dropdown.bind("<<ComboboxSelected>>", auf_aktualisieren)

# ========================
# Starten
# ========================
root.mainloop()