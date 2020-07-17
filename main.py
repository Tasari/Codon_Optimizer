import tkinter as tk
from src.Frontend.Checklist_board import add_checklist_board
from src.Frontend.Codon_Bias_Table import Codon_bias_entry

main_window = tk.Tk()

main_window.iconbitmap('icon.ico')

checklist_board = add_checklist_board(main_window)
checklist_board.grid(row=0, column=0)
Codon_bias_entry = Codon_bias_entry(main_window, 0, 1)
main_window.mainloop()