from tkinter import Frame, Label, END, Radiobutton, IntVar
from tkinter.scrolledtext import ScrolledText
from src.logs import errors


class Codon_bias_entry(Frame):
    """Tkinter Frame containing information about Codon Bias.
    
    Class responsible of taking data from user, it has option to
    take the codon bias table from Kazusa.or.jp or representative 
    sequence of the organism.

    Atributes:
        Texts: 
            Text where user can put data in.
        Labels: 
            Labels containing various data.
        Radiobuttons: 
            Option to choose table or represenstative sequence.
    """
    def __init__(self, master):
        """Initialization with selecting main window"""
        super().__init__(master)
        self.label = Label(self, text="Codon Bias", font=("Arial", 16))
        self.label.grid(row=0, column=0)
        self.text = ScrolledText(self, bd=1, height=19, width=80)
        self.text.grid(row=1, column=0)
        self.CGs = Label(
            self, text="CG% = 00.00% CG1 = 00.00% CG2 = 00.00% CG3 = 00.00%"
        )
        self.CGs.grid(row=2, column=0)
        self.var = IntVar(None, 0)
        self.RadioTable = Radiobutton(
            self,
            text="Use Table",
            variable=self.var,
            value=0,
            command=lambda: self.set_text_of_label("Codon Bias"),
        )
        self.RadioSequence = Radiobutton(
            self,
            text="Use Sequence",
            variable=self.var,
            value=1,
            command=lambda: self.set_text_of_label("Sequences"),
        )
        self.RadioTable.grid(row=0, column=0, sticky="w")
        self.RadioSequence.grid(row=0, column=0, sticky="e")

    def all_data(self):
        """Method taking all the data in the text window"""
        return self.text.get("1.0", END).upper()

    def set_CGs(self, CGstable):
        """Method setting CG content of supersequence under the entry."""
        self.CGs.config(
            text="CG% = {:02.2f}% CG1 = {:02.2f}% CG2 = {:02.2f}% CG3 = {:02.2f}%".format(
                CGstable[0], CGstable[1], CGstable[2], CGstable[3]
            )
        )

    def check_table_valid(self):
        """Method checking if the data passed is valid table."""
        for letter in self.all_data().replace("\n", ""):
            if letter not in ['U', 'T', 'A', 'C', 'G', '.', ' ', ')', '(',
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                errors.append("Found invalid data char in table: {}".format(letter))
                raise Exception

    def set_text_of_label(self, new_text):
        """Method setting text on the top of entry"""
        self.label.config(text=new_text)
