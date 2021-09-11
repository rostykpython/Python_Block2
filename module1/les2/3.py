from abc import ABC, abstractmethod


class Aircraft(ABC):

    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def lend(self):
        print('All system worked well')


class Jet(Aircraft):

    def fly(self):
        print('My jet is flying!')

    def lend(self):
        super().lend()
        print('Let jsa\dpaflkdfj')


b = Jet()
b.lend()
b.fly()



