from abc import ABC, abstractmethod
import json

class SerializationInterface(ABC):
    @abstractmethod
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    @abstractmethod
    def serialization(self):
        pass


class SerializeJson(SerializationInterface):
    pass


class SerializeBin(SerializationInterface):
    pass

test_json = SerializeJson()
test_bin = SerializeBin()
