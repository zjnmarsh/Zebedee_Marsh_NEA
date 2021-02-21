import tkinter as tk
from tkinter import ttk
import pandas as pd
from tkinter import filedialog
from tkinter import messagebox

import sqlite3

import sub_SIR_model as my_sir
import sub_CA_model as my_ca
import sub_sql_functions as my_sql

current_user = "zebedee"
current_id = "25414344"

class gui_history:
    """GUI history window which shows history of values entered for the user currently logged in
    """

    def __init__(self, master):
        self.master = master
        self.frame = ttk.Frame(master, padding=5)
        self.frame.grid(row=0, column=0, sticky='nsew')
        # self.user_history = my_sql.ca_return_history(current_id)  # user_history is a list of tuples
        # print(self.user_history)

        self.lb_history = tk.Listbox(self.frame, width=50)
        # for i in range(len(self.user_history)):
        #     to_insert = str(i) + "  " + str(self.user_history[i])
        #     self.lb_history.insert(i, to_insert)

        self.lbl_title = ttk.Label(self.frame, text=f"History of {current_user}")
        self.btn_exit = ttk.Button(self.frame, text="Exit", command="")
        self.lbl_text = ttk.Label(self.frame, text="Enter number to simulate with same parameters")
        self.lbl_key = ttk.Label(self.frame,
                                 text="")
        self.e_sim_num = ttk.Entry(self.frame)
        self.btn_use = ttk.Button(self.frame, text="Use values", command="")

        self.lbl_title.grid(column=1, row=1, columnspan=3)
        self.lbl_text.grid(column=1, row=2, columnspan=3)
        # self.lbl_key.grid(column=1, row=3)
        self.lb_history.grid(column=1, row=4)
        self.e_sim_num.grid(column=2, row=4)
        self.btn_use.grid(column=3, row=4)
        self.btn_exit.grid(column=2, row=5, columnspan=2)

    # def exit(self):
    #     self.master.destroy()
    #     main_ca = tk.Tk()
    #     main_ca.title('CA')
    #     new_window = gui_First_CA_Window(main_ca)
    #     main_ca.mainloop()
    #
    # def use(self):
    #     """User enter number and set of parameters are retrieved from the database"""
    #     sim_number = int(self.e_sim_num.get())
    #     sim_param = list(self.user_history[sim_number])
    #     print(sim_param)
    #     sim_param.append(False)
    #     ca = my_ca.cellular_automata(*sim_param)
    #     ca.new_generation()

class CA_history(gui_history):
    def __init__(self, master):
        gui_history.__init__(self, master)

        self.btn_exit['command'] = self.exit
        self.btn_use['command'] = self.use

        self.user_history = my_sql.ca_return_history(current_id)  # user_history is a list of tuples
        print(self.user_history)
        for i in range(len(self.user_history)):
            to_insert = str(i) + "  " + str(self.user_history[i])
            self.lb_history.insert(i, to_insert)
        self.lbl_key['text'] = "Sim Number (cells, generations, x, y, infection radius, number infected, recovered can be infected, days until recovered, use immunity, days of immunity)"
        self.lbl_key.grid(column=1, row=3)


    def exit(self):
        pass
    def use(self):
        pass


root = tk.Tk()
root.title("main window")
window = CA_history(root)
root.mainloop()
