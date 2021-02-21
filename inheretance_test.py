import tkinter as tk
from tkinter import ttk
import sub_sql_functions as my_sql


class gui_statistics:

    def __init__(self, master):
        self.master = master
        self.frame = ttk.Frame(master, padding=5)

        self.wrapper1 = tk.LabelFrame(self.frame)
        self.wrapper2 = tk.LabelFrame(self.frame)

        # self.tree = ttk.Treeview(self.wrapper1, column=("c1", "c2", "c3", "c4", "c5", "c6"), show='headings')

        self.btn_ca = ttk.Button(self.wrapper2, text="CA", command="")
        self.btn_sir = ttk.Button(self.wrapper2, text="SIR", command=self.open_sir)
        self.btn_filter = ttk.Button(self.wrapper2, text="Filter", command="")
        self.btn_export = ttk.Button(self.wrapper2, text="Export", command="")
        self.btn_exit = ttk.Button(self.wrapper2, text="Exit", command="")

        self.frame.grid(column=0, row=0, sticky='nsew')

        self.wrapper1.grid(column=0, row=0)
        self.wrapper2.grid(column=1, row=0)

        # self.tree.grid(row=0, column=0, sticky='nsew')

        self.btn_ca.grid(column=0, row=0)
        self.btn_sir.grid(column=0, row=1)
        self.btn_filter.grid(column=0, row=2)
        self.btn_export.grid(column=0, row=3)
        self.btn_exit.grid(column=0, row=4)

        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        self.frame.columnconfigure(1, weight=1)
        self.frame.rowconfigure(1, weight=1)

    def open_sir(self):
        print("open")
        self.master.destroy()
        root1 = tk.Tk()
        root1.title('SIR Stats')
        window = stats_sir(root1)



class stats_sir(gui_statistics):
    def __init__(self, master):
        gui_statistics.__init__(self, master)
        self.tree = ttk.Treeview(self.wrapper1, column=("c1", "c2", "c3", "c4", "c5", "c6"), show='headings')

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
        for row in self.sir:
            self.tree.insert("", tk.END, values=row)


root = tk.Tk()
root.title('Main Window')
window = gui_statistics(root)
# test = stats_sir(root)


# current_user = "zebedee"
root.mainloop()
