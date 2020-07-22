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
        self.dataframe = Frame(self)
        self.dataframe.grid(row=2, column=0)
        self.CAI = Label(self.dataframe, text="CAI = 0.00")
        self.CAI.grid(row=0, column=0)
        self.CGs = Label(self.dataframe, text="CG% = 00.00% CG1 = 00.00% CG2 = 00.00% CG3 = 00.00%")
        self.CGs.grid(row=0, column=1)
    def all_data(self):
        return self.text.get('1.0', END)

    def set_data(self, sequence):
        self.text.delete('1.0', END)
        self.text.insert(INSERT, sequence)

    def set_CAI(self, CAI):
        self.CAI.config(text='CAI = {}'.format(CAI))

    def set_CGs(self, CG, CG1, CG2, CG3):
        self.CGs.config(text="CG% = {}% CG1 = {}% CG2 = {}% CG3 = {}%".format(CG, CG1, CG2, CG3))