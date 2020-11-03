import tkinter as tk
from tkinter import ttk
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
import time
from matplotlib.animation import FuncAnimation
import matplotlib
import csv
import json
from tkinter import filedialog

import sub_SIR_model as my_sir
import sub_CA_model as my_ca
import sub_sql_functions as my_sql

current_user = "None"


class gui_Main_Window:

    def __init__(self, master):
        self.master = master
        self.frame = ttk.Frame(master, padding=5)

        # self.lbl_name = ttk.Label(self.frame, text='This is the main page')
        self.e_user = ttk.Entry(self.frame)
        self.btn_login = ttk.Button(self.frame, text='Login', command=self.login)
        self.btn_SIR = ttk.Button(self.frame, text='SIR model', command=self.openSIR, state=tk.DISABLED)
        self.btn_CA = ttk.Button(self.frame, text='Cellular Automata', command=self.openCA, state=tk.DISABLED)

        self.frame.grid(row=0, column=0, sticky='nsew')

        # self.lbl_name.grid(column=1, row=0, columnspan=3, sticky='n')
        self.e_user.grid(column=1, row=0, sticky='n')
        self.btn_login.grid(column=2, row=0, sticky='n')
        self.btn_SIR.grid(column=1, row=1, columnspan=2, sticky='s')
        self.btn_CA.grid(column=1, row=2, columnspan=2, sticky='s')

        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        self.frame.columnconfigure(1, weight=1)
        self.frame.rowconfigure(1, weight=1)

    def openSIR(self):
        # self.master.destroy()
        root2 = tk.Tk()
        root2.title('SIR Model')
        # root2.geometry('1400x900')
        new_window = gui_First_SIR_Window(root2)
        root2.mainloop()

    def openCA(self):
        # self.master.destroy()
        root2 = tk.Tk()
        root2.title('CA Model')
        new_window = gui_First_CA_Window(root2)
        root2.mainloop()

    def login(self):
        username = str(self.e_user.get())
        my_sql.enter_username(username)
        global current_user
        current_user = username

        self.btn_SIR['state'] = tk.NORMAL
        self.btn_CA['state'] = tk.NORMAL
        self.e_user.destroy()
        self.btn_login.destroy()
        self.lbl_name = ttk.Label(self.frame, text=f'Hello {current_user}')
        self.lbl_name.grid(column=1, row=0)
        self.btn_logout = ttk.Button(self.frame, text='logout', command=self.logout)
        self.btn_logout.grid(column=2, row=0)

    def logout(self):
        print('logout')
        self.e_user = ttk.Entry(self.frame)
        self.btn_login = ttk.Button(self.frame, text='Login', command=self.login)
        self.e_user.grid(column=1, row=0, sticky='n')
        self.btn_login.grid(column=2, row=0, sticky='n')
        self.btn_SIR['state'] = tk.DISABLED
        self.btn_CA['state'] = tk.DISABLED


# ---------------------------------------

class gui_First_SIR_Window:
    """Class asking user to enter how many graphs they want"""

    def __init__(self, master):
        self.master = master
        self.frame = ttk.Frame(master, padding=5)

        self.lbl_name = ttk.Label(self.frame, text='This is the SIR model')

        self.lbl_num_sim = ttk.Label(self.frame, text='Number of simulations')
        self.e_num_sim = ttk.Entry(self.frame)
        # self.num_sim.insert(0, 1)
        self.btn_open_file = ttk.Button(self.frame, text='Load File', command=self.open_file)
        self.btn_input_param = ttk.Button(self.frame, text='Enter Parameters', command=self.input)
        self.btn_close = ttk.Button(self.frame, text='Close', command=self.close)

        self.frame.grid(row=0, column=0, sticky='nsew')

        self.lbl_name.grid(column=0, row=0, columnspan=2, sticky='n')
        self.lbl_num_sim.grid(column=0, row=1)
        self.e_num_sim.grid(column=1, row=1)
        # self.num_sim.grid(column=0, row=1)
        self.btn_open_file.grid(column=0, row=2)
        self.btn_input_param.grid(column=1, row=2)
        self.btn_close.grid(column=0, row=3, sticky='s')

        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        self.frame.columnconfigure(1, weight=1)
        self.frame.rowconfigure(1, weight=1)

    def close(self):
        self.master.destroy()

    def open_file(self):
        filename = filedialog.askopenfilename()
        df = pd.read_excel(filename)
        # print(df)

    def input(self):
        self.number_of_simulations = int(self.e_num_sim.get())
        print(self.number_of_simulations)

        # self.number_of_simulations = 1
        root3 = tk.Tk()
        root3.title('Input Parameters')
        input_window = gui_SIR_Param(root3, self.number_of_simulations)
        root3.mainloop()


class gui_SIR_Param:
    """Class for entering SIR parameters"""

    def __init__(self, master, num_sim):
        self.param_list = [[], [], [], [], []]
        self.counter = 0

        self.number_of_simulations = num_sim
        self.master = master
        self.frame = ttk.Frame(master, padding=5)
        self.frame.grid(row=0, column=0, sticky='nsew')

        # label variables
        self.lbl_name = ttk.Label(self.frame, text='Enter parameters for SIR model')
        self.s_name = ttk.Label(self.frame, text='Susceptible')
        self.i_name = ttk.Label(self.frame, text='Infected')
        self.r_name = ttk.Label(self.frame, text='Recovered')
        self.tr_name = ttk.Label(self.frame, text='Transmission rate')
        self.re_name = ttk.Label(self.frame, text='Recovery rate')
        self.btn_enter = ttk.Button(self.frame, text='Enter', command=self.enter_param)

        # button variables
        self.e_s = ttk.Entry(self.frame)
        self.e_i = ttk.Entry(self.frame)
        self.e_r = ttk.Entry(self.frame)
        self.e_tr = ttk.Entry(self.frame)
        self.e_re = ttk.Entry(self.frame)

        # gridding label variables
        self.lbl_name.grid(column=0, row=0, columnspan=2, sticky='n')
        self.s_name.grid(column=0, row=1, sticky='w')
        self.i_name.grid(column=0, row=2, sticky='w')
        self.r_name.grid(column=0, row=3, sticky='w')
        self.tr_name.grid(column=0, row=4, sticky='w')
        self.re_name.grid(column=0, row=5, sticky='w')

        self.e_s.grid(column=1, row=1, sticky='w')
        self.e_i.grid(column=1, row=2, sticky='w')
        self.e_r.grid(column=1, row=3, sticky='w')
        self.e_tr.grid(column=1, row=4, sticky='w')
        self.e_re.grid(column=1, row=5, sticky='w')

        self.btn_enter.grid(column=0, row=6, columnspan=2, sticky='s')

        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        # weight elements for resizing
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=1)
        self.frame.rowconfigure(2, weight=1)
        self.frame.rowconfigure(3, weight=1)
        self.frame.rowconfigure(4, weight=1)
        self.frame.rowconfigure(5, weight=1)
        self.frame.rowconfigure(6, weight=1)

    def enter_param(self):
        self.counter += 1

        self.param_list[0].append(float(self.e_s.get()))
        self.param_list[1].append(float(self.e_i.get()))
        self.param_list[2].append(float(self.e_r.get()))
        self.param_list[3].append(float(self.e_tr.get()))
        self.param_list[4].append(float(self.e_re.get()))

        self.e_s.delete(0, 'end')
        self.e_i.delete(0, 'end')
        self.e_r.delete(0, 'end')
        self.e_tr.delete(0, 'end')
        self.e_re.delete(0, 'end')

        if self.counter == self.number_of_simulations:
            self.submit_param()
            self.counter = 0

    def submit_param(self):

        # print(self.param_list)
        self.master.destroy()
        queue = my_sir.QueueSimulation(self.number_of_simulations, self.param_list[0], self.param_list[1], self.param_list[2],
                                       self.param_list[3], self.param_list[4],
                                       100)
        queue.run_simulation()


# ---------------------------------------

class gui_First_CA_Window:

    def __init__(self, master):
        self.master = master
        self.frame = ttk.Frame(master, padding=5)

        self.lbl_name = ttk.Label(self.frame, text='This is the Cellular Automata model')
        # self.num_sim = ttk.Entry(self.frame)
        # self.num_sim.insert(0, 1)
        self.btn_open_file = ttk.Button(self.frame, text='Load File', command=self.open_file)
        self.btn_input_param = ttk.Button(self.frame, text='Enter Parameters', command=self.input)
        self.btn_close = ttk.Button(self.frame, text='Close', command=self.close)

        self.frame.grid(row=0, column=0, sticky='nsew')

        self.lbl_name.grid(column=0, row=0, columnspan=2, sticky='n')
        # self.num_sim.grid(column=0, row=1)
        self.btn_open_file.grid(column=0, row=1)
        self.btn_input_param.grid(column=1, row=1)
        self.btn_close.grid(column=0, row=2, sticky='s')

        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        self.frame.columnconfigure(1, weight=1)
        self.frame.rowconfigure(1, weight=1)

    def open_file(self):
        # enter file stuff
        print("Opening file dialog")
        file = filedialog.askopenfile(mode="r")
        lines = [line.rstrip('\n') for line in file]
        file.close()

        if lines[-1] == "":
            del lines[-1]

        # result = [json.loads(item) for item in lines]
        self.master.destroy()

        ca = my_ca.cellular_automata(0, 0, 0, 0, 0, 0, False, 0, False, 0, True, lines)
        ca.new_generation()
        self.master.destroy()

    def input(self):
        # manual user input
        root3 = tk.Tk()
        root3.title('Input Parameters')
        input_window = gui_CA_Param(root3)

    def close(self):
        self.master.destroy()


