import tkinter as tk
from todo import Todo
from addTodo import addTodo


class todoHomePage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.addNoteLebel = tk.Label(
            self, text="Todo List", font=("Arial", 16, "bold"))

        self.todos = tk.Listbox(self)
        for i, k in enumerate(Todo.todohash.keys()):
            self.todos.insert(i, k)

        self.buttonFrame = tk.Frame(self)

        self.buttonAdd = tk.Button(
            self.buttonFrame, text='add', command=self.add_todo)
        self.buttonDelete = tk.Button(self.buttonFrame, text='delete')
        self.buttonEdit = tk.Button(self.buttonFrame, text='one task mode')

        self.addNoteLebel.grid(row=0, column=0, padx=10, pady=10)

        self.buttonAdd.grid(row=0, column=0, padx=50, pady=50)
        self.buttonDelete.grid(row=0, column=1, padx=50, pady=50)
        self.buttonEdit.grid(row=0, column=2, padx=50, pady=50)
        self.buttonFrame.grid(row=2, column=0, padx=10, pady=10)
        self.todos.grid(row=1, column=0, padx=10, pady=10)

    def add_todo(self):
        addTodo()
    @classmethod 
    def refrch(cls):
        
