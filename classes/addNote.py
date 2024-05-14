import tkinter as tk

root = tk.Tk()
root.title("section project")

addNoteLebel = tk.Label(root, text="add note", font=("Arial", 16, "bold"))

title = tk.Entry(root)
text = tk.Text(root)
button = tk.Button(root, text='add')

addNoteLebel.pack(padx=10, pady=10)

# Set default text for title Entry widget
title.insert(0, "note title")
title.pack(padx=10, pady=10)

# Set default text for text Text widget
text.insert(tk.END, "note text")
text.pack(padx=10, pady=10)

button.pack(padx=10, pady=10)
root.mainloop()
