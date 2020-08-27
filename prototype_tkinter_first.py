import tkinter as tk


class Gui(tk.Tk):

    def __init__(self, *args,
                 **kwargs):  # *args - pass through any number of variables; **kwargs - pass through dictionaries
        tk.Tk.__init__(self, *args, **kwargs)  # initialising tkinter
        container = tk.Frame(self)  # the frame of the window

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)  # 0 sets minimum size, weight shows priority
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}  # allows application to open different types of pages easily

        frame = StartPage(container, self)

        self.frames[StartPage] = frame

        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont] # looks for cont in dict
        frame.tkraise()  # which is then raised


class StartPage(tk.Frame):

    def __init__(self, parent, controller): # parent class is Gui
        tk.Frame.__init__(self, parent,)

        label = tk.Label(self, text="Start Page")
        label.pack(pady=10, padx=10)


app = Gui()
app.mainloop()
