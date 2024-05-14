import tkinter as tk
from note import Note
from addNote import addNote

class noteHomePage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # self.root = tk.Tk()

        self.addNoteLebel = tk.Label(self, text="Notes", font=("Arial", 16, "bold"))

        self.notes = tk.Listbox(self)

        self.buttonFrame = tk.Frame(self)

        self.buttonAdd = tk.Button(self.buttonFrame, text='add', command=self.addNote)
        self.buttonDelete = tk.Button(self.buttonFrame, text='delete')
        self.buttonEdit = tk.Button(self.buttonFrame, text='edit')

        self.addNoteLebel.grid(row=0,column=0,padx=10, pady=10)

        self.buttonAdd.grid(row=0, column=0, padx=50, pady=50)
        self.buttonDelete.grid(row=0, column=1, padx=50, pady=50)
        self.buttonEdit.grid(row=0, column=2, padx=50, pady=50)
        self.buttonFrame.grid(row=2, column=0, padx=10, pady=10)
        self.notes.grid(row=1, column=0, padx=10, pady=10)

    def addNote(self):
        addNote()