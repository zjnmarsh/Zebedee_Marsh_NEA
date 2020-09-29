import random
import numpy as np
import matplotlib.pyplot as plt
import time


class cell:
    """Each cell will be a class instance of this class"""

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

        rand = random.randint(0, 8)
        instructions[rand]()  # like a switch case condition - for constant time complexity


class cellular_automata:
    """Main class to run function"""
    def __init__(self, no_cells, generations, size_x, size_y):
        """Creates list of how every many cells the user inputs so a list will look like ['cell1','cell2','cell3'...]. Each
        element in that list will then be used as a dictionary key where the definition will be a cell object"""
        # self.number_cells = no_cells  # needs to create cell objects based on user input
        self.generations = generations
        self.cell_list = []
        self.cell_object_dict = {}
        self.size_x = size_x
        self.size_y = size_y
        for i in range(no_cells):
            self.cell_list.append(("cell" + str(i)))
        for element in self.cell_list:
            self.cell_object_dict[element] = cell(0, 0)  # need to create random coordinates

        # print(self.cell_object_list)

        # self.cell1 = cell(4,5)
        # self.cell2 = cell(7,2)
        # self.cell3 = cell(9,4)
        # print(self.cell1)

    def update_position(self):

        loc_x = []
        loc_y = []

        # self.cell1.movement()
        # loc_x.append(self.cell1.location()[0])
        # loc_y.append(self.cell1.location()[1])
        # self.cell2.movement()
        # loc_x.append(self.cell2.location()[0])
        # loc_y.append(self.cell2.location()[1])
        # self.cell3.movement()
        # loc_x.append(self.cell3.location()[0])
        # loc_y.append(self.cell3.location()[1])

        for cell_obj_name in self.cell_list:  # for each cell object name ie. 'cell1', 'cell2' etc, use the name as a dictionary key and run movement function and get location
            self.cell_object_dict[cell_obj_name].movement()
            loc_x.append(self.cell_object_dict[cell_obj_name].location()[0])
            loc_y.append(self.cell_object_dict[cell_obj_name].location()[1])

        return loc_x, loc_y

        # np_x = np.array([])
        # np_y = np.array([])

    def new_generation(self):
        x_coordinates = []
        y_coordinates = []

        for i in range(self.generations):  # for the number generations, append new x and y coordinates for however many cells
            x_list, y_list = self.update_position()  # arrays with positions for new generation
            # print(x_list)
            # print(y_list)

            x_coordinates.append(x_list)
            y_coordinates.append(y_list)

            # np_x = np.concatenate((np_x, x_list))
            # np_y = np.concatenate((np_y, y_list))

        x = np.array(x_coordinates)
        y = np.array(y_coordinates)

        # print(x_coordinates)
        # print(y_coordinates)

        print(x[0])


        for i in range(self.generations):
            plt.xlim(-self.size_x, self.size_x)
            plt.ylim(-self.size_y, self.size_y)
            plt.scatter(x_coordinates[i], y_coordinates[i])
            plt.draw()
            plt.pause(0.00000001)
            plt.clf()




ca = cellular_automata(100, 100, 50, 30)
ca.new_generation()
