import tkinter as tk
from src.Frontend.Checklist_board import add_checklist_board

main_window = tk.Tk()
main_window.iconbitmap('icon.ico')
checklist_board = add_checklist_board(main_window)
checklist_board.pack(side='top')
main_window.mainloop()