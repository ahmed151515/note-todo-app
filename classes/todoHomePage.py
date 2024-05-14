import tkinter as tk
from tkinter import messagebox
from todo import Todo
from addTodo import addtodo


class todoHomePage(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.addNoteLebel = tk.Label(
            self, text="Todo List", font=("Arial", 16, "bold"))

        todoHomePage.todos = tk.Listbox(self)

        for i, k in enumerate(Todo.todohash.keys()):
            todoHomePage.todos.insert(i, k)
        todoHomePage.todos.bind("<Double-Button-1>", self.on_double_click)
        self.buttonFrame = tk.Frame(self)

        self.buttonAdd = tk.Button(
            self.buttonFrame, text='add', command=self.add_todo)
        self.buttonDelete = tk.Button(
            self.buttonFrame, text='delete', command=todoHomePage.delete)
        self.buttonEdit = tk.Button(
            self.buttonFrame, text='one task mode', command=self.one_task)

        self.addNoteLebel.grid(row=0, column=0, padx=10, pady=10)

        self.buttonAdd.grid(row=0, column=0, padx=50, pady=50)
        self.buttonDelete.grid(row=0, column=1, padx=50, pady=50)
        self.buttonEdit.grid(row=0, column=2, padx=50, pady=50)
        self.buttonFrame.grid(row=2, column=0, padx=10, pady=10)
        todoHomePage.todos.grid(row=1, column=0, padx=10, pady=10)

    def add_todo(self):
        self.add = addtodo()

    @classmethod
    def ref(cls, title):
        todoHomePage.todos.insert(tk.END, title)

    @classmethod
    def delete(cls):

        selected_title = todoHomePage.todos.get(
            todoHomePage.todos.curselection())
        del Todo.todohash[selected_title]
        todoHomePage.todos.delete(todoHomePage.todos.curselection())

    def on_double_click(self, event):
        selected_title = todoHomePage.todos.get(
            todoHomePage.todos.curselection())

        messagebox.showinfo(message=f"{Todo.todohash[selected_title]}")

    def one_task(self):
        if len(Todo.todohash) != len(Todo.todolist):
            Todo.convert_dict_to_list()
        todoHomePage.one = tk.Toplevel()
        tk.Checkbutton(todoHomePage.one, text=f"{
                       Todo.todolist[0].title}", command=self.pop, font=("Arial", 40)).grid()
        tk.Label(todoHomePage.one, text=f"{
                 Todo.todolist[0].describ}", font=("Arial", 40)).grid()

    def pop(self):
        tmp = Todo.todolist.pop(0)
        del Todo.todohash[tmp.title]
        todoHomePage.one.destroy()
        self.one_task()
