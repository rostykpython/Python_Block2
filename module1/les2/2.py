from abc import ABC, abstractmethod


class Worker(ABC):
    @abstractmethod
    def work(self):
        print('Doing Job')


class Builder(Worker):
    def work(self):
        print('Building house!')


class Manager():
    def manage(self):
        print('Managing!')


class SkyScrapper:
    def creating(self, worker):
        print('Creating bulding')
        worker.work()


worker = Builder()
work1 = Manager()

sc = SkyScrapper()
sc.creating(worker)
