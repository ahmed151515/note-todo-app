import tkinter as tk
from tkinter import ttk
from addNote import addNote
from noteHomePage import noteHomePage
from todoHomePage import todoHomePage
from note import Note
from todo import Todo

class MainGui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Section project")

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.tabControl = ttk.Notebook(self)

        self.Note = noteHomePage(self.tabControl)
        self.Todo = todoHomePage(self.tabControl)

        self.tabControl.add(self.Note, text='note')
        self.tabControl.add(self.Todo, text='todo')
        self.tabControl.grid()
        # self.addNote = addNote(self)
        # self.addTodo = addTodo(self)
        # self.noteHomePage = noteHomePage(self)
        # self.todoHomePage = todoHomePage(self)

        # self.addNote.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        # self.addTodo.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        # self.noteHomePage.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        # self.todoHomePage.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        #
        # self.tabControl.pack()

    def on_closing(self):
        Note.save()
        Todo.save()
        self.destroy()



if __name__ == "__main__":
    main_gui = MainGui()
    main_gui.mainloop()