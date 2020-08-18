from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt


# class SIR_model:
#     def __init__(self, s, i, r, population, b, k):
#         """
#         The initial conditions of the simulation are set here
#         beta and gamma are constant
#         at the moment, population is constant (ie. not accounting for birth rate, death rate, migration...
#         """
#         self.population = population
#         self.susceptible = s
#         self.infected = i
#         self.recovered = r
#         self.beta = b  # rate of transmission ie. contact rate
#         self.gamma = k  # rate of recovery
#         self.initial_conditions = (self.susceptible, self.infected, self.recovered)
#         self.t = np.linspace(0, 160, 160)
#
#     def solver(self):
#
#         def eqns(y, *args):
#             S, I, R = y
#             # rate of change of susceptible individuals
#             dsdt = -(self.beta * self.susceptible * self.infected) / self.population
#             # rate of change of infected individuals
#             didt = ((self.beta * self.susceptible * self.infected) / self.population) - self.gamma * self.infected
#             # rate of change of recovered individuals
#             drdt = self.gamma * self.infected
#             return dsdt, didt, drdt
#
#         result = odeint(eqns, self.initial_conditions, self.t, args=(self.beta, self.gamma))
#         solution = np.array(result)
#         print(solution)
#
#         plt.figure(figsize=[6,4])
#         plt.plot(self.t, solution[:, 0], label="susceptible")
#         plt.show()
#
#     # def calculate(self):
#     #     results = odeint(self.eqns, self.initial_conditions, self.t, args=(self.population, self.beta, self.gamma))
#     #     print(results)
#     #
#     #     fig = plt.figure(facecolor='w')
#     #     ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)
#     #     ax.plot(self.t, results[0] / 1000, 'b', alpha=0.5, lw=2, label='Susceptible')
#
#
# sir = SIR_model(999, 1, 0, 1000, 0.2, 1. / 10)
# sir.solver()

def SIR_model(s0, i0, r0, beta, gamma, t):
    """
    :param s: number of susceptible people
    :param i: number of infected people
    :param r: number of recovered people
    :param b: transmission rate of an individual
    :param g: recovery rate of an individual
    :param t: how long simulaiton should run for
    """
    t = np.linspace(0, t, t)  # creates a time array at the points where the differential equations will be calculated
    N = s0 + i0 + r0  # total population
    y0 = (s0, i0, r0)  # initial conditions

    def eqns(y0, t, beta, gamma):
        S, I, R = y0
        dsdt = -(beta * S * I) / N  # rate of change of susceptible individuals
        didt = ((beta * S * I) / N) - gamma * I  # rate of change of infected individuals
        drdt = gamma * I  # rate of change of recovered individuals
        return dsdt, didt, drdt

    result = odeint(eqns, y0, t, args=(beta, gamma))
    solution = np.array(result)
    print(solution)
    plt.figure(figsize=[6,4])
    plt.plot(t, solution[:, 0], label="S(t)")
    plt.plot(t, solution[:, 1], label="I(t)")
    plt.plot(t, solution[:, 2], label="R(t)")
    plt.show()


SIR_model(999, 1, 0, 0.2, 0.1, 160)

