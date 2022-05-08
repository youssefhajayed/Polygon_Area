import math


class Rectangle:
    width = 0
    height = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):

        print((math.sqrt(self.height ^ 2 + self.width ^ 2)))

        return math.sqrt(self.height ** 2 + self.width ** 2)

    def get_picture(self):

        output = ""
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        for i in range(self.height):
            for j in range(self.width):
                output = output + "*"
            output = output + "\n"

        return output

    def get_amount_inside(self, shape):
        n_width = self.width // shape.width
        n_height = self.height // shape.height
        return n_height * n_width

    def __str__(self):
        return str(type(self).__name__) + "(width=" + str(self.width) + ", height=" + str(self.height) + ")"


class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return str(type(self).__name__) + "(side=" + str(self.width) + ")"
