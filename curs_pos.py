import tkinter as tk

root = tk.Tk()
root.title("Cursor bleibt an letzter Position")

entry = tk.Entry(root, font=("Arial", 14), width=30)
entry.pack(pady=20)

def create_filter_func(i):
    def filter_func(event):
        # Hier deine Filterlogik
        print(f"Filter für Index {i} aktiviert: {event.widget.get()}")

        # ✅ Cursor an die letzte aktuelle Position setzen
        current_pos = event.widget.index(tk.INSERT)  # Aktuelle Cursorposition
        event.widget.icursor(current_pos)           # Cursor an diese Position setzen
        event.widget.focus()                        # Fokus sicherstellen

    return filter_func

# Bindung: Bei jedem Tastenloslassen
entry.bind('<KeyRelease>', create_filter_func(0))

root.mainloop()