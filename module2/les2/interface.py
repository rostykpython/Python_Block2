from abc import ABC, abstractmethod


class Device(ABC):

    @staticmethod
    @abstractmethod
    def power_on():
        pass


class Router(ABC):

    @staticmethod
    @abstractmethod
    def route():
        pass


class Network_Device(Device, Router):
    @staticmethod
    def power_on():
        print('Ready to process')

    @staticmethod
    def route():
        print('Nothing')