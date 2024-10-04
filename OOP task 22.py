class Shape:
    def __init__(self,colour,filled):
        self._colour = colour
        self._filled = filled
    
    def display(self):
        print(self._colour)
        print(self._filled)

    def setColour(self, col):
        self._colour = col

    def setFilled(self, fill):
        self._filled = fill

class Circle(Shape):
    def __init__(self, colour, filled, radius):
        super().__init__(colour, filled)
        self._radius = radius

    def setRadius(self, rad):
        self._radius = rad

    def display(self):
        super().display()
        print(self._radius)

class Rectangle(Shape):
    def __init__(self, colour, filled, length, height):
        super().__init__(colour, filled)
        self._length = length
        self._height = height

    def setLength(self, length):
        self._length = length

    def setHeigh(self, height):
        self._height = height

    def display(self):
        super().display()
        print(self._length)
        print(self._height)
    

s1 = Shape("pink", True)
s1.display()
s2 = Circle("black", False, 12)
s2.display()
s3 = Rectangle("blue", True, 10, 5)
s3.display()

