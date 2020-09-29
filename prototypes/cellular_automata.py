class cells:

    def __init__(self, c, p, s, i, r):
        self.carrying_capacity = c    # maximum population of a cell
        self.total_population = p
        self.s_spopulation = s    # susceptible sub-population
        self.i_spopulation = i    # infected sub-population
        self.r_spopulation = r    # recovered sub-population
