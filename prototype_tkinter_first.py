import tkinter as tk
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt


class Gui(tk.Tk):

    def __init__(self, *args,
                 **kwargs):  # *args - pass through any number of variables; **kwargs - pass through dictionaries
        tk.Tk.__init__(self, *args, **kwargs)  # initialising tkinter
        container = tk.Frame(self)  # the frame of the window

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)  # 0 sets minimum size, weight shows priority
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}  # allows application to open different types of pages easily

        for F in (StartPage, GUI_SIR):  # all pages need to be listed here

            print(F)

            frame = F(container, self)

            self.frames[F] = frame  # saving classes to dictionary, "loading it in"

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(GUI_SIR)  # start page is shown first

    def show_frame(self, cont):
        frame = self.frames[cont]  # looks for cont in dict
        frame.tkraise()  # which is then raised


class StartPage(tk.Frame):

    def __init__(self, parent,
                 controller):  # parent class is Gui, controller class is main class, allowing show_frame to be called
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Start Page")
        label.pack(pady=10, padx=10)
        button1 = tk.Button(self, text="SIR Model", command=lambda: controller.show_frame(SIR_model))
        button1.pack()


class GUI_SIR(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # button2 = tk.Button(self, text="Start Page", command=lambda: controller.show_frame(StartPage))
        # button2.grid(column=0, row=0)

        s_input_field = tk.Entry(self)
        i_input_field = tk.Entry(self)
        r_input_field = tk.Entry(self)
        enter_button = tk.Button(self, text="Submit", command=self.run_sir)

        s_input_field.grid(column=0, row=0)
        i_input_field.grid(column=0, row=1)
        r_input_field.grid(column=0, row=2)
        # self.input_parameters = [s_input_field.get(), i_input_field.get(), r_input_field.get()]
        # self.s = s_input_field.get()
        enter_button.grid(column=0, row=3)

    def run_sir(self):
        print()
        print(type(self.s))


class SIR_model:

    def __init__(self):
        pass

    def SIR_model(self, s0, i0, r0, beta, gamma, t):
        """
        :param s: number of susceptible people
        :param i: number of infected people
        :param r: number of recovered people
        :param b: transmission rate of an individual
        :param g: recovery rate of an individual
        :param t: how long the simulation should run for
        """
        t = np.linspace(0, t,
                        t * 10)  # creates a time array at the points where the differential equations will be calculated, (start, end, number of timepoints)
        N = s0 + i0 + r0  # total population
        y0 = (s0, i0, r0)  # initial conditions

        def eqns(y0, t, beta, gamma):
            S, I, R = y0
            dsdt = -(beta * S * I) / N  # rate of change of susceptible individuals
            didt = ((beta * S * I) / N) - gamma * I  # rate of change of infected individuals
            drdt = gamma * I  # rate of change of recovered individuals
            return dsdt, didt, drdt

        result = odeint(eqns, y0, t, args=(beta, gamma))
        print(result)
        solution = np.array(result)
        # print(solution)
        plt.figure(figsize=[6, 4])
        plt.plot(t, solution[:, 0], label="S(t)")
        plt.plot(t, solution[:, 1], label="I(t)")
        plt.plot(t, solution[:, 2], label="R(t)")
        plt.show()


# sir_model = SIR_model()
# sir_model.SIR_model(999, 1, 0, 0.2, 0.1, 160)

app = Gui()
app.mainloop()
