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


class gui_Main_Window:

    def __init__(self, master):
        self.master = master
        self.frame = ttk.Frame(master, padding=5)

        self.lbl_name = ttk.Label(self.frame, text='This is the main page')
        self.btn_SIR = ttk.Button(self.frame, text='SIR model', command=self.openSIR)
        self.btn_CA = ttk.Button(self.frame, text='Cellular Automata', command=self.openCA)

        self.frame.grid(row=0, column=0, sticky='nsew')

        self.lbl_name.grid(column=1, row=0, columnspan=3, sticky='n')
        self.btn_SIR.grid(column=1, row=1, sticky='s')
        self.btn_CA.grid(column=1, row=2, sticky='s')

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
        new_window = gui_First_SIR_Window(root2)
        root2.mainloop()

    def openCA(self):
        self.master.destroy()
        root2 = tk.Tk()
        root2.title('CA Model')
        new_window = gui_First_CA_Window(root2)
        root2.mainloop()


class gui_First_SIR_Window:
    """Class asking user to enter how many graphs they want"""

    def __init__(self, master):
        self.master = master
        self.frame = ttk.Frame(master, padding=5)

        self.lbl_name = ttk.Label(self.frame, text='This is the SIR model')
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

    def close(self):
        self.master.destroy()

    def open_file(self):
        filename = filedialog.askopenfilename()
        df = pd.read_excel(filename)
        # print(df)

    def input(self):
        # self.number_of_simulations = int(self.num_sim.get())
        # print(self.number_of_simulations)

        self.number_of_simulations = 1
        root3 = tk.Tk()
        root3.title('Input Parameters')
        input_window = gui_SIR_Param(root3, self.number_of_simulations)
        root3.mainloop()


class gui_SIR_Param:
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
        param_list = [[], [], [], [], []]
        # for i in range(self.number_of_simulations):
        param_list[0].append(float(self.e_s.get()))
        param_list[1].append(float(self.e_i.get()))
        param_list[2].append(float(self.e_r.get()))
        param_list[3].append(float(self.e_tr.get()))
        param_list[4].append(float(self.e_re.get()))
        # param_list.append()
        # print(param_list)
        queue = QueueSimulation(1, param_list[0], param_list[1], param_list[2], param_list[3], param_list[4], 100)
        queue.run_simulation()


class QueueSimulation:

    def __init__(self, n, s_list, i_list, r_list, b_list, g_list, t):
        self.n = n  # number of simulations to be run
        self.parameters = []
        for i in range(n):
            self.parameters.append([s_list[i], i_list[i], r_list[i], b_list[i], g_list[i], t, i + 1])
        print(self.parameters)

    def run_simulation(self):
        sir_model = SIR_model()
        for i in range(self.n):
            sir_model.SIR_model(*self.parameters[i])
        plt.show()


class SIR_model:

    def __init__(self):
        pass

    def SIR_model(self, s0, i0, r0, beta, gamma, t, f, *args, **kwargs):
        """
        :param s0: number of susceptible people
        :param i0: number of infected people
        :param r0: number of recovered people
        :param beta: transmission rate of an individual
        :param gamma: recovery rate of an individual
        :param t: how long the simulation should run for
        :param f: how many graphs should be calculated simultaneously
        """

        plt.figure(f)  # names the graph
        N = s0 + i0 + r0  # total population

        timearray = list(range(1, int(t)))  # creates time array

        def eqns(param):
            # e = random.uniform(0, 1)
            e = 0
            S, I, R = param
            dsdt = (-(beta * S * I) / N) + (e * R)  # rate of change of susceptible individuals
            didt = ((beta * S * I) / N) - gamma * I  # rate of change of infected individuals
            drdt = (gamma * I) - (e * R)  # rate of change of recovered individuals
            return dsdt, didt, drdt

        def solver():  # solves differential equations in eqns
            param = (s0, i0, r0)
            solver_result = [[], [], []]
            for time in timearray:
                eqns_results = eqns(param)
                x, y, z = (param[0] + eqns_results[0]), (param[1] + eqns_results[1]), (param[2] + eqns_results[2])
                solver_result[0].append(x)
                solver_result[1].append(y)
                solver_result[2].append(z)
                param = (x, y, z)
            return solver_result

        solver_result = solver()

        # print(solver_result)

        def export_to_excel():  # exports calculated results to excel
            data = {'Time': timearray,
                    'S': solver_result[0],
                    'I': solver_result[1],
                    'R': solver_result[2]}

            df = pd.DataFrame(data, columns=['Time', 'S', 'I', 'R'])
            name = "output" + str(f) + ".xlsx"
            df.to_excel(name, sheet_name='output')

        export_to_excel()
        plt.plot(timearray, solver_result[0], label="S(t)")
        plt.plot(timearray, solver_result[1], label="I(t)")
        plt.plot(timearray, solver_result[2], label="R(t)")


# ----------------------------------------------------------------------

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
        pass

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

        ca = cellular_automata(no_cells, generations, size_x, size_y, inf_rad, no_inf, rec_inf, days_rec, use_imm,
                               days_imm)
        ca.new_generation()


# class cell:
#     """Each cell will be a class instance of this class"""
#
#     def __init__(self, x, y, infected, d_r, d_i):
#         self.x = x
#         self.y = y
#         self.infected = infected
#         self.recovered = False
#         self.recover_count = d_r  # default - can be changed - time until infected cell recovers
#         self.immune = False
#         self.immune_count = d_i
#         self.original_immune = d_i
#         # self.infection_rate = i
#
#     def cell_test_function(self):
#         return self.x, self.y, self.infected
#
#     def location(self):
#         # print(self.x, self.y)
#         return self.x, self.y
#
#     def recover_generation(self):
#         self.recover_count -= 1
#         if self.recover_count <= 0:
#             self.recovered = True
#             self.infected = False
#             self.recover_count = 10
#             if ca.use_immunity:
#                 self.immune = True
#
#     def immunity_generation(self):
#         if self.immune:
#             self.immune_count -= 1
#             if self.immune_count <= 0:
#                 self.immune = False
#                 self.immune_count = self.original_immune
#
#     def movement(self):
#         def nothing():
#             pass
#
#         # mvmt = 5
#         mvmt = random.randint(0, 50)
#
#         def north():
#             self.y -= mvmt
#
#         def northeast():
#             self.x += mvmt
#             self.y -= mvmt
#
#         def east():
#             self.x += mvmt
#
#         def southeast():
#             self.x += mvmt
#             self.y += mvmt
#
#         def south():
#             self.y += mvmt
#
#         def southwest():
#             self.x -= mvmt
#             self.y += mvmt
#
#         def west():
#             self.x -= mvmt
#
#         def northwest():
#             self.x -= mvmt
#             self.y -= mvmt
#
#         instructions = {
#             0: nothing,
#             1: north,
#             2: northeast,
#             3: east,
#             4: southeast,
#             5: south,
#             6: southwest,
#             7: west,
#             8: northwest
#         }
#
#         rand = random.randint(0, 8)
#         instructions[rand]()  # like a switch case condition - for constant time complexity
#         # print(self.x, self.y)


root = tk.Tk()
root.title('Main Window')
# root.geometry('600x400')
# root.geometry('400x400')
# window = gui_Main_Window(root)
# window = SIR_Param(root)
window = gui_CA_Param(root)

root.mainloop()
