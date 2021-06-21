import tkinter as tk
from datetime import datetime


class Button_Frame_Class(tk.Frame):
    def __init__(self, the_curve, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.the_curve = the_curve
        self.main_dlg = args[0]

        self.grid(row=1, column=1, sticky='nsew')
        self.config(bg='red')
        self.grid_propagate(0)

        this_row = 0
        self.rowconfigure(this_row, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(3, weight=1)

        this_row = this_row + 1
        one_label = tk.Label(self, text='This is where your interface will be')
        one_label.config(bg='red')
        one_label.grid(row=this_row, column=1)

        this_row = this_row + 1
        one_button = tk.Button(self, text='Press This', command=lambda: self.default_button_pressed())
        one_button.grid(row=this_row, column=1)

        third_button = tk.Button(self, name="zoom_button", text='Zoom In', command=lambda: self.zoom_in(1))
        third_button.grid(row=this_row, column=3)

        this_row = this_row + 1
        one_entry = tk.Entry(self, width=10, name='one_entry')
        one_entry.grid(row=this_row, column=1)
        one_entry.insert(0, 0)

        tk.Label(self, text="Zoom Amount", width=10).grid(row=this_row, column=2)

        this_row = this_row + 1
        tk.Scale(self, width=10, orient="horizontal", from_=0, to=10, name="scale").grid(row=this_row, column=2)

        tk.Label(self, text="Move Amount", width=10).grid(row=this_row, column=3)

        this_row = this_row + 1
        tk.Scale(self, width=10, orient="horizontal", from_=0, to=10, name="move_amount").grid(row=this_row, column=3)
        this_row = this_row + 1

        tk.Button(self, name="shift_left", text="move left", command=lambda: self.move_left()).grid(row=this_row, column=1)
        this_row = this_row + 1

        tk.Button(self, name="shift_right", text="move right", command=lambda: self.move_right()).grid(row=this_row, column=1)
        this_row = this_row + 1

        tk.Button(self, name="shift_down", text="move down", command=lambda: self.move_down()).grid(row=this_row, column=1)
        this_row = this_row + 1

        tk.Button(self, name="shift_up", text="move up", command=lambda: self.move_up()).grid(row=this_row, column=1)

        this_row = this_row + 1
        self.rowconfigure(this_row, weight=1)

    def default_button_pressed(self):
        self.button_pressed()

    def button_pressed(self):
        drawing_area = self.main_dlg.nametowidget('our_canvas')
        # if self.iteration_number == 0:
        widget = self.nametowidget('one_entry')
        # iteration_number = widget.
        drawing_area.draw_triangle(int(widget.get()), self.nametowidget("scale").get() * 100)
        drawing_area.draw_grid()

    def zoom_in(self, scale):
        this_entry = self.nametowidget('one_entry')
        temp = this_entry.get()
        temp = 0

    def move_x(self, amount):
        self.the_curve.shift_points(amount, 0)
        self.button_pressed()

    def move_y(self, amount):
        self.the_curve.shift_points(0, amount)
        self.button_pressed()

    def move_left(self):
        self.move_x(-self.nametowidget("move_amount").get())

    def move_right(self):
        self.move_x(self.nametowidget("move_amount").get())

    def move_down(self):
        self.move_y(-self.nametowidget("move_amount").get())

    def move_up(self):
        self.move_y(self.nametowidget("move_amount").get())
