import tkinter as tk
class addNote(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.root = tk.Tk()

        self.addNoteLebel = tk.Label(self.root, text="add note", font=("Arial", 16, "bold"))
        
        self.title = tk.Entry(self.root)
        self.text = tk.Text(self.root)
        self.button = tk.Button(self.root, text='add')
        
        self.addNoteLebel.pack(padx=10, pady=10)
        

        self.title.insert(0, "note title")
        self.title.pack(padx=10, pady=10)

        self.text.insert(tk.END, "note text")
        self.text.pack(padx=10, pady=10)
        
        self.button.pack(padx=10, pady=10)
