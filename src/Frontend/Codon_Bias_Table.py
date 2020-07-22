from tkinter import Frame, Text, Label, END

class Codon_bias_entry(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.label = Label(self, text='Codon Bias', font=('Arial', 16))
        self.label.grid(row=0, column=0)
        self.text = Text(self, bd=1, height=19, width=80)
        self.text.grid(row=1, column=0)
        self.CGs = Label(self, text='CG% = 00.00% CG1 = 00.00% CG2 = 00.00% CG3 = 00.00%')
        self.CGs.grid(row=2, column=0)
        
    def all_data(self):
        return self.text.get('1.0', END)
        
    def set_CGs(self, CGstable):
        self.CGs.config(text="CG% = {:02.2f}% CG1 = {:02.2f}% CG2 = {:02.2f}% CG3 = {:02.2f}%".format(CGstable[0], CGstable[1], CGstable[2], CGstable[3]))