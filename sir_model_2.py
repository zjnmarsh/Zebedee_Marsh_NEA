class SIR_model:
    def __init__(self,s,i,r,population,b,k):
        self.population = population
        self.susceptible = s
        self.infected = i
        self.recovered = r
        self.beta = b    # rate of transmission
        self.gamma = k    # rate of recovery

    def sir_model(self):
        # rate of change of susceptible individuals
        dsdt = -(self.beta*self.susceptible*self.infected)/self.population
        # rate of change of infected individuals
        didt = ((self.beta*self.susceptible*self.infected)/self.population) - self.gamma*self.infected
        # rate of change of recovered individuals
        drdt = self.gamma*self.infected
