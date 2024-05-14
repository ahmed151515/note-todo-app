import tkinter as tk
from tkinter import messagebox
from note import Note
from addNote import addNote

class noteHomePage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.notes = tk.Listbox(self, selectmode=tk.MULTIPLE)
        self.notes.bind("<Double-Button-1>", self.on_double_click)

        for i, k in enumerate(Note.notehash.keys()):
            self.notes.insert(i, k)

        self.addNoteLabel = tk.Label(self, text="Notes", font=("Arial", 16, "bold"))

        self.buttonFrame = tk.Frame(self)

        self.buttonAdd = tk.Button(self.buttonFrame, text='add', command=self.addNote)
        self.buttonDelete = tk.Button(self.buttonFrame, text='delete', command=self.remove_item)

        self.addNoteLabel.grid(row=0, column=0, padx=10, pady=10)

        self.buttonAdd.grid(row=0, column=0, padx=50, pady=50)
        self.buttonDelete.grid(row=0, column=1, padx=50, pady=50)
        self.buttonFrame.grid(row=2, column=0, padx=10, pady=10)
        self.notes.grid(row=1, column=0, padx=10, pady=10)

    def remove_item(self):
        for i in self.notes.curselection():
            selected_title = self.notes.get(self.notes.curselection())
            del Note.notehash[selected_title]
            self.notes.delete(self.notes.curselection())

    def on_double_click(self, event):
        selected_title = self.notes.get(self.notes.curselection())

        messagebox.showinfo(f"{Note.notehash[selected_title]}",f"{Note.notehash[selected_title]}")

    def addNote(self):
        addNote()
