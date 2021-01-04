from tkinter import messagebox
import tkinter as tk

class error:

    def __init__(self, err_type, message):
        title = err_type + " error"
        messagebox.showerror(title, message)


# err = error("Count", "not in range")
#
# pass123 = True
#

tk.Tk().withdraw()
messagebox.showerror("count error", "number not in range")
