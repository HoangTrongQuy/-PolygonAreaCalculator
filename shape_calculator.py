class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self,width_s):
        self.width = width_s

    def set_height(self,height_s):
        self.height = height_s

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return (2*self.width + 2*self.height)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** 0.5)

    def get_picture(self):
        picture = ""
        if self.width >= 50 or self.height >= 50: picture = "Too big for picture."
        else:
            for i in range(self.height):
                for j in range(self.width):
                    picture += "*"
                picture += "\n"
        return picture

    def get_amount_inside(self, shape):
        if self.width % shape.width == 0 and self.height % shape.height == 0:
            return int((self.width / shape.width) * (self.height / shape.height))
        else:
            print("shape not fit")

    def __repr__(self):
        return f"Rectangle (width={self.width}, height={self.height})"

class Square(Rectangle):

    def __init__(self, side):
        self.side = side
        self.width = side
        self.height = side

    def set_side(self, side_s):
        self.side = side_s
        self.width = side_s
        self.height = side_s

    def __repr__(self):
        return f"Square (side={self.side})"



