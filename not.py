from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt


class SIR_model:
    def __init__(self,s,i,r,population,b,k):
        """
        The initial conditions of the simulation are set here
        beta and gamma are constant
        at the moment, population is constant (ie. not accounting for birth rate, death rate, migration...
        """
        self.population = population
        self.susceptible = s
        self.infected = i
        self.recovered = r
        self.beta = b    # rate of transmission ie. contact rate
        self.gamma = k    # rate of recovery
        self.t = np.linspace(0, 160, 160)
        self.S = 0
        self.I = 0
        self.R = 0

    def sir_model(self, y, t, n, beta, gamma):
        print(y)
        self.S, self.I, self.R = y
        # rate of change of susceptible individuals
        dsdt = -(self.beta*self.susceptible*self.infected)/self.population
        # rate of change of infected individuals
        didt = ((self.beta*self.susceptible*self.infected)/self.population) - self.gamma*self.infected
        # rate of change of recovered individuals
        drdt = self.gamma*self.infected
        return dsdt, didt, drdt

    def derive(self):
        y0 = self.susceptible, self.infected, self.recovered    # initial conditions vector
        # print(self.t)
        # ret = odeint(self.sir_model, y0, self.t, args=(self.population, self.beta, self.gamma))
        ret = odeint(self.sir_model, (999, 1, 0), np.linspace(0, 160, 160), args=(1000, 0.2, 0.1))

        self.S, self.I, self.R = ret.T
        self.plot()

    def plot(self):
        # print(S)
        fig = plt.figure(facecolor='w')
        ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)
        # print(self.S)
        ax.plot(self.t, self.S / 1000, 'b', alpha=0.5, lw=2, label='Susceptible')
        # ax.plot(t, I / 1000, 'r', alpha=0.5, lw=2, label='Infected')
        # ax.plot(t, R / 1000, 'g', alpha=0.5, lw=2, label='Recovered with immunity')
        ax.set_xlabel('Time /days')
        ax.set_ylabel('Number (1000s)')
        ax.set_ylim(0, 1.2)
        ax.yaxis.set_tick_params(length=0)
        ax.xaxis.set_tick_params(length=0)
        ax.grid(b=True, which='major', c='w', lw=2, ls='-')
        legend = ax.legend()
        legend.get_frame().set_alpha(0.5)
        for spine in ('top', 'right', 'bottom', 'left'):
            ax.spines[spine].set_visible(False)
        plt.show()


sir = SIR_model(999,1,0,1000,0.2,1./10)
sir.derive()
