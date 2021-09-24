from abc import ABC, abstractmethod


class Garage(ABC):

    def __init__(self):
        self.cars = []

    @abstractmethod
    def car_to_garage(self, car):
        pass

    @abstractmethod
    def need_to_charge(self, name):
        pass


class NewChargingStation(Garage, ABC):
    def car_to_garage(self, car):
        self.cars.append(car)

    def need_to_charge(self, name):
        return [car for car in self.cars]
