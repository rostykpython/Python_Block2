class Garage:
    def __init__(self):
        self.cars = []

    def car_to_garage(self, car):
        self.cars.append(car)


class ChargingStation:
    def __init__(self, garage):
        number_of_cars = len([car for car in garage.cars])
        print(f'Need to charge {number_of_cars}')


gar = Garage()
gar.car_to_garage('Tesla')
gar.car_to_garage('Audi')

station = ChargingStation(gar)

