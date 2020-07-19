from tkinter import Frame, Text, Label

class Codon_bias_entry(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.label = Label(self, text='Codon Bias', font=('Arial', 16))
        self.label.grid(row=0, column=0)
        self.text = Text(self, bd=1, height=19, width=80)
        self.text.grid(row=1, column=0)

        
