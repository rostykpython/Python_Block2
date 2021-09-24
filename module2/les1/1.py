class OldRectangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        return self.height * self.width

    def draw(self):
        print('Drawing rectangle')


class Rectangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        return self.height * self.width


class Drawing(Rectangle):

    def draw(self):
        print('Drawing')