class gui_CA_Param:
    """Class for entering CA parameters
    Need to make some entry boxes dependent on checkboxes
    """

    def __init__(self, master):
        self.master = master
        self.frame = ttk.Frame(master, padding=5)
        self.frame.grid(row=0, column=0, sticky='nsew')

        # label variables
        self.l_lbl_name = ttk.Label(self.frame, text='Enter parameters for CA model')
        self.l_no_cells = ttk.Label(self.frame, text='Number of cells')
        self.l_gen = ttk.Label(self.frame, text='Generations')
        self.l_size_x = ttk.Label(self.frame, text='Size x')
        self.l_size_y = ttk.Label(self.frame, text='Size y')
        self.l_inf_rad = ttk.Label(self.frame, text='Infection radius')
        self.l_no_inf = ttk.Label(self.frame, text='Number of infected')
        self.l_r_i = ttk.Label(self.frame, text='Recovered can be infected?')
        self.l_d_r = ttk.Label(self.frame, text='Days until recovery')
        self.l_use_imm = ttk.Label(self.frame, text='Use immunity')
        self.l_d_i = ttk.Label(self.frame, text='Days of immunity')

        # bool values for checkbuttons
        self.b_r_i = tk.BooleanVar()
        self.b_u_i = tk.BooleanVar()

        # entry and checkbutton variables
        self.e_no_cells = ttk.Entry(self.frame)
        self.e_gen = ttk.Entry(self.frame)
        self.e_size_x = ttk.Entry(self.frame)
        self.e_size_y = ttk.Entry(self.frame)
        self.e_inf_rad = ttk.Entry(self.frame)
        self.e_no_inf = ttk.Entry(self.frame)
        self.cb_r_i = ttk.Checkbutton(self.frame, variable=self.b_r_i)
        self.e_d_r = ttk.Entry(self.frame)
        self.cb_use_imm = ttk.Checkbutton(self.frame, variable=self.b_u_i)
        self.e_d_i = ttk.Entry(self.frame)

        self.btn_enter = ttk.Button(self.frame, text='Enter', command=self.enter_param)

        # grid label variables
        self.l_lbl_name.grid(column=0, row=0, columnspan=2, sticky='n')
        self.l_no_cells.grid(column=0, row=1, sticky='w')
        self.l_gen.grid(column=0, row=2, sticky='w')
        self.l_size_x.grid(column=0, row=3, sticky='w')
        self.l_size_y.grid(column=0, row=4, sticky='w')
        self.l_inf_rad.grid(column=0, row=5, sticky='w')
        self.l_no_inf.grid(column=0, row=6, sticky='w')
        self.l_r_i.grid(column=0, row=7, sticky='w')
        self.l_d_r.grid(column=2, row=7, sticky='w')
        self.l_use_imm.grid(column=0, row=8, sticky='w')
        self.l_d_i.grid(column=2, row=8, sticky='w')

        # grid entry variables
        self.e_no_cells.grid(column=2, row=1, sticky='w')
        self.e_gen.grid(column=2, row=2, sticky='w')
        self.e_size_x.grid(column=2, row=3, sticky='w')
        self.e_size_y.grid(column=2, row=4, sticky='w')
        self.e_inf_rad.grid(column=2, row=5, sticky='w')
        self.e_no_inf.grid(column=2, row=6, sticky='w')
        self.cb_r_i.grid(column=1, row=7, sticky='w')
        self.e_d_r.grid(column=3, row=7, sticky='w')
        self.cb_use_imm.grid(column=1, row=8, sticky='w')
        self.e_d_i.grid(column=3, row=8, sticky='w')

        self.btn_enter.grid(column=0, row=9, columnspan=4, sticky='s')

        # grid main column and tow
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        # weight elements for resizing
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=1)
        self.frame.rowconfigure(2, weight=1)
        self.frame.rowconfigure(3, weight=1)
        self.frame.rowconfigure(4, weight=1)
        self.frame.rowconfigure(5, weight=1)
        self.frame.rowconfigure(6, weight=1)

    def enter_param(self):
        # should call CA function in this
        no_cells = int(self.e_no_cells.get())
        generations = int(self.e_gen.get())
        size_x = int(self.e_size_x.get())
        size_y = int(self.e_size_y.get())
        inf_rad = int(self.e_inf_rad.get())
        no_inf = int(self.e_no_inf.get())
        rec_inf = self.b_r_i.get()
        days_rec = int(self.e_d_r.get())
        use_imm = self.b_u_i.get()
        days_imm = int(self.e_d_i.get())

        self.master.destroy()
        # print(rec_inf)
        # print(use_imm)

        arguments = [no_cells, generations, size_x, size_y, inf_rad, no_inf, rec_inf, days_rec, use_imm,
                     days_imm, False]

        my_sql.ca_enter_param(current_user, arguments)

        # ca = my_ca.cellular_automata(no_cells, generations, size_x, size_y, inf_rad, no_inf, rec_inf, days_rec, use_imm,
        #                              days_imm, False)
        ca = my_ca.cellular_automata(*arguments)  # arguments sent as separate parameters

        ca.new_generation()


# ---------------------------------------


root = tk.Tk()
root.title('Main Window')

window = gui_Main_Window(root)

root.mainloop()
