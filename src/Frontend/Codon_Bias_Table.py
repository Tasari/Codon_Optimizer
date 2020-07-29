from tkinter import Frame, Label, END
from tkinter.scrolledtext import ScrolledText
from src.logs import errors

class Codon_bias_entry(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.label = Label(self, text='Codon Bias', font=('Arial', 16))
        self.label.grid(row=0, column=0)
        self.text = ScrolledText(self, bd=1, height=19, width=80)
        self.text.grid(row=1, column=0)
        self.CGs = Label(self, text='CG% = 00.00% CG1 = 00.00% CG2 = 00.00% CG3 = 00.00%')
        self.CGs.grid(row=2, column=0)
        
    def all_data(self):
        return self.text.get('1.0', END).upper()
        
    def set_CGs(self, CGstable):
        self.CGs.config(text="CG% = {:02.2f}% CG1 = {:02.2f}% CG2 = {:02.2f}% CG3 = {:02.2f}%".format(CGstable[0], CGstable[1], CGstable[2], CGstable[3]))

    def check_table_valid(self):
        for letter in self.all_data().replace('\n', ''):
            if letter not in ['U', 'T', 'A', 'C', 'G', '.', ' ', ')', '(', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                errors.append("Found invalid data char in table: {}".format(letter))
                raise Exception