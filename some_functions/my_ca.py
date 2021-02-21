# might have to adjust class so cell locations generated on demand

import random
import numpy as np
import matplotlib.pyplot as plt
import time
from matplotlib.animation import FuncAnimation
import pandas as pd
import matplotlib
import csv
import json


class cell:
    """Each cell will be a class instance of this class"""

    def __init__(self, x, y, infected, d_r, d_i):
        self.x = x
        self.y = y
        self.infected = infected
        self.recovered = False
        self.recover_count = d_r  # default - can be changed - time until infected cell recovers
        self.immune = False
        self.immune_count = d_i
        self.original_immune = d_i
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
            self.recover_count = 10
            if ca.use_immunity == True:
                self.immune = True

    def immunity_generation(self):
        if self.immune == True:
            self.immune_count -= 1
            if self.immune_count <= 0:
                self.immune = False
                self.immune_count = self.original_immune

    def movement(self):
        def nothing():
            pass

        # mvmt = 5
        mvmt = random.randint(0, 50)

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

    def __init__(self, no_cells, generations, size_x, size_y, infection_radius, infected, r_i, d_r, immunity, d_i,
                 user_file):
        """Creates list of how every many cells the user inputs so a list will look like ['cell1','cell2','cell3'...]. Each
        element in that list will then be used as a dictionary key where the definition will be a class instance of cell. Each
        class instance will be created with a random x and y coordinate, and an infected status.
        r_i : recovered can be infected
        d_r : days until recovery
        """
        self.user_file = user_file
        self.use_immunity = immunity
        self.number_of_cells = no_cells
        self.number_of_infected = infected
        self.infection_radius = infection_radius
        self.generations = generations
        self.cell_list = []
        self.cell_object_dict = {}
        self.size_x = size_x
        self.size_y = size_y
        self.full_list = []
        self.r_i = r_i  # recovered can be infected
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
                                                  infected_status, d_r, d_i)  # creates a dictionary of cell objects

    # def collect_data(self):
    #     """For each generation, appends a list with cell name, x coordinate, y coordinate and infection status to a master list
    #     This function is needed for exporting to excel
    #     INDEPENDENT WITH export_to_excel"""
    #     cell_list = []
    #     for cell_object in self.cell_object_dict:
    #         x, y, infected = self.cell_object_dict[cell_object].cell_test_function()
    #         cell_list.append([cell_object, x, y, infected])
    #     np_cell_list = np.array(cell_list)
    #
    #     self.full_list.append(cell_list)  # full list of cells and their status assigned to this variable
    #
    #     return np_cell_list
    #
    # def export_to_excel(self):
    #     """Exports cell name and cell infection status with each new generation. RELIANT ON COLLECT_DATA
    #     INDEPENDENT WITH collect_data"""
    #     name = []
    #     x = []
    #     y = []
    #     inf = []
    #     rec = []
    #
    #     for generation in range(len(self.full_list)):
    #         gen_inf = []
    #         for cell in range(self.number_of_cells):
    #             gen_inf.append(self.full_list[generation][cell][3])
    #         inf.append(gen_inf)
    #
    #     data = {'Cell name': self.cell_list}  # dictionary containing cell names and infection statius
    #     for generation in range(len(self.full_list)):
    #         name = "generation" + str(generation)
    #         data[name] = inf[generation]
    #
    #     df = pd.DataFrame(data)
    #     name = "ca_output.xlsx"
    #     df.to_excel(name, sheet_name='output')

    def rand_coordinate_generator(self):
        """Generates random coordinates for cells being generated"""
        rand_x = random.randint(0, self.size_x)
        rand_y = random.randint(0, self.size_y)
        return rand_x, rand_y

    def export_data(self, sus_full, inf_full, rec_full, imm_full, lg_values, time_array):
        """Should export data in a format that it can be analysed and reused
        gen_imm empty when not using immunity, but shouldn't be a problem"""

        filename = "../other_files/ca_output.txt"
        with open(filename, 'w') as file:
            file.write(str(sus_full) + "\n")
            file.write(str(inf_full) + "\n")
            file.write(str(rec_full) + "\n")
            file.write(str(imm_full) + "\n")
            file.write(str(lg_values) + "\n")
            file.write(str(time_array) + "\n")

    def import_data(self):
        filename = "../other_files/ca_output.txt"
        with open(filename, 'r') as file:
            lines = [line.rstrip('\n') for line in file]

        if lines[-1] == "":
            del lines[-1]

        result = [json.loads(item) for item in lines]
        print(result)
        return result

    def update_position(self):
        """For each cell object, movement function will be called to see where the cell will move, and the x coordinate list and y coordinate list will be returned of the new generation"""
        loc_x = []
        loc_y = []
        infected = []
        recovered = []
        immune = []

        for cell_obj_name in self.cell_list:  # for each cell object name ie. 'cell1', 'cell2' etc, use the name as a dictionary key and run movement function and get location
            self.cell_object_dict[cell_obj_name].movement()
            loc_x.append(self.cell_object_dict[cell_obj_name].location()[0])
            loc_y.append(self.cell_object_dict[cell_obj_name].location()[1])
            infected.append(self.cell_object_dict[cell_obj_name].infected)
            recovered.append(self.cell_object_dict[cell_obj_name].recovered)
            immune.append(self.cell_object_dict[cell_obj_name].immune)

        # print(infected)
        # print(recovered)
        # print(immune)
        # print("------------")

        # self.collect_data()  # this function could be moved into the new generation class function

        return loc_x, loc_y, infected, recovered, immune

    def cells_touch(
            self):  # need to change to put all infected in a list, THEN compare susceptible otherwise not proper
        """If another cell in in a certain radius of an infected cell, it will become infected. To be changed"""
        infected_locations = []  # list of tuples of infected cells
        recovered_obj = []
        susceptible_obj = []
        for cell_name in self.cell_list:
            if self.cell_object_dict[cell_name].infected:
                infected_locations.append(self.cell_object_dict[cell_name].location())
            elif self.cell_object_dict[cell_name].recovered:
                recovered_obj.append(self.cell_object_dict[cell_name])  # holds recovered both with and without immunity
            else:
                susceptible_obj.append(self.cell_object_dict[cell_name])

        def touch(cell_obj):
            sus_x, sus_y = cell_obj.location()
            for infected_tuple in infected_locations:
                if (sus_x - infected_tuple[0]) ** 2 + (
                        sus_y - infected_tuple[1]) <= self.infection_radius ** 2:  # equation of a circle
                    # self.cell_object_dict[cell_name].infected = True  # need to chance for chance
                    # PROBLEM
                    cell_obj.infected = True
                    # print(f'{cell_obj} has been infected')
                    # cell is infected, LISTS ARE NOT UPDATED

        if self.r_i:  # if recovered can be infected - doesn't change immunity status but is currently dependent on it - CHANGE
            for recovered in recovered_obj:
                if not recovered.immune:
                    touch(recovered)
        for susceptible in susceptible_obj:
            if not susceptible.immune:
                touch(susceptible)

    def cell_recovery(self):
        """Cells automatically recover after a certain period of time"""
        for cell_name in self.cell_list:
            cell_obj = self.cell_object_dict[cell_name]
            if cell_obj.recovered == False and cell_obj.infected == True:
                cell_obj.recover_generation()
            elif cell_obj.recovered == True and cell_obj.infected:
                cell_obj.recover_generation()

    def cell_immunity(self):
        for cell_name in self.cell_list:
            cell_obj = self.cell_object_dict[cell_name]
            if cell_obj.recovered == True and cell_obj.immune == True:
                cell_obj.immunity_generation()

    def new_generation(self):
        """Main definition for running program. For the number of generations to simulate, call self.update_position() to get new coordinate lists"""

        # coordinates = []

        sus_full = []
        inf_full = []
        rec_full = []
        imm_full = []

        lg_values = [[], [], []]

        time_array = list(range(0, self.generations))

        if not self.user_file:
            # if user chosing own file will not need - put in function later
            for i in range(
                    self.generations):

                if i % 50 == 0:
                    print("Generating generation " + str(i))

                x_list, y_list, infected, recovered, immune = self.update_position()

                # check if cells touch here, then can adjust objects if need
                self.cells_touch()  # adjusts the objects, not any list

                # recovery function
                self.cell_recovery()

                # immunity function
                if self.use_immunity:
                    self.cell_immunity()

                gen_sus = []
                gen_inf = []
                gen_rec = []
                gen_imm = []

                # puts cells in list depending on their status and whether immunity is used
                if self.use_immunity:
                    for inf in range(len(self.cell_list)):
                        if infected[inf]:  # if True
                            gen_inf.append([x_list[inf], y_list[inf]])
                        elif immune[inf]:
                            gen_imm.append([x_list[inf], y_list[inf]])
                        elif recovered[inf]:
                            gen_rec.append([x_list[inf], y_list[inf]])
                        else:
                            gen_sus.append([x_list[inf], y_list[inf]])
                else:
                    for inf in range(len(self.cell_list)):
                        if infected[inf]:  # if True
                            gen_inf.append([x_list[inf], y_list[inf]])
                        elif recovered[inf]:
                            gen_rec.append([x_list[inf], y_list[inf]])
                        else:
                            gen_sus.append([x_list[inf], y_list[inf]])

                # print(gen_inf)
                # print(gen_rec)
                # print(gen_sus)
                # print("--------------")

                sus_full.append(gen_sus)
                inf_full.append(gen_inf)
                rec_full.append(gen_rec)
                if self.use_immunity:
                    imm_full.append(gen_imm)

                lg_values[0].append(len(gen_sus))
                lg_values[1].append(len(gen_inf))
                lg_values[2].append((len(gen_rec) + len(gen_imm)))

                # coordinates.append([x_list, y_list])

                # print(sus_full)

        # self.export_to_excel() # will soon be redundant
        if not self.user_file:
            self.export_data(sus_full, inf_full, rec_full, imm_full, lg_values, time_array)  # WORKING NOW

        # if using own values, assign them here
        if self.user_file:
            sus_full, inf_full, rec_full, imm_full, lg_values, time_array = self.import_data()
            print("Imported data!")
            print(sus_full)
            print(inf_full)
            print(rec_full)
            print(imm_full)
            print(lg_values)
            print(time_array)

        fig, axs = plt.subplots(2)
        fig.suptitle('Cellular Automata')

        """
        def animate(i):  #  need to adjust to work with two graphs

            plt.figure(1)

            # plt.xlim(0, 600)
            # plt.ylim(0, 600)
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
                # if self.use_immunity:
                #     x_imm_full = [cell[0] for cell in imm_full[i]]
                #     y_imm_full = [cell[1] for cell in imm_full[i]]


                plt.scatter(x_sus_full, y_sus_full, color='blue')
                plt.scatter(x_inf_full, y_inf_full, color='red')
                plt.scatter(x_rec_full, y_rec_full, color='purple')
                if self.use_immunity:
                    plt.scatter([cell[0] for cell in imm_full[i]], [cell[1] for cell in imm_full[i]], color='gray')


            plt.figure(2)
            plt.plot(time_array[0:i], lg_values[0][0:i], label="Susceptible")
            # print(time_array[0:i])
            # print(lg_values[0][0:i])
            # print("---------")
            """

        def animate(i):  # need to adjust to work with two graphs
            # https://stackoverflow.com/questions/42621036/how-to-use-funcanimation-to-update-and-animate-multiple-figures-with-matplotlib

            mycount.increase()
            if mycount.get_count() > self.generations:
                print("End of simulation")
                time.sleep(10000)
            else:
                axs[0].cla()

                x_sus_full = [cell[0] for cell in sus_full[i]]
                y_sus_full = [cell[1] for cell in sus_full[i]]
                x_inf_full = [cell[0] for cell in inf_full[i]]
                y_inf_full = [cell[1] for cell in inf_full[i]]
                x_rec_full = [cell[0] for cell in rec_full[i]]
                y_rec_full = [cell[1] for cell in rec_full[i]]

                axs[0].scatter(x_sus_full, y_sus_full, color='blue')
                axs[0].scatter(x_inf_full, y_inf_full, color='red')
                axs[0].scatter(x_rec_full, y_rec_full, color='purple')
                if self.use_immunity:
                    axs[0].scatter([cell[0] for cell in imm_full[i]], [cell[1] for cell in imm_full[i]], color='gray')

            # plots line graph
            axs[1].plot(time_array[0:i], lg_values[0][0:i], label="Susceptible", color="blue")
            axs[1].plot(time_array[0:i], lg_values[1][0:i], label="Infected", color="red")
            axs[1].plot(time_array[0:i], lg_values[2][0:i], label="recovered", color="purple")

        # plt.xlim(0, self.size_x)
        # plt.ylim(0, self.size_y)

        ani = FuncAnimation(plt.gcf(), animate, interval=100)

        # ani.save('video.mp4', writer='ffmpeg', fps=30, dpi=250)

        plt.tight_layout()
        plt.show()


# self, no_cells, generations, size_x, size_y, infection_radius, infected-1, recovered can be infected, days until recovered, use immunity,days of immunity, use_own_file

# if user uses own file, use some default values

# ca = cellular_automata(5, 10, 10, 10, 2, 3, True)
# ca = cellular_automata(500, 1000, 1000, 1000, 10, 2, True)
# ca = cellular_automata(100, 250, 250, 300, 10, 2)
# ca = cellular_automata(250, 250, 500, 500, 5, 2)
# ca = cellular_automata(500, 100, 100, 100, 20, 10, True)
# ca = cellular_automata(100, 500, 500, 500, 1, 5, True, 15, False, 15, True)
ca = cellular_automata(10, 25, 50, 50, 3, 3, True, 5, True, 5, True)

ca.new_generation()
