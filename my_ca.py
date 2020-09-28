import random

class person:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # self.infection_rate = i

    def location(self):
        return (self.x, self.y)

    def movement(self):

        def nothing():
            pass
        def north():
            self.y -= 1
        def northeast():
            self.x += 1
            self.y -= 1
        def east():
            self.x += 1
        def southeast():
            self.x += 1
            self.y += 1
        def south():
            self.y += 1
        def southwest():
            self.x -= 1
            self.y += 1
        def west():
            self.x -= 1
        def northwest():
            self.x -= 1
            self.y -= 1

        instructions = {
            0: nothing,
            1: north,
            2: northeast,
            3: east,
            4: southeast,
            5: south,
            6: southwest,
            7: west,
            8: northwest
        }

        rand = random.randint(0,8)
        instructions[rand]()  # like a switch case condition - for good time complexity



cell1 = person(4,5)
cell2 = person(7,2)
cell3 = person(9,4)


def update_cells():

    loc_x = []
    loc_y = []

    cell1.movement()
    loc_x.append(cell1.location()[0])
    loc_y.append(cell1.location()[1])
    cell2.movement()
    loc_x.append(cell2.location()[0])
    loc_y.append(cell2.location()[1])
    cell3.movement()
    loc_x.append(cell3.location()[0])
    loc_y.append(cell3.location()[1])

    return loc_x, loc_y

# for i in range(10):
#     update_cells()



# for i in range(10):
#     x_list, y_list = update_cells()



