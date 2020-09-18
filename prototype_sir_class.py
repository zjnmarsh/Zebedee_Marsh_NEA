from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt


class SIR_model:

    def __init__(self):
        # self.y0 = (0,0,0)
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

        plt.figure(f)
        # t = np.linspace(0, t,
        #                 t * 10)  # creates a time array at the points where the differential equations will be calculated, (start, end, number of timepoints)
        N = s0 + i0 + r0  # total population
        self.y0 = (s0, i0, r0)  # initial conditions

        # print(t)
        timearray = list(range(1, int(t))) # creates time array

        # def eqns(y0, t, beta, gamma):
        def eqns(param):
            # e = 0.75
            e = 0
            S, I, R = param
            dsdt = (-(beta * S * I) / N) + (e * R)  # rate of change of susceptible individuals
            didt = ((beta * S * I) / N) - gamma * I  # rate of change of infected individuals
            drdt = (gamma * I) - (e * R)  # rate of change of recovered individuals
            return dsdt, didt, drdt

        def solver():
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

        # result = odeint(eqns, y0, t, args=(beta, gamma))
        solver_result = solver()
        print(solver_result)

        plt.plot(timearray, solver_result[0], label="S(t)")
        plt.plot(timearray, solver_result[1], label="I(t)")
        plt.plot(timearray, solver_result[2], label="R(t)")


        # solution = np.array(result)
        # # print(solution)
        # plt.figure(figsize=[6, 4])
        # plt.plot(t, solution[:, 0], label="S(t)")
        # plt.plot(t, solution[:, 1], label="I(t)")
        # plt.plot(t, solution[:, 2], label="R(t)")
        # # plt.show()


# sir_model = SIR_model()
# sir_model.SIR_model(999, 1, 0, 0.2, 0.1, 160, 1)
# plt.show()

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


# queue = QueueSimulation(2, [999, 599], [1, 3], [0, 0], [0.2, 0.4], [0.1,0.1], 100)
# queue = QueueSimulation(1, [999], [1], [0], [0.4], [0.1], 200)
queue = QueueSimulation(1, [1], [0.01], [0], [0.4], [0.1], 100)

queue.run_simulation()
