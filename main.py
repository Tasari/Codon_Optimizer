import tkinter as tk
from src.Frontend.Checklist_board import add_checklist_board
from src.Frontend.Codon_Bias_Table import Codon_bias_entry
from src.Frontend.Gene_text import Gene_text

main_window = tk.Tk()

main_window.iconbitmap('icon.ico')

checklist_board = add_checklist_board(main_window)
checklist_board.grid(row=0, column=0, sticky='e')
codon_bias_entry = Codon_bias_entry(main_window)
codon_bias_entry.grid(row=0, column=1, columnspan=2)
input_gene = Gene_text(main_window, "Input gene")
output_gene = Gene_text(main_window, "Output gene")
input_gene.grid(row=1, column=0, sticky='w')
output_gene.grid(row=1, column=2, sticky='w')
optimize_button = tk.Button(main_window, text='OPTIMIZE', height=10, width=30, pady=5)
optimize_button.grid(row=1, column=1)

col_count, row_count = main_window.grid_size()

for col in range(col_count):
    main_window.grid_columnconfigure(col, minsize=200)

for row in range(row_count):
    main_window.grid_rowconfigure(row, minsize=200)

main_window.mainloop()