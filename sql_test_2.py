from tkinter import ttk

import tkinter as tk

import sqlite3

#https://www.activestate.com/resources/quick-reads/how-to-display-data-in-a-table-using-tkinter/

# def connect():
#
#     con1 = sqlite3.connect("my_database.db")
#
#     cur1 = con1.cursor()
#
#     con1.commit()
#
#     con1.close()


def View():

    con1 = sqlite3.connect("my_database.db")

    cur1 = con1.cursor()

    cur1.execute("SELECT * FROM users")

    rows = cur1.fetchall()

    for row in rows:

        print(row)

        tree.insert("", tk.END, values=row)

    con1.close()


# connect to the database

# connect()

root = tk.Tk()

tree = ttk.Treeview(root, column=("c1", "c2", "c3", "c4", "c5", "c6"), show='headings')

tree.column("#1", anchor=tk.CENTER)

tree.heading("#1", text="username")

tree.column("#2", anchor=tk.CENTER)

tree.heading("#2", text="id")

tree.column("#3", anchor=tk.CENTER)

tree.heading("#3", text="see_all")

tree.column("#4", anchor=tk.CENTER)

tree.heading("#4", text="email")

tree.column("#5", anchor=tk.CENTER)

tree.heading("#5", text="first_name")

tree.column("#6", anchor=tk.CENTER)

tree.heading("#6", text="last_name")

tree.pack()

button1 = tk.Button(text="Display data", command=View)

button1.pack(pady=10)

root.mainloop()
