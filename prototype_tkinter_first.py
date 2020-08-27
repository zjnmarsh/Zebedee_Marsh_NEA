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

        for F in (StartPage, PageOne):  # all pages need to be listed here

            print(F)

            frame = F(container, self)

            self.frames[F] = frame  # saving classes to dictionary, "loading it in"

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)  # start page is shown first

    def show_frame(self, cont):
        frame = self.frames[cont]  # looks for cont in dict
        frame.tkraise()  # which is then raised


class StartPage(tk.Frame):

    def __init__(self, parent,
                 controller):  # parent class is Gui, controller class is main class, allowing show_frame to be called
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Start Page")
        label.pack(pady=10, padx=10)
        button1 = tk.Button(self, text="Page 1", command=lambda: controller.show_frame(PageOne))
        button1.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="This is page 1")
        label.pack(pady=10, padx=10)
        button2 = tk.Button(self, text="Start Page", command=lambda: controller.show_frame(StartPage))
        button2.pack()


app = Gui()
app.mainloop()
