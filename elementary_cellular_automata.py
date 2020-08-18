# grid = [None] * 10

# grid = [0,1,0,0,1,1,0,1,1,0]

class CA:
    def __init__(self, width, generations):
        self.ruleset = [0, 1, 1, 1, 1, 0, 1, 1]
        self.width = width
        self.cells = [0] * width
        self.new_cells = [None] * width
        self.cells[int((width / 2) - 1)] = 1

    def rules(self, a, b, c, i):
        index = int((a + b + c), 2)
        ruleset = [0, 1, 0, 1, 1, 0, 1, 0]
        self.new_cells[i] = ruleset[index]

    def ca(self):
        for i in range(self.width):
            a = str(self.cells[((i - 1) % self.width)])
            b = str(self.cells[i])
            c = str(self.cells[((i + 1) % self.width)])
            print(a,b,c)
            self.rules(a, b, c, i)
        print(self.cells)
        print(self.new_cells)


ca = CA(10)
ca.ca()
