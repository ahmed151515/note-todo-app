import tkinter as tk
from tkinter import messagebox
from note import Note
from addNote import addNote

class noteHomePage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.notes = tk.Listbox(self)
        self.notes.bind("<Double-Button-1>", self.on_double_click)

        for i, k in enumerate(Note.notehash.keys()):
            self.notes.insert(i, k)

        self.addNoteLabel = tk.Label(self, text="Notes", font=("Arial", 16, "bold"))

        self.buttonFrame = tk.Frame(self)

        self.buttonDelete = tk.Button(self.buttonFrame, text='delete', command=self.remove_item)
        self.buttonAdd = tk.Button(self.buttonFrame, text='add', command=self.addNote)
        self.buttonSearch = tk.Button(self.buttonFrame, text='search', command=self.search_item)

        self.addNoteLabel.grid(row=0, column=0, padx=10, pady=10)
        self.buttonAdd.grid(row=0, column=0, padx=50, pady=50)
        self.buttonSearch.grid(row=0, column=1, padx=50, pady=50)
        self.buttonDelete.grid(row=0, column=2, padx=50, pady=50)
        self.buttonFrame.grid(row=2, column=0, padx=10, pady=10)
        self.notes.grid(row=1, column=0, padx=10, pady=10)

        # self.update_notes_list()

    def update_notes_list(self):
        self.notes.delete(0, tk.END)  # Clear the listbox
        for i, k in enumerate(Note.notehash.keys()):
            self.notes.insert(i, k)

    def search_item(self):

        self.one = tk.Toplevel()

        self.searchTitle = tk.Entry(self.one)
        self.searchList=tk.Listbox(self.one)
        search = tk.Button(self.one,text="search", command= self.search_b)
        self.searchList.bind("<Double-Button-1>", self.on_double_click_search)
        search.grid(row=1, column=0, padx=10, pady=10)
        self.searchTitle.grid(row=0, column=0, padx=10, pady=10)
        self.searchList.grid(row=2, column=0, padx=10, pady=10)

    def on_double_click_search(self, event):
        selected_title = self.searchList.get(self.searchList.curselection())
        messagebox.showinfo(f"{Note.notehash[selected_title]}", f"{Note.notehash[selected_title]}")


    # def on_double_click_search(self, event):
    #     self.found_title = self.searchList.get(self.searchList.curselection())


        self.one.destroy()


    def search_b(self):
        res = [k for k in Note.notehash if self.searchTitle.get() in k]
        for i, k in enumerate(res):
            self.searchList.insert(i,k)

    def remove_item(self):
        for i in self.notes.curselection():
            selected_title = self.notes.get(self.notes.curselection())
            del Note.notehash[selected_title]
            self.notes.delete(self.notes.curselection())
            self.update_notes_list()

    # def edit(self):
    #
    #     edit = tk.Toplevel()
    #     self.editNoteLebel = tk.Label(edit, text="edit note", font=("Arial", 16, "bold"))
    #
    #     self.editTitle = tk.Entry(edit)
    #     self.editText = tk.Text(edit)
    #     self.editButton = tk.Button(edit, text='supmit')
    #
    #     self.editNoteLebel.pack(padx=10, pady=10)
    #
    #     self.editTitle.insert(0, f"{self.found_title}")
    #     self.editTitle.pack(padx=10, pady=10)
    #
    #     self.editText.insert(tk.END, f"{Note.notehash[self.found_title]}")
    #     self.editText.pack(padx=10, pady=10)
    #
    #     self.editButton.pack(padx=10, pady=10)

    def on_double_click(self, event):
        selected_title = self.notes.get(self.notes.curselection())

        messagebox.showinfo(f"{Note.notehash[selected_title]}",f"{Note.notehash[selected_title]}")


    def addNote(self):
        addNote()
        self.update_notes_list()
