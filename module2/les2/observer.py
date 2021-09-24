from abc import ABC, abstractmethod


class Observer(ABC):

    @abstractmethod
    def update(self, message):
        pass


class Observable(ABC):
    def __init__(self):
        self.observers = []

    def register(self, observer: Observer):
        self.observers.append(observer)

    def notify_observers(self, message):
        for observer in self.observers:
            observer.update(message)


class Newspaper(Observable):

    def add_news(self, news):
        self.notify_observers(news)


class Citizen(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f'{self.name} just knew {message}')


if __name__ == '__main__':
    newspaper = Newspaper()
    newspaper.register(Citizen('Rost'))
    newspaper.add_news('Observer very interesting pattern')
