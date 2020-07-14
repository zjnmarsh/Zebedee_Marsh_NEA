class SIR_model:
    def __init__(self,s,i,r,population,b,k):
        self.susceptible = s / population
        self.infected = i / population
        self.recovered = r / population
        self.infection_rate = b
        self.recovery_rate = k

    def equations(self):
        # rate if change of susceptible individuals
        dsdt = -self.infection_rate * self.susceptible * self.infected
        # rate of change of infected individuals
        didt = self.infection_rate * self.susceptible * self.infected - (self.recovery_rate * self.infected)
        # rate of change of recovered individuals
        drdt = self.recovery_rate * self.infected
        return dsdt, didt, drdt




sir = SIR_model(997,3,0,1000,2,1)
print(sir.equations())
