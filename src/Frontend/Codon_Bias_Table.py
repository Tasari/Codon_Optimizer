from tkinter import Frame, Text, Label

class Codon_bias_entry(Frame):
    def __init__(self, master, row, column):
        super().__init__(master)
        self.text = Text(self, bd=1, height=19, width=80)
        self.text.grid(row=0, column=0)
        self.grid_columnconfigure(0, minsize=150)
        self.grid_rowconfigure(0, minsize=150)
        self.grid(row=row, column=column)
        
