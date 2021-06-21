import math

import tkinter


class Wedge_Piece_Class():

    def __init__(self, point_a, point_e):
        # for each iteration we will be making a new Wedge Piece for each line segment
        # point_a and point_e are the end points of the line segments

        # self.point_a = self.get_smaller_point(point_a, point_e)
        # self.point_e = self.get_larger_point(point_a, point_e)

        self.point_a = point_a
        self.point_e = point_e

        self.point_b = self.calculate_point_b()
        self.point_d = self.calculate_point_d()
        self.point_c = self.calculate_point_c()

    def calculate_point_b(self):
        return self.calculate_point(self.point_a, self.point_e, 1 / 3)

    def calculate_point_d(self):
        return self.calculate_point(self.point_a, self.point_e, 2 / 3)

    def calculate_point(self, start, end, fraction):
        return [(end[0] - start[0]) * fraction + start[0],
                (end[1] - start[1]) * fraction + start[1]]

    def calculate_point_c(self):
        midpoint = self.calculate_point(self.point_a, self.point_e, 1 / 2)

        b_copy = [self.point_b[0], self.point_b[1]]

        translated_a = self.translate(self.point_a, b_copy)
        translated_b = self.translate(self.point_b, b_copy)
        translated_d = self.translate(self.point_d, b_copy)
        translated_e = self.translate(self.point_e, b_copy)

        midpoint = self.translate(midpoint, b_copy)

        hypotenuse = ((translated_d[0] - translated_b[0]) ** 2 + (translated_d[1] - translated_b[1]) ** 2) ** 0.5
        cos_theta = (translated_d[0] - translated_b[0]) / hypotenuse
        sin_theta = -(translated_d[1] - translated_b[1]) / hypotenuse

        rotated_a = self.rotate(cos_theta, sin_theta, translated_a)
        rotated_b = self.rotate(cos_theta, sin_theta, translated_b)
        rotated_d = self.rotate(cos_theta, sin_theta, translated_d)
        rotated_e = self.rotate(cos_theta, sin_theta, translated_e)

        rotated_midpoint = self.rotate(cos_theta, sin_theta, midpoint)

        distance_b_to_m = self.distance(rotated_midpoint, translated_b)

        rotated_c = [rotated_midpoint[0], distance_b_to_m * (3 ** 0.5)]

        translated_a = self.rotate(cos_theta, -sin_theta, rotated_a)
        translated_b = self.rotate(cos_theta, -sin_theta, rotated_b)
        translated_c = self.rotate(cos_theta, -sin_theta, rotated_c)
        translated_d = self.rotate(cos_theta, -sin_theta, rotated_d)
        translated_e = self.rotate(cos_theta, -sin_theta, rotated_e)

        b_copy = [-b_copy[0], -b_copy[1]]

        # translated_a = self.translate(translated_a, b_copy)
        # translated_b = self.translate(translated_b, b_copy)
        return self.translate(translated_c, b_copy)
        # translated_d = self.translate(translated_d, b_copy)
        # translated_e = self.translate(translated_e, b_copy)

    def translate(self, point, translate_by):
        return [point[0] - translate_by[0],
                point[1] - translate_by[1]]

    def rotate(self, cos_theta, sin_theta, point):
        return [point[0] * cos_theta - point[1] * sin_theta,
                point[0] * sin_theta + point[1] * cos_theta]

    def distance(self, point_one, point_two):
        return ((point_one[0] - point_two[0]) ** 2 +
                (point_one[1] - point_two[1]) ** 2) ** 0.5
