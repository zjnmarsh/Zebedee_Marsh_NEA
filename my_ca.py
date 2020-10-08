# might have to adjust class so cell locations generated on demand

import random
import numpy as np
import matplotlib.pyplot as plt
import time
from matplotlib.animation import FuncAnimation
import pandas as pd
import matplotlib


class cell:
    """Each cell will be a class instance of this class"""

    def __init__(self, x, y, infected):
        self.x = x
        self.y = y
        self.infected = infected
        self.recovered = False
        self.recover_count = 5 # default - can be changed
        # self.infection_rate = i

    def cell_test_function(self):
        return self.x, self.y, self.infected

    def location(self):
        # print(self.x, self.y)
        return self.x, self.y

    def recover_generation(self):
        self.recover_count -= 1
        if self.recover_count <= 0:
            self.recovered = True
            self.infected = False

    def movement(self):
        def nothing():
            pass

        # mvmt = 5
        mvmt = random.randint(0, 10)

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


class counter:
    def __init__(self):
        self.count = 0

    def increase(self):
        self.count += 1

    def get_count(self):
        return self.count


mycount = counter()


class cellular_automata:
    """Main class to run function"""

    def __init__(self, no_cells, generations, size_x, size_y, infection_radius, infected, r_i):
        """Creates list of how every many cells the user inputs so a list will look like ['cell1','cell2','cell3'...]. Each
        element in that list will then be used as a dictionary key where the definition will be a class instance of cell. Each
        class instance will be created with a random x and y coordinate, and an infected status."""
        self.number_of_cells = no_cells
        self.number_of_infected = infected
        self.infection_radius = infection_radius
        self.generations = generations
        self.cell_list = []
        self.cell_object_dict = {}
        self.size_x = size_x
        self.size_y = size_y
        self.full_list = []
        self.r_i = r_i
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
                                                  infected_status)  # creates a dictionary of cell objects

    def collect_data(self):
        """For each generation, appends a list with cell name, x coordinate, y coordinate and infection status to a master list
        This function is needed for exporting to excel"""
        cell_list = []
        for cell_object in self.cell_object_dict:
            x, y, infected = self.cell_object_dict[cell_object].cell_test_function()
            cell_list.append([cell_object, x, y, infected])
        np_cell_list = np.array(cell_list)

        self.full_list.append(cell_list)  # full list of cells and their status assigned to this variable

        return np_cell_list

    def export_to_excel(self):
        """Exports cell name and cell infection status with each new generation"""
        name = []
        x = []
        y = []
        inf = []
        rec = []

        for generation in range(len(self.full_list)):
            gen_inf = []
            for cell in range(self.number_of_cells):
                gen_inf.append(self.full_list[generation][cell][3])
            inf.append(gen_inf)

        data = {'Cell name': self.cell_list}  # dictionary containing cell names and infection statius
        for generation in range(len(self.full_list)):
            name = "generation" + str(generation)
            data[name] = inf[generation]

        df = pd.DataFrame(data)
        name = "ca_output.xlsx"
        df.to_excel(name, sheet_name='output')

    def rand_coordinate_generator(self):
        """Generates random coordinates for cells being generated"""
        rand_x = random.randint(0, self.size_x)
        rand_y = random.randint(0, self.size_y)
        return rand_x, rand_y

    def update_position(self):
        """For each cell object, movement function will be called to see where the cell will move, and the x coordinate list and y coordinate list will be returned"""
        loc_x = []
        loc_y = []
        infected = []
        recovered = []

        for cell_obj_name in self.cell_list:  # for each cell object name ie. 'cell1', 'cell2' etc, use the name as a dictionary key and run movement function and get location
            self.cell_object_dict[cell_obj_name].movement()
            loc_x.append(self.cell_object_dict[cell_obj_name].location()[0])
            loc_y.append(self.cell_object_dict[cell_obj_name].location()[1])
            infected.append(self.cell_object_dict[cell_obj_name].infected)
            recovered.append(self.cell_object_dict[cell_obj_name].recovered)

        self.collect_data()

        return loc_x, loc_y, infected, recovered

    def cells_touch(self):  # need to change to put all infected in a list, THEN compare susceptible otherwise not proper
        """If another cell in in a certain radius of an infected cell, it will become infected. To be changed"""
        infected_locations = []  # list of tuples of infected cells
        for cell_name in self.cell_list:
            if self.cell_object_dict[cell_name].infected:
                infected_locations.append(self.cell_object_dict[cell_name].location())
            else:
                sus_x, sus_y = self.cell_object_dict[cell_name].location()  # location of susceptible cell
                for infected_tuple in infected_locations:
                    if (sus_x - infected_tuple[0]) ** 2 + (
                            sus_y - infected_tuple[1]) <= self.infection_radius ** 2:  # equation of a circle
                        self.cell_object_dict[cell_name].infected = True  # need to chance for chance


    def cell_recovery(self):
        for cell_name in self.cell_list:
            cell_obj = self.cell_object_dict[cell_name]
            if cell_obj.recovered == False and cell_obj.infected == True:
                cell_obj.recover_generation()

    def new_generation(self):
        """Main definition for running program. For the number of generations to simulate, call self.update_position() to get new coordinate lists"""

        # x_coordinates = []
        # y_coordinates = []

        coordinates = []

        # x_sus_full = []
        # y_sus_full = []
        # x_inf_full = []
        # y_inf_full = []
        # x_rec_full = []
        # y_rec_full = []

        sus_full = []
        inf_full = []
        rec_full = []

        for i in range(
                self.generations):

            if i % 50 == 0:
                print("Generating generation " + str(i))

            x_list, y_list, infected, recovered = self.update_position()

            # check if cells touch here, then can adjust objects if need
            self.cells_touch()

            # recovery function
            self.cell_recovery()

            # infected and susceptible cells go in separate lists for plotting
            # x_sus = []
            # y_sus = []
            # x_inf = []
            # y_inf = []
            # x_rec = []
            # y_rec = []

            gen_sus = []
            gen_inf = []
            gen_rec = []


            # for inf in range(len(self.cell_list)):
            #     # print(inf)
            #     if infected[inf]:
            #         x_inf.append(x_list[inf])
            #         y_inf.append(y_list[inf])
            #     elif recovered[inf]:
            #         x_rec.append(x_list[inf])
            #         y_rec.append(y_list[inf])
            #     else:
            #         x_sus.append(x_list[inf])
            #         y_sus.append(y_list[inf])

            for inf in range(len(self.cell_list)):
                if infected[inf]:
                    gen_inf.append([x_list[inf], y_list[inf]])
                elif recovered[inf]:
                    gen_rec.append([x_list[inf], y_list[inf]])
                else:
                    gen_sus.append([x_list[inf], y_list[inf]])



            # x_sus_full.append(x_sus)
            # y_sus_full.append(y_sus)
            # x_inf_full.append(x_inf)
            # y_inf_full.append(y_inf)
            # x_rec_full.append(x_rec)
            # y_rec_full.append(y_rec)

            sus_full.append(gen_sus)
            inf_full.append(gen_inf)
            rec_full.append(gen_rec)

            # x_coordinates.append(x_list)
            # y_coordinates.append(y_list)

            coordinates.append([x_list, y_list])

            # print(sus_full)

        self.export_to_excel()

        # list comprehension

        def animate(i):
            # plt.xlim(0, self.size_x)
            # plt.ylim(0, self.size_y)
            plt.xlim(0, 600)
            plt.ylim(0, 600)
            mycount.increase()
            if mycount.get_count() > self.generations:
                print("End of simulation")
                time.sleep(10000)
            else:
                plt.cla()

                x_sus_full = [cell[0] for cell in sus_full[i]]
                y_sus_full = [cell[1] for cell in sus_full[i]]
                x_inf_full = [cell[0] for cell in inf_full[i]]
                y_inf_full = [cell[1] for cell in inf_full[i]]
                x_rec_full = [cell[0] for cell in rec_full[i]]
                y_rec_full = [cell[1] for cell in rec_full[i]]

                # print(x_sus_full)
                # print(y_sus_full)

                # plt.scatter(x_sus_full[i], y_sus_full[i], color='blue')
                # plt.scatter(x_inf_full[i], y_inf_full[i], color='red')
                # plt.scatter(x_rec_full[i], y_rec_full[i], color='purple')
                plt.scatter(x_sus_full, y_sus_full, color='blue')
                plt.scatter(x_inf_full, y_inf_full, color='red')
                plt.scatter(x_rec_full, y_rec_full, color='purple')



        plt.xlim(0, self.size_x)
        plt.ylim(0, self.size_y)

        ani = FuncAnimation(plt.gcf(), animate, interval=100)

        # ani.save('video.mp4', writer='ffmpeg', fps=30, dpi=250)

        plt.tight_layout()
        plt.show()


# self, no_cells, generations, size_x, size_y, infection_radius, infected-1, recovered can be infected


# ca = cellular_automata(5, 5, 10, 10, 2, 3)
# ca = cellular_automata(500, 1000, 1000, 1000, 10, 2, True)
# ca = cellular_automata(100, 250, 250, 300, 10, 2)
# ca = cellular_automata(250, 250, 500, 500, 5, 2)
ca = cellular_automata(50, 100, 100, 100, 2, 5, True)
ca.new_generation()
