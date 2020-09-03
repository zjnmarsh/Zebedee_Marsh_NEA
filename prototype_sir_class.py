from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt


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


sir_model = SIR_model()
# sir_model.SIR_model(999, 1, 0, 0.2, 0.1, 160)


class QueueSimulation:

    def __init__(self, n, s_list, i_list, r_list, b_list, g_list):
        self.n = n  # number of simulations to be run
        self.parameters = []
        for i in range(n):
            self.parameters.extend((s_list[i], i_list[i], r_list[i], b_list[i], g_list[i]))

    def foo(self):
        pass


queue = QueueSimulation(2, [999, 599], [1, 3], [0, 0], [0.2, 0.4], [0.1,0.1])
queue.foo()
