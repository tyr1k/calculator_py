#!/usr/bin/env python3

import tkinter as tk

class Calculator(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.result_var = tk.StringVar()
        self.result_var.set("0")

        self.result_label = tk.Label(self, textvariable=self.result_var, font=("Arial", 24))
        self.result_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+",
            "C" # add a new button for clear line
        ]
        row = 1
        col = 0
        for button_text in buttons:
            button = tk.Button(self, text=button_text, font=("Arial", 18), width=5, height=2)
            button.grid(row=row, column=col, padx=5, pady=5)
            button.bind("<Button-1>", self.button_click)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def button_click(self, event):
        button_text = event.widget["text"]
        if button_text == "=":
            try:
                result = eval(self.result_var.get())
                self.result_var.set(str(result))
            except:
                self.result_var.set("Error")
        elif button_text == "C": # handle the new clear line button
                self.result_var.set("0")
        else:
            if self.result_var.get() == "0" and button_text.isdigit():
                self.result_var.set(button_text)
            else:
                self.result_var.set(self.result_var.get() + button_text)

root = tk.Tk()
app = Calculator(master=root)
app.mainloop()
