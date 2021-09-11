from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y



