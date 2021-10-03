import threading as trd
import time
import random
import datetime


class Race:
    def __init__(self):
        self.barrier = trd.Barrier(4)
        self.cars = ['porsche', 'bmw', 'audi', 'vw']

    def lead(self):
        car = self.cars.pop()
        time.sleep(random.randrange(1, 5))
        print(f'\n {car} reached the barrier at {datetime.datetime.now()}')
        self.barrier.wait()

        time.sleep(random.randrange(1, 5))
        print(f'\n {car} started race at {datetime.datetime.now()}')

        time.sleep(random.randrange(1, 5))
        print(f'\n {car} finished race at {datetime.datetime.now()}')

        self.barrier.wait()
        print(f'\n driver of car {car} go to have a rest')


if __name__ == '__main__':
    print('Race preparation')

    race = Race()

    for x in range(4):
        t1 = trd.Thread(target=race.lead)
        t1.start()