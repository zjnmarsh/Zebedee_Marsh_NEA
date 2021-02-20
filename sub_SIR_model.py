import matplotlib.pyplot as plt
import pandas as pd
import sub_sql_functions as my_sql


class QueueSimulation:

    def __init__(self, n, s_list, i_list, r_list, b_list, g_list, t, current_id):
        self.n = n  # number of simulations to be run
        self.parameters = []
        for i in range(n):
            self.parameters.append([s_list[i], i_list[i], r_list[i], b_list[i], g_list[i], t, i + 1])
            my_sql.sir_enter_param(current_id, [s_list[i], i_list[i], r_list[i], b_list[i], g_list[i], t])
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
            name = "output" + str(f) + ".xls"
            df.to_excel(name, sheet_name='output')

        export_to_excel()
        plt.plot(timearray, solver_result[0], label="S(t)")
        plt.plot(timearray, solver_result[1], label="I(t)")
        plt.plot(timearray, solver_result[2], label="R(t)")


class plot_graph:

    def __init__(self, ta, s, i, r):
        # deconstruct file here
        self.timearray = ta
        self.sus = s
        self.inf = i
        self.rec = r

    def plot(self):
        plt.plot(self.timearray, self.sus, label="S(t)")
        plt.plot(self.timearray, self.inf, label="I(t)")
        plt.plot(self.timearray, self.rec, label="R(t)")
        plt.show()
