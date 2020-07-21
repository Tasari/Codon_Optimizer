from tkinter import scrolledtext, Frame, Label, END, INSERT

class Gene_text(Frame):
    def __init__(self, master, label=0):
        super().__init__(master)
        if label:
            self.label=Label(self, text=label, font=('Arial', 16))
        self.text = scrolledtext.ScrolledText(self, bd=1, width=66, height=15)
        if label:
            self.label.grid(row=0, column=0)
        self.text.grid(row=1, column=0, sticky='w')
    
    def all_data(self):
        return self.text.get('1.0', END)

    def set_data(self, sequence):
        self.text.delete('1.0', END)
        self.text.insert(INSERT, sequence)