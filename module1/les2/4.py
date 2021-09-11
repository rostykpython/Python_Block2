from abc import ABC, abstractmethod


class Person:

    @staticmethod
    @abstractmethod
    def hello(age):
        print(f'Hello world{age}!')


class Student(Person):

    def hello(self, age):
        super().hello(age)


s = Student()
s.hello(23)
