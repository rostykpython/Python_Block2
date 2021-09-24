from abc import ABC, abstractmethod


class GeometricInterface(ABC):

    @abstractmethod
    def get_area(self):
        pass


class SquareInterface(GeometricInterface, ABC):
    pass


class Square(SquareInterface):
    def __init__(self, h, w):
        self.height = h
        self.width = w

    def get_area(self):
        return self.width * self.height


class CircleInterface(GeometricInterface, ABC):

    @abstractmethod
    def get_diameter(self):
        pass


class Circle(CircleInterface):
    def __init__(self, r):
        self.radius = r

    def get_area(self):
        return self.radius * 3.14 ** 2

    def get_diameter(self):
        return self.radius * 2


