import tkinter as tk
from tkinter import ttk
from addNote import addNote
from addTodo import addTodo
from noteHomePage import noteHomePage
from todoHomePage import todoHomePage

class MainGui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.root = tk.Tk()
        self.title("Section project")

        self.tabControl = ttk.Notebook(self.root)

        self.Note = ttk.Frame(self.tabControl)
        self.Todo = ttk.Frame(self.tabControl)

        self.tabControl.add(self.Note, text='note')
        self.tabControl.add(self.Todo, text='todo')

        self.addNote = addNote(self)
        self.addTodo = addTodo(self)
        self.noteHomePage = noteHomePage(self)
        self.todoHomePage = todoHomePage(self)

        self.addNote.pack()
        self.addTodo.pack()
        self.noteHomePage.pack()
        self.todoHomePage.pack()

        self.tabControl.pack()

if __name__ == "__main__":
    main_gui = MainGui()
    main_gui.mainloop()