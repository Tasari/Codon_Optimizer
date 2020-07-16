from tkinter import Checkbutton, IntVar, Frame, Entry

def block_entry(entry, var):
    if var.get() == 0:
        entry.configure(state='disabled')
    else:
        entry.configure(state='normal')

def add_checklist_board(master):
    checklist_board = Frame(master)
    CAI_check = IntVar()
    Harmonization_check = IntVar()
    CG_balancing_check = IntVar()
    Hidden_STOP_check = IntVar()
    Repeat_remove_check = IntVar()
    Cis_acting_check = IntVar()
    Favored_sequences_check = IntVar()
    Forbidden_sequences_check = IntVar()
    Hidden_codons_entry = Entry(checklist_board, bd=1, state='disabled')
    Include_sequence_entry = Entry(checklist_board, bd=1, state='disabled')
    Forbid_sequence_entry = Entry(checklist_board, bd=1, state='disabled')

    CAI_checkbutton = Checkbutton(checklist_board, text = "Maximize CAI",\
                                   variable = CAI_check, )

    Harmonization_checkbutton = Checkbutton(checklist_board, text = "Harmonize sequence", \
                                            variable = Harmonization_check)

    CG_balancing_checkbutton = Checkbutton(checklist_board, text = "Balance CG", \
                                            variable = CG_balancing_check)

    Hidden_STOP_checkbutton = Checkbutton(checklist_board, text = "Erase hidden codons", \
                                            variable = Hidden_STOP_check, \
                                            command=lambda  entry=Hidden_codons_entry, \
                                            var=Hidden_STOP_check: block_entry(entry, var))

    Repeat_remove_checkbutton = Checkbutton(checklist_board, text = "Remove repeating bases", \
                                            variable = Repeat_remove_check)

    Cis_acting_checkbutton = Checkbutton(checklist_board, text = "Find cis-acting sequences", \
                                            variable = Cis_acting_check)

    Favored_sequences_checkbutton = Checkbutton(checklist_board, text = "Include sequence", \
                                            variable = Favored_sequences_check, \
                                            command=lambda entry=Include_sequence_entry, \
                                            var = Favored_sequences_check: block_entry(entry, var))

    Forbidden_sequences_checkbutton = Checkbutton(checklist_board, text = "Forbid sequence", \
                                            variable = Forbidden_sequences_check, \
                                            command = lambda: block_entry(Forbid_sequence_entry, Forbidden_sequences_check))



    CAI_checkbutton.grid(row=0, column=0, sticky='w')
    Harmonization_checkbutton.grid(row=1, column=0, sticky='w')
    CG_balancing_checkbutton.grid(row=2, column=0, sticky='w')
    Hidden_STOP_checkbutton.grid(row=0, column=1, sticky='w')
    Hidden_codons_entry.grid(row=0, column=1, sticky='s')
    Repeat_remove_checkbutton.grid(row=2, column=1, sticky='w')
    Cis_acting_checkbutton.grid(row=1, column=1, sticky='w')
    Favored_sequences_checkbutton.grid(row=0, column=2, sticky='w')
    Include_sequence_entry.grid(row=0, column=2, sticky='s')
    Forbidden_sequences_checkbutton.grid(row=1, column=2, sticky='w')
    Forbid_sequence_entry.grid(row=1, column=2, sticky='s')
    col_count, row_count = checklist_board.grid_size()

    for col in range(col_count):
        checklist_board.grid_columnconfigure(col, minsize=150)

    for row in range(row_count):
        checklist_board.grid_rowconfigure(row, minsize=65)

    return checklist_board