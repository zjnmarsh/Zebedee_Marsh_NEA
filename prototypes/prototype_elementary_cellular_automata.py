# grid = [None] * 10

# grid = [0,1,0,0,1,1,0,1,1,0]

import time


class CA:
    def __init__(self, width, generations):
        self.ruleset = [0, 1, 1, 1, 1, 0, 1, 1]
        self.width = width
        self.cells = [0] * width
        self.new_cells = [None] * width
        self.cells[int((width / 2) - 1)] = 1
        self.generations = generations
        self.cell_timeline = []

    def rules(self, a, b, c, i):
        index = int((a + b + c), 2)
        # print(a,b,c)
        ruleset = [0, 1, 0, 1, 1, 0, 1, 0]
        # print(index, ruleset[index])
        self.new_cells[i] = ruleset[index]

    def draw(self):
        output = ""
        for cell_state in self.cell_timeline:
            for element in cell_state:
                if element == 0:
                    output += " " + " "
                else:
                    output += "X" + " "
            print(output)
            time.sleep(0.1)
            output = ""

    def ca(self):
        # print(self.cells)
        for gen in range(self.generations):
            for i in range(self.width):
                a = str(self.cells[((i - 1) % self.width)])
                b = str(self.cells[i])
                c = str(self.cells[((i + 1) % self.width)])
                # print(a,b,c)
                self.rules(a, b, c, i)
            self.cells = self.new_cells
            self.cell_timeline.append(self.cells)
            self.new_cells = [None] * self.width
            # print(self.cells)
        self.draw()


ca = CA(100, 100)
ca.ca()
