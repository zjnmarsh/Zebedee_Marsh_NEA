import tkinter as tk
from tkinter import ttk
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random


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

        self.master.destroy()
        root2 = tk.Tk()
        root2.title('SIR Model')
        # root2.geometry('1400x900')
        new_window = SIR_Window(root2)
        root2.mainloop()


class SIR_Window:
    """Class asking user to enter how many graphs they want"""

    def __init__(self, master):
        self.master = master
        self.frame = ttk.Frame(master, padding=5)

        self.lbl_name = ttk.Label(self.frame, text='This is the SIR model')
        self.num_sim = ttk.Entry(self.frame)
        self.num_sim.insert(0, 1)
        self.btn_input_param = ttk.Button(self.frame, text='Enter Parameters', command=self.input)
        self.btn_close = ttk.Button(self.frame, text='Close', command=self.close)

        self.frame.grid(row=0, column=0, sticky='nsew')

        self.lbl_name.grid(column=0, row=0, columnspan=2, sticky='n')
        self.num_sim.grid(column=0, row=1)
        self.btn_input_param.grid(column=1, row=1)
        self.btn_close.grid(column=0, row=2, sticky='s')

        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        self.frame.columnconfigure(1, weight=1)
        self.frame.rowconfigure(1, weight=1)

    def close(self):
        self.master.destroy()

    def input(self):
        self.number_of_simulations = int(self.num_sim.get())
        # print(self.number_of_simulations)

        root3 = tk.Tk()
        root3.title('Input Parameters')
        input_window = SIR_Param(root3, self.number_of_simulations)
        root3.mainloop()




class SIR_Param:
    """Class for entering SIR parameters"""

    def __init__(self, master, num_sim):
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
        # self.master.destroy()
        param_list = [[],[],[],[],[]]
        # for i in range(self.number_of_simulations):
        param_list[0].append(float(self.e_s.get()))
        param_list[1].append(float(self.e_i.get()))
        param_list[2].append(float(self.e_r.get()))
        param_list[3].append(float(self.e_tr.get()))
        param_list[4].append(float(self.e_re.get()))
        # param_list.append()
        # print(param_list)


root = tk.Tk()
root.title('Main Window')
# root.geometry('600x400')
# root.geometry('400x400')
window = Main_Window(root)
# window = SIR_Param(root)

root.mainloop()
