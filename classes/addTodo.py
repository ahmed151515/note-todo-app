import tkinter as tk

root = tk.Tk()
root.title("section project")
root.geometry("300x200")

addTodoLebel = tk.Label(root, text="add Todo", font=("Arial", 16, "bold"))

title = tk.Entry(root)
details = tk.Entry(root)
button = tk.Button(root, text='add')

addTodoLebel.pack(padx=10, pady=10)


title.insert(0, "todo")
title.pack(padx=10, pady=10)


details.insert(tk.END, "details")
details.pack(padx=10, pady=10)

button.pack(padx=10, pady=10)
root.mainloop()
