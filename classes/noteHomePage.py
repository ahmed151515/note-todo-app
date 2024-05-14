import tkinter as tk

root = tk.Tk()
root.title("section project")

addNoteLebel = tk.Label(root, text="Notes", font=("Arial", 16, "bold"))

todos = tk.Text(root)

buttonFrame = tk.Frame(root)

buttonAdd = tk.Button(buttonFrame, text='add')
buttonDelete = tk.Button(buttonFrame, text='delete')
buttonEdit = tk.Button(buttonFrame, text='edit')

addNoteLebel.grid(row=0,column=0,padx=10, pady=10)





buttonAdd.grid(row=0, column=0, padx=50, pady=50)
buttonDelete.grid(row=0, column=1, padx=50, pady=50)
buttonEdit.grid(row=0, column=2, padx=50, pady=50)
buttonFrame.grid(row=2, column=0, padx=10, pady=10)
todos.grid(row=1, column=0, padx=10, pady=10)
root.overrideredirect(True)
root.mainloop()
