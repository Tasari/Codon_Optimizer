from tkinter import Frame, Text, Label, INSERT, END


class Log_text(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.label = Label(self, text="Logs", font=("Arial", 16))
        self.label.grid(row=0, column=0)
        self.text = Text(self, bd=1, height=40, width=40)
        self.text.grid(row=1, column=0)

    def add_errors(self, errors):
        self.text.delete("1.0", END)
        for error in errors:
            self.text.insert(
                INSERT, error + "\n"
            )
