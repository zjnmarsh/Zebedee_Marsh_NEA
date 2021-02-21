import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox



class gui_Enter_Email:
    def __init__(self, master):
        self.email = ""

        self.master = master
        self.frame = ttk.Frame(master, padding=5)

        self.lbl_email = ttk.Label(self.frame, text='Please enter your email address')
        self.e_email = ttk.Entry(self.frame)
        self.btn_enter = ttk.Button(self.frame, text="Submit", command=self.submit)

        self.frame.grid(row=0, column=0, sticky='nswe')

        self.lbl_email.grid(column=0, row=0)
        self.e_email.grid(column=0, row=1)
        self.btn_enter.grid(column=0, row=2)

        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        self.frame.columnconfigure(1, weight=1)
        self.frame.rowconfigure(1, weight=1)

    def submit(self):
        self.email = str(self.e_email.get())
        self.master.destroy()
        return self.email

    def return_email(self):
        return self.email

# root = tk.Tk()
# root.title('Email')
#
# window = gui_Enter_Email(root)
# yes = root.mainloop()
# print(yes)
# print(window.return_email())

# def enter_email():
#     print('enter_email')
#     root5 = tk.Tk()
#     root5.title('Enter email')
#     email_window = gui_Enter_Email(root5)
#     email = email_window.return_email()
#     print("got email")
#     return email

# yes = enter_email()
# print(yes)

root5 = tk.Tk()
root5.title('Enter email')
email_window = gui_Enter_Email(root5)
