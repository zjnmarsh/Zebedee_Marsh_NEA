import random
import numpy as np
import matplotlib.pyplot as plt
import time
from matplotlib.animation import FuncAnimation
#import pandas as pd

class cell:
    """Each cell will be a class instance of this class"""

    def __init__(self, x, y, infected):
        self.x = x
        self.y = y
        self.infected = infected
        # self.infection_rate = i

    def cell_test_function(self):
        return self.x, self.y, self.infected

    def location(self):
        # print(self.x, self.y)
        return self.x, self.y

    def movement(self):
        def nothing():
            pass

        mvmt = 1

        def north():
            self.y -= mvmt

        def northeast():
            self.x += mvmt
            self.y -= mvmt

        def east():
            self.x += mvmt

        def southeast():
            self.x += mvmt
            self.y += mvmt

        def south():
            self.y += mvmt

        def southwest():
            self.x -= mvmt
            self.y += mvmt

        def west():
            self.x -= mvmt

        def northwest():
            self.x -= mvmt
            self.y -= mvmt

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
        # print(self.x, self.y)

class cellular_automata:
    """Main class to run function"""

    def __init__(self, no_cells, generations, size_x, size_y, infection_radius, infected):
        """Creates list of how every many cells the user inputs so a list will look like ['cell1','cell2','cell3'...]. Each
        element in that list will then be used as a dictionary key where the definition will be a class instance of cell. Each
        class instance will be created with a random x and y coordinate, and an infected status."""
        self.number_of_infected = infected
        self.infection_radius = infection_radius
        self.generations = generations
        self.cell_list = []
        self.cell_object_dict = {}
        self.size_x = size_x
        self.size_y = size_y
        self.full_list = []
        for i in range(no_cells):
            self.cell_list.append(("cell" + str(i)))

        infected_counter = 0
        for element in self.cell_list:  # creates user inputted number of infected cells first, then creates normal cells
            infected_counter += 1
            infected_status = False
            if infected_counter < self.number_of_infected:
                infected_status = True
            rand_x, rand_y = self.rand_coordinate_generator()
            self.cell_object_dict[element] = cell(rand_x, rand_y,
                                                  infected_status)  # creates a dictionary of cell objects || Need to create function to generate randomly infected cells

    def ca_test_function(self):
        """Test function to get information on a cell"""
        cell_list = []
        for cell_object in self.cell_object_dict:
            x, y, infected = self.cell_object_dict[cell_object].cell_test_function()
            cell_list.append([cell_object, x, y, infected])
        np_cell_list = np.array(cell_list)

        self.full_list.append(cell_list)

        return np_cell_list

    # def export_to_excel(self):
    #     name = []
    #     x = []
    #     y = []
    #     inf = []
    #     # for generation in self.full_list:
    #     #     # name.append(generation[0])
    #     #     print(generation[0])
    #     #     print(generation[1])
    #     for generation in range(len(self.full_list)):
    #         for cell in range(len(self.full_list)):
    #             print(self.full_list[generation][cell][1])
    #             name.append(self.full_list[generation][cell][0])
    #             x.append(self.full_list[generation][cell][1])
    #             y.append(self.full_list[generation][cell][2])
    #             inf.append(self.full_list[generation][cell][3])
    #
    #     print(name)
    #     print(x)
    #     print(y)
    #     print(inf)

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

        self.ca_test_function()

        return loc_x, loc_y

    def cells_touch(self):
        infected_locations = [] # list of tuples of infected cells
        for cell_name in self.cell_list:
            if self.cell_object_dict[cell_name].infected:
                infected_locations.append(self.cell_object_dict[cell_name].location())
            else:
                sus_x, sus_y = self.cell_object_dict[cell_name].location() # location of susceptible cell
                for infected_tuple in infected_locations:
                    if (sus_x - infected_tuple[0])**2 + (sus_y - infected_tuple[1]) <= self.infection_radius**2: # equation of a circle
                        self.cell_object_dict[cell_name].infected = True  # need to chance for chance


    def new_generation(self):
        """Main definition for running program. For the number of generations to simulate, call self.update_position() to get new coordinate lists"""

        x_coordinates = []
        y_coordinates = []

        for i in range(
                self.generations):
            x_list, y_list = self.update_position()

            # check if cells touch here, then can adjust objects if need
            # self.cells_touch()

            x_coordinates.append(x_list)
            y_coordinates.append(y_list)

        x = np.array(x_coordinates)
        y = np.array(y_coordinates)

        # self.export_to_excel()

        # fig, ax = plt.subplots()
        plt.figure("graph")

        for i in range(self.generations):
            plt.xlim(0, self.size_x)
            plt.ylim(0, self.size_y)
            plt.scatter(x[i], y[i])
            plt.draw()
            plt.pause(0.00000001)
            # plt.pause(1)
            plt.clf()

# self, no_cells, generations, size_x, size_y, infection_radius, infected-1
ca = cellular_automata(5, 5, 10, 10, 2, 3)

# ca = cellular_automata(100, 1000, 600, 300, 5, 5)
ca.new_generation()
