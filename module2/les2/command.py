from abc import ABC, abstractmethod


class Command(ABC):

    @abstractmethod
    def do(self):
        pass

    def undo(self):
        pass


class LunchCommand(Command):
    def __init__(self, lunch):
        self.lunch = lunch

    def do(self):
        self.lunch.make_lunch()

    def undo(self):
        self.lunch.stop_lunch()


class Lunch:

    def make_lunch(self):
        print('Your lunch is ready')

    def stop_lunch(self):
        print('It is the end')


class MealInvoker:
    def __init__(self, command):
        self.command = command

    def invoke(self):
        self.command.do()

    def stop(self):
        self.command.undo()


if __name__ == '__main__':
    lunch1 = Lunch()
    command_lunch = LunchCommand(lunch1)
    meal_invoker = MealInvoker(command_lunch)
    meal_invoker.invoke()
    meal_invoker.stop()
