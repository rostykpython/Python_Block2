from abc import ABC, abstractmethod

class Animal(ABC):

    def live(self):
        print('Live')

    @abstractmethod
    def behave(self):
        print('Please behave!')

class Dog(Animal):
    pass

dog1 = Dog()
dog1.behave()