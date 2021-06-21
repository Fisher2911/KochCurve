from wedge_piece_class import Wedge_Piece_Class

class the_curve_class():
    def __init__(self):

        self.the_pieces = []
                                # this is where the individual pieces will be
                                # the first index is the iteration
                                # the second index will be the object of one wedge piece

        # these are the vertices of an equilateral triangle
        self.starting_points = [[-1.0, -1.0], [1.0, -1.0], [0, ((3**0.5)-1)]]

        self.setup_starting_wedge()
        # this_wedge_piece = Wedge_Piece_Class(starting_points[0],starting_points[1])

    def setup_starting_wedge(self):
        temp_list = [Wedge_Piece_Class(self.starting_points[1], self.starting_points[0]),
                     Wedge_Piece_Class(self.starting_points[2], self.starting_points[1]),
                     Wedge_Piece_Class(self.starting_points[0], self.starting_points[2])]
        self.the_pieces.append(temp_list)

    def get_last_layer(self):
        return len(self.the_pieces)

    def load_next_layer(self):
        last_layer = self.get_last_layer() - 1
        wedge_list = self.get_points_at(last_layer)
        temp_list = []
        for wedge in wedge_list:
            temp_list.append(Wedge_Piece_Class(wedge.point_a, wedge.point_b))
            temp_list.append(Wedge_Piece_Class(wedge.point_b, wedge.point_c))
            temp_list.append(Wedge_Piece_Class(wedge.point_c, wedge.point_d))
            temp_list.append(Wedge_Piece_Class(wedge.point_d, wedge.point_e))
        self.the_pieces.append(temp_list)

    def get_points_at(self, at):
        return self.the_pieces[at]

    def shift_points(self, shift_x, shift_y):
        for wedge_list in self.the_pieces:
            for wedge in wedge_list:
                wedge.point_a = [wedge.point_a[0] + shift_x, wedge.point_a[1] + shift_y]
                wedge.point_b = [wedge.point_b[0] + shift_x, wedge.point_b[1] + shift_y]
                wedge.point_c = [wedge.point_c[0] + shift_x, wedge.point_c[1] + shift_y]
                wedge.point_d = [wedge.point_d[0] + shift_x, wedge.point_d[1] + shift_y]
                wedge.point_e = [wedge.point_e[0] + shift_x, wedge.point_e[1] + shift_y]


