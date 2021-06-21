import datetime
import math
import tkinter as tk
from the_curve_file import the_curve_class
from wedge_piece_class import Wedge_Piece_Class


class Canvas_Class(tk.Canvas):
    def __init__(self, the_curve, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.main_dlg = args[0]

        self.grid(row=1, column=2, sticky='nsew')
        self.config(bg='white')
        self.grid_propagate(0)
        self.the_curve = the_curve

        self.bind('<Button-1>', self.button_clicked)
        self.bind('<ButtonRelease-1>', self.button_released)

    def button_released(self, event):
        x = event.x
        y = event.y

        temp = 1

    def button_clicked(self, event):
        x = event.x
        y = event.y
        temp = 1
        print("test")

    def draw_line(self):
        max_x = self.winfo_width()
        max_y = self.winfo_height()

        self.create_line(0, 0, max_x, max_y)
        self.create_line(0, max_y, max_x, 0)

    def draw_grid(self):
        max_x = self.winfo_width()
        max_y = self.winfo_height()

        middle_x = max_x / 2
        middle_y = max_y / 2

        self.create_line(middle_x, 0, middle_x, max_x)
        self.create_line(0, middle_y, max_x, middle_y)

        x = - 1000
        y = - 1000

        while x <= 1001:
            while y <= 1001:
                if x % 50 != 0:
                    y += 1
                    continue
                if y % 50 != 0:
                    y += 1
                    continue
                if x != 0 and y != 0:
                    y += 1
                    continue
                coordinate = self.convert_point(x, y, 1)
                self.create_text(coordinate[0], coordinate[1],
                                 text="(" + str(x) + "," + str(y) + ")")
                y += 1
            x += 1
            y = -1000

    def draw_wedge(self, at, scale_factor):
        wedges = self.the_curve.get_points_at(at)
        self.delete("all")
        for wedge in wedges:
            point_a = self.convert_coordinate(wedge.point_a, scale_factor)
            point_b = self.convert_coordinate(wedge.point_b, scale_factor)
            point_c = self.convert_coordinate(wedge.point_c, scale_factor)
            point_d = self.convert_coordinate(wedge.point_d, scale_factor)
            point_e = self.convert_coordinate(wedge.point_e, scale_factor)

            self.create_line(point_a[0],
                             point_a[1],
                             point_b[0],
                             point_b[1])

            self.create_line(point_b[0],
                             point_b[1],
                             point_c[0],
                             point_c[1])

            self.create_line(point_c[0],
                             point_c[1],
                             point_d[0],
                             point_d[1])

            self.create_line(point_d[0],
                             point_d[1],
                             point_e[0],
                             point_e[1])

    def outside_rectangle(self, rectangle, coordinate):
        rectangle_bottom = rectangle[0]
        rectangle_top = rectangle[1]
        return ((rectangle_bottom[0] > coordinate[0] and
                 rectangle_bottom[1] > coordinate[1]) or
                (rectangle_top[0] < coordinate[0] and
                 rectangle_top[1] < coordinate[1]))

    def draw_triangle(self, iteration_number, scale_factor):
        while self.the_curve.get_last_layer() <= iteration_number:
            self.the_curve.load_next_layer()
        self.draw_wedge(iteration_number, scale_factor)

    def convert_coordinate(self, point, scale_factor):
        return self.convert_point(point[0], point[1], scale_factor)

    def convert_point(self, point_x, point_y, scale_factor):
        max_x = self.winfo_width()
        max_y = self.winfo_height()
        middle_x = max_x / 2
        middle_y = max_y / 2

        converted_x = middle_x + (point_x * scale_factor)
        converted_y = middle_y - (point_y * scale_factor)
        return [converted_x, converted_y - scale_factor]

    # def find_lower(self, number, other):
    #     if number <= other:
    #         return number
    #     return other
    #
    # def find_upper(self, number, other):
    #     if number >= other:
    #         return number
    #     return other
