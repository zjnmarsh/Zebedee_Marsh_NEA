# grid = [None] * 10

# grid = [0,1,0,0,1,1,0,1,1,0]

class CA:
    def __init__(self, width, generations):
        self.ruleset = [0, 1, 1, 1, 1, 0, 1, 1]
        self.width = width
        self.cells = [0] * width
        self.new_cells = [None] * width
        self.cells[int((width / 2) - 1)] = 1
        self.generations = generations

    def rules(self, a, b, c, i):
        index = int((a + b + c), 2)
        # print(a,b,c)
        ruleset = [0, 1, 0, 1, 1, 0, 1, 0]
        # print(index, ruleset[index])
        self.new_cells[i] = ruleset[index]

    def ca(self):
        print(self.cells)
        for gen in range(self.generations):
            for i in range(self.width):
                a = str(self.cells[((i - 1) % self.width)])
                b = str(self.cells[i])
                c = str(self.cells[((i + 1) % self.width)])
                # print(a,b,c)
                self.rules(a, b, c, i)
            self.cells = self.new_cells
            self.new_cells = [None]*self.width
            print(self.cells)


ca = CA(100,100)
ca.ca()
