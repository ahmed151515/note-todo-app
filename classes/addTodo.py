import tkinter as tk
from todo import Todo


class addtodo(tk.Toplevel):

    def __init__(self, ):
        super().__init__()
        # self.root = tk.Tk()

        self.addTodoLebel = tk.Label(
            self, text="add Todo", font=("Arial", 16, "bold"))

        self.title = tk.Entry(self)
        self.descraibe = tk.Entry(self)
        self.button = tk.Button(self, text='add', command=self.add_todo)

        self.addTodoLebel.pack(padx=10, pady=10)

        self.title.insert(0, "todo")
        self.title.pack(padx=10, pady=10)

        self.descraibe.insert(tk.END, "descraibe")
        self.descraibe.pack(padx=10, pady=10)

        self.button.pack(padx=10, pady=10)

    def add_todo(self):
        from todoHomePage import todoHomePage

        Todo.todohash[self.title.get()] = self.descraibe.get()
        todoHomePage.ref(self.title.get())
        self.destroy()