from tkinter import Checkbutton, IntVar, Frame

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

    CAI_checkbutton = Checkbutton(checklist_board, text = "Maximize CAI",\
                                   variable = CAI_check, )

    Harmonization_checkbutton = Checkbutton(checklist_board, text = "Harmonize sequence", \
                                            variable = Harmonization_check)

    CG_balancing_checkbutton = Checkbutton(checklist_board, text = "Balance CG", \
                                            variable = CG_balancing_check)

    Hidden_STOP_checkbutton = Checkbutton(checklist_board, text = "Erase Hidden STOP codons", \
                                            variable = Hidden_STOP_check)

    Repeat_remove_checkbutton = Checkbutton(checklist_board, text = "Remove repeating bases", \
                                            variable = Repeat_remove_check)

    Cis_acting_checkbutton = Checkbutton(checklist_board, text = "Find cis-acting sequences", \
                                            variable = Cis_acting_check)

    Favored_sequences_checkbutton = Checkbutton(checklist_board, text = "Include sequence", \
                                            variable = Favored_sequences_check)

    Forbidden_sequences_checkbutton = Checkbutton(checklist_board, text = "Forbid sequence", \
                                            variable = Forbidden_sequences_check)



    CAI_checkbutton.grid(row=0, column=0, sticky='w')
    Harmonization_checkbutton.grid(row=1, column=0, sticky='w')
    CG_balancing_checkbutton.grid(row=2, column=0, sticky='w')
    Hidden_STOP_checkbutton.grid(row=0, column=1, sticky='w')
    Repeat_remove_checkbutton.grid(row=1, column=1, sticky='w')
    Cis_acting_checkbutton.grid(row=2, column=1, sticky='w')
    Favored_sequences_checkbutton.grid(row=0, column=2, sticky='w')
    Forbidden_sequences_checkbutton.grid(row=1, column=2, sticky='w')

    col_count, row_count = checklist_board.grid_size()

    for col in range(col_count):
        checklist_board.grid_columnconfigure(col, minsize=150)

    for row in range(row_count):
        checklist_board.grid_rowconfigure(row, minsize=20)

    return checklist_board