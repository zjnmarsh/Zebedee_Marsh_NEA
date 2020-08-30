import tkinter as tk
from tkinter import ttk


class mainWindow():

    def __init__(self, master):
        self.master = master
        self.frame = ttk.Frame(master, padding=5)

        self.lbl_name = ttk.Label(self.frame, text='This is the main page')
        self.btn_SIR = ttk.Button(self.frame, text='SIR model')

        self.frame.grid(row=0, column=0)

        self.lbl_name.grid(column=0, row=0, columnspan=3)
        self.btn_SIR.grid(column=1, row=1)


root = tk.Tk()
root.title('Main Window')

window = mainWindow(root)

root.mainloop()
