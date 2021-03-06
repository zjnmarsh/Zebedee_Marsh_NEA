import tkinter as tk
from tkinter import ttk
import sub_sql_functions as my_sql


class gui_statistics:

    def __init__(self, master):
        self.master = master
        self.frame = ttk.Frame(master, padding=5)

        self.wrapper0 = tk.LabelFrame(self.frame)
        self.wrapper1 = tk.LabelFrame(self.frame)
        self.wrapper2 = tk.LabelFrame(self.frame)

        self.tree = ttk.Treeview(self.wrapper1)

        self.btn_ca = ttk.Button(self.wrapper2, text="CA", command=self.open_ca)
        self.btn_sir = ttk.Button(self.wrapper2, text="SIR", command=self.open_sir)
        self.btn_filter = ttk.Button(self.wrapper2, text="Filter", command="", state=tk.DISABLED)
        self.btn_export = ttk.Button(self.wrapper2, text="Export", command="", state=tk.DISABLED)
        self.btn_exit = ttk.Button(self.wrapper2, text="Exit", command=self.exit)
        self.lb_text = ttk.Label(self.wrapper0, text="Display statistics for CA or SIR")
        self.lb_filter = ttk.Label(self.wrapper0, text="Filter results by username")
        self.e_usr = ttk.Entry(self.wrapper0)
        self.btn_filter = ttk.Button(self.wrapper0, text="Filter", command="", state=tk.DISABLED)

        self.frame.grid(column=0, row=0, sticky='nsew')

        self.wrapper0.grid(column=0, row=0, columnspan=2)
        self.wrapper1.grid(column=0, row=1)
        self.wrapper2.grid(column=1, row=1)

        self.btn_ca.grid(column=0, row=0)
        self.btn_sir.grid(column=0, row=1)
        self.btn_export.grid(column=0, row=2)
        self.btn_exit.grid(column=0, row=3)

        self.lb_text.grid(column=0, row=0, columnspan=3)

        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        self.frame.columnconfigure(1, weight=1)
        self.frame.rowconfigure(1, weight=1)

    def clear_tree(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

    def open_sir(self):
        self.master.destroy()
        root1 = tk.Tk()
        root1.title('SIR Stats')
        window = stats_sir(root1)

    def open_ca(self):
        self.master.destroy()
        root1 = tk.Tk()
        root1.title('CA Stats')
        window = stats_ca(root1)

    def exit(self):
        self.master.destroy()


class stats_sir(gui_statistics):
    def __init__(self, master):
        gui_statistics.__init__(self, master)
        self.data = []

        self.btn_filter['state'] = 'normal'
        self.btn_filter['command'] = self.filter
        self.btn_export['state'] = 'normal'
        self.btn_export['command'] = self.export_data

        self.lb_filter.grid(column=0, row=1)
        self.e_usr.grid(column=1, row=1)
        self.btn_filter.grid(column=2, row=1)

        self.tree['column'] = ("c1", "c2", "c3", "c4", "c5", "c6")
        self.tree['show'] = 'headings'

        self.tree.heading("#1", text="username")
        self.tree.heading("#2", text="sus0")
        self.tree.heading("#3", text="inf0")
        self.tree.heading("#4", text="rec0")
        self.tree.heading("#5", text="beta")
        self.tree.heading("#6", text="gamma")

        self.tree.column('#1', width=100)
        self.tree.column('#2', width=75)
        self.tree.column('#3', width=75)
        self.tree.column('#4', width=75)
        self.tree.column('#5', width=75)
        self.tree.column('#6', width=75)

        self.tree.grid(row=0, sticky='nsew')
        self.treeview = self.tree
        self.sir, self.ca = my_sql.full_statistics()

        self.data = self.sir

        for row in self.sir:
            self.tree.insert("", tk.END, values=row)

    def filter(self):
        self.clear_tree()
        username = str(self.e_usr.get())
        username = username.lower()
        rows = my_sql.filtered_statistics("sir", username)

        self.data = rows
        print(self.data)
        for row in rows:
            self.tree.insert("", tk.END, values=row)

    def export_data(self):
        columns = "Name, sus0, inf0, rec0, beta, gamma"
        with open("../other_files/exported_data.csv", "w") as file:
            file.write("Name, sus0, inf0, rec0, beta, gamma\n")
            print(self.data)
            for line in self.data:
                file.write(str(line)[1:-1] + "\n")


class stats_ca(gui_statistics):
    def __init__(self, master):
        gui_statistics.__init__(self, master)
        self.data = []

        self.btn_filter['state'] = 'normal'
        self.btn_export['state'] = 'normal'
        self.btn_export['command'] = self.export_data
        self.btn_filter['command'] = self.filter

        self.lb_filter.grid(column=0, row=1)
        self.e_usr.grid(column=1, row=1)
        self.btn_filter.grid(column=2, row=1)

        self.tree['column'] = ("c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "c11", "c12")
        self.tree['show'] = 'headings'

        self.tree.heading("#1", text="username")
        self.tree.heading("#2", text="no_cells")
        self.tree.heading("#3", text="generations")
        self.tree.heading("#4", text="size x")
        self.tree.heading("#5", text="size y")
        self.tree.heading("#6", text="inf radius")
        self.tree.heading("#7", text="number inf")
        self.tree.heading("#8", text="rec inf true")
        self.tree.heading("#9", text="days inf")
        self.tree.heading("#10", text="use immunity")
        self.tree.heading("#11", text="days immune")

        self.tree.column('#1', width=100)
        self.tree.column('#2', width=100)
        self.tree.column('#3', width=100)
        self.tree.column('#4', width=100)
        self.tree.column('#5', width=100)
        self.tree.column('#6', width=75)
        self.tree.column('#7', width=75)
        self.tree.column('#8', width=75)
        self.tree.column('#9', width=75)
        self.tree.column('#10', width=75)
        self.tree.column('#11', width=75)

        self.tree.grid(row=0, sticky='nsew')
        self.treeview = self.tree
        self.sir, self.ca = my_sql.full_statistics()
        self.data = self.ca
        for row in self.ca:
            self.tree.insert("", tk.END, values=row)

    def filter(self):
        self.clear_tree()
        username = str(self.e_usr.get())
        username = username.lower()
        rows = my_sql.filtered_statistics("ca", username)
        self.data = rows
        for row in rows:
            self.tree.insert("", tk.END, values=row)

    def export_data(self):
        columns = "Name, sus0, inf0, rec0, beta, gamma"
        with open("../other_files/exported_data.csv", "w") as file:
            file.write(
                "Name, no_cells, generations, size_x, size_y, inf_radius, num_infected, rec_inf_true, days_inf, use_immunity, days_immune\n")
            print(self.data)
            for line in self.data:
                file.write(str(line)[1:-1] + "\n")


root = tk.Tk()
root.title('Main Window')
window = gui_statistics(root)
# test = stats_sir(root)


# current_user = "zebedee"
root.mainloop()
