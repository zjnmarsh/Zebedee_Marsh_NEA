import tkinter as tk
from tkinter import ttk


class Main_Window:

    def __init__(self, master):
        self.master = master
        self.frame = ttk.Frame(master, padding=5)

        self.lbl_name = ttk.Label(self.frame, text='This is the main page')
        self.btn_SIR = ttk.Button(self.frame, text='SIR model', command=self.openSIR)

        self.frame.grid(row=0, column=0, sticky='nsew')

        self.lbl_name.grid(column=1, row=0, columnspan=3, sticky='n')
        self.btn_SIR.grid(column=1, row=1, sticky='s')

        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        self.frame.columnconfigure(1, weight=1)
        self.frame.rowconfigure(1, weight=1)

    def openSIR(self):
        # self.new_window = tk.Toplevel(self.master)
        # self.app = SIR_Window(self.new_window)
        # self.new_window = tk.Toplevel(self.master)
        # self.app = SIR_Window(self.new_window)

        root2 = tk.Tk()
        root2.title('SIR Model')
        root2.geometry('1400x900')

        new_window = SIR_Window(root2)
        root2.mainloop()

class SIR_Window:

    def __init__(self, master):
        self.master = master
        self.frame = ttk.Frame(master, padding=5)

        self.lbl_name = ttk.Label(self.frame, text='This is the SIR model')
        self.btn_SIR = ttk.Button(self.frame, text='Close', command=self.close)

        self.frame.grid(row=0, column=0, sticky='nsew')

        self.lbl_name.grid(column=1, row=0, columnspan=3, sticky='n')
        self.btn_SIR.grid(column=1, row=1, sticky='s')

        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        self.frame.columnconfigure(1, weight=1)
        self.frame.rowconfigure(1, weight=1)

    def close(self):
        self.master.destroy()


root = tk.Tk()
root.title('Main Window')
root.geometry('600x400')

window = Main_Window(root)

root.mainloop()
