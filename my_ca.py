import random
import numpy as np
import matplotlib.pyplot as plt
import time
from matplotlib.animation import FuncAnimation


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

        """
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
        """

        def north():
            self.y -= 5

        def northeast():
            self.x += 5
            self.y -= 5

        def east():
            self.x += 5

        def southeast():
            self.x += 5
            self.y += 5

        def south():
            self.y += 5

        def southwest():
            self.x -= 5
            self.y += 5

        def west():
            self.x -= 5

        def northwest():
            self.x -= 5
            self.y -= 5

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
            rand_x, rand_y = self.rand_coordinate_generator()
            self.cell_object_dict[element] = cell(rand_x, rand_y)  # need to create random coordinates

    def rand_coordinate_generator(self):
        """Generates random coordinates for cells being generated"""
        rand_x = random.randint(0, self.size_x)
        rand_y = random.randint(0, self.size_y)
        return rand_x, rand_y

    def update_position(self):
        """For each cell object, movement function will be called to see where the cell will move, and the x coordinate list and y coordinate list will be returned"""
        loc_x = []
        loc_y = []

        for cell_obj_name in self.cell_list:  # for each cell object name ie. 'cell1', 'cell2' etc, use the name as a dictionary key and run movement function and get location
            self.cell_object_dict[cell_obj_name].movement()
            loc_x.append(self.cell_object_dict[cell_obj_name].location()[0])
            loc_y.append(self.cell_object_dict[cell_obj_name].location()[1])

        return loc_x, loc_y

    def cells_touch(self):
        pass

    def new_generation(self):
        """Main definition for running program. For the number of generations to simulate, call self.update_position() to get new coordinate lists"""
        x_coordinates = []
        y_coordinates = []

        for i in range(
                self.generations):
            x_list, y_list = self.update_position()

            # check if cells touch here, then can adjust objects if need

            x_coordinates.append(x_list)
            y_coordinates.append(y_list)

        x = np.array(x_coordinates)
        y = np.array(y_coordinates)

        # fig, ax = plt.subplots()
        plt.figure("graph")

        for i in range(self.generations):
            plt.xlim(0, self.size_x)
            plt.ylim(0, self.size_y)
            plt.scatter(x[i], y[i])
            plt.draw()
            plt.pause(0.00000001)
            plt.clf()


ca = cellular_automata(100, 1000, 600, 300)
ca.new_generation()
