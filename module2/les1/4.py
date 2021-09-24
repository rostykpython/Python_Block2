from abc import abstractmethod, ABC


class GeometricInterface(ABC):

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_diameter(self):
        pass


class Square(GeometricInterface):
    def __init__(self, h, w):
        self.height = h
        self.width = w

    def get_area(self):
        return self.width * self.height

    def get_diameter(self):
        raise NotImplemented


class Circle(GeometricInterface):
    def __init__(self, r):
        self.radius = r

    def get_area(self):
        return self.radius * 3.14 ** 2

    def get_diameter(self):
        return self.radius * 2