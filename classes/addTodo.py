import tkinter as tk

class addTodo(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # self.root = tk.Tk()


        self.addTodoLebel = tk.Label(self, text="add Todo", font=("Arial", 16, "bold"))

        self.title = tk.Entry(self)
        self.details = tk.Entry(self)
        self.button = tk.Button(self, text='add')

        self.addTodoLebel.pack(padx=10, pady=10)


        self.title.insert(0, "todo")
        self.title.pack(padx=10, pady=10)


        self.details.insert(tk.END, "details")
        self.details.pack(padx=10, pady=10)

        self.button.pack(padx=10, pady=10)

