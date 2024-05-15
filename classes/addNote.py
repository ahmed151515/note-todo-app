import tkinter as tk
from note import Note

class addNote(tk.Toplevel):
    def __init__(self):
        super().__init__()

        # self.root = tk.Tk()
        self.title_var = tk.StringVar()
        self.text_var = tk.StringVar()

        self.addNoteLebel = tk.Label(self, text="add note", font=("Arial", 16, "bold"))

        self.title = tk.Entry(self)
        self.text = tk.Text(self)
        self.button = tk.Button(self, text='add', command = self.add_getter)

        self.addNoteLebel.pack(padx=10, pady=10)


        self.title.insert(0, "note title")
        self.title.pack(padx=10, pady=10)

        self.text.insert(tk.END, "note text")
        self.text.pack(padx=10, pady=10)

        self.button.pack(padx=10, pady=10)

    def add_getter(self):
        Ntitle = self.title.get()
        Ntext = self.text.get(1.0, "end-1c" )
        Note.notehash[Ntitle] = Ntext
        Note.save()
        self.destroy()
