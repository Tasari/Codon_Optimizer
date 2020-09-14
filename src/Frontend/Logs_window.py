from tkinter import Frame, Text, Label, INSERT, END


class Log_text(Frame):
    """Window holding the logs given out by Genetic_Optimizer."""
    def __init__(self, master):
        super().__init__(master)
        self.label = Label(self, text="Logs", font=("Arial", 16))
        self.label.grid(row=0, column=0)
        self.text = Text(self, bd=1, height=40, width=40)
        self.text.grid(row=1, column=0)

    def add_errors(self, errors):
        """Method adding errors to Log window."""
        self.text.delete("1.0", END)
        for error in errors:
            self.text.insert(
                INSERT, error + "\n"
            )
