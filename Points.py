class Points:
    index = 0
    x = 0
    y = 0
    z = 0
    colour = 0

    def __init__(self, x, y, z, length):
        self.index = length
        self.x = x
        self.y = y
        self.z = z

    def change_colour(self, c):
        self.colour = c


def create_the_grid(x_length: int, y_length: int, z_length: int):
    p_l = []  # creating list of points

    temp_x = 0
    temp_y = 0
    temp_z = 0

    for i in range(z_length):
        for j in range(x_length * y_length):
            if j % 5 == 0 and j != 0:
                temp_x = temp_x + 1
                temp_y = 0
            pt = Points(temp_x, temp_y, temp_z, len(p_l))
            p_l.append(pt)
            temp_y = temp_y + 1
        temp_z = temp_z + 1
        temp_x = 0
        temp_y = 0

    return p_l
