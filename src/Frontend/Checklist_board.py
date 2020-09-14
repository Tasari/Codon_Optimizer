from tkinter import Checkbutton, IntVar, Frame, Entry, Label, END


class checklist_board(Frame):
    """Frame containing multiple checkbuttons symbolizing options.

    Class contains all the options which can be used in optimize
    and checkbuttons telling if option should be used.

    Attributes:
        Checks: Checkboxes telling if box is checked.
        Entries: Entries containing data used in checked options. 
        Checkbuttons: Actual Checkbuttons
    """
    def __init__(self, master):
        """Inits the class connecting it to main window.
        
        Creates all of checks, checkbuttons and entries, 
        putting them into their places.
        """
        super().__init__(master)
        self.label = Label(self, text="Options", font=("Arial", 16))
        self.label.grid(row=0, column=0)
        self.checklist_board = Frame(self)
        self.CAI_maximize_check = IntVar()
        self.Harmonization_check = IntVar()
        self.Hidden_STOP_check = IntVar()
        self.Repeat_remove_check = IntVar()
        self.Favored_sequences_check = IntVar()
        self.Forbidden_sequences_check = IntVar()
        self.Hidden_codons_entry = Entry(self.checklist_board, bd=1, state="disabled")
        self.Include_sequence_entry = Entry(
            self.checklist_board, bd=1, state="disabled"
        )
        self.Forbid_sequence_entry = Entry(self.checklist_board, bd=1, state="disabled")

        self.CAI_checkbutton = Checkbutton(
            self.checklist_board,
            onvalue=1,
            offvalue=0,
            text="Maximize CAI",
            variable=self.CAI_maximize_check,
        )

        self.Harmonization_checkbutton = Checkbutton(
            self.checklist_board,
            text="Harmonize sequence \n and balance CG",
            variable=self.Harmonization_check,
        )

        self.Hidden_STOP_checkbutton = Checkbutton(
            self.checklist_board,
            text="Erase hidden codons",
            variable=self.Hidden_STOP_check,
            command=lambda entry=self.Hidden_codons_entry, var=self.Hidden_STOP_check: self.block_entry(
                entry, var
            ),
        )

        self.Repeat_remove_checkbutton = Checkbutton(
            self.checklist_board,
            text="Remove repeating bases",
            variable=self.Repeat_remove_check,
        )

        self.Favored_sequences_checkbutton = Checkbutton(
            self.checklist_board,
            text="Include sequence",
            variable=self.Favored_sequences_check,
            command=lambda entry=self.Include_sequence_entry, var=self.Favored_sequences_check: self.block_entry(
                entry, var
            ),
        )

        self.Forbidden_sequences_checkbutton = Checkbutton(
            self.checklist_board,
            text="Forbid sequence",
            variable=self.Forbidden_sequences_check,
            command=lambda: self.block_entry(
                self.Forbid_sequence_entry, self.Forbidden_sequences_check
            ),
        )

        self.CAI_checkbutton.grid(row=0, column=0, sticky="w")
        self.Harmonization_checkbutton.grid(row=1, column=0, sticky="w")
        self.Hidden_STOP_checkbutton.grid(row=0, column=1, sticky="w")
        self.Hidden_codons_entry.grid(row=0, column=1, sticky="s")
        self.Repeat_remove_checkbutton.grid(row=1, column=1, sticky="w")
        self.Favored_sequences_checkbutton.grid(row=0, column=2, sticky="w")
        self.Include_sequence_entry.grid(row=0, column=2, sticky="s")
        self.Forbidden_sequences_checkbutton.grid(row=1, column=2, sticky="w")
        self.Forbid_sequence_entry.grid(row=1, column=2, sticky="s")
        col_count, row_count = self.checklist_board.grid_size()

        for col in range(col_count):
            self.checklist_board.grid_columnconfigure(col, minsize=150)

        for row in range(row_count):
            self.checklist_board.grid_rowconfigure(row, minsize=65)
        self.checklist_board.grid(row=1, column=0)

    def block_entry(self, entry, var):
        """Defines if entry should be blocket based on check"""
        if var.get() == 0:
            entry.configure(state="disabled")
        else:
            entry.configure(state="normal")

    def get_forbidden(self):
        """Takes data from forbidden entry"""
        return self.Forbid_sequence_entry.get().replace("T", "U").split(", ")

    def get_favored(self):
        """Takes the data from include entry"""
        return self.Include_sequence_entry.get().replace("T", "U").split(", ")

    def get_hidden(self):
        """Takes the data form hidden entry"""
        return self.Hidden_codons_entry.get().replace("T", "U").split(", ")
