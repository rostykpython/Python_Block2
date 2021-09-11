import json
import pickle
from abc import ABC, abstractmethod


class SerializationInterface(ABC):
    @abstractmethod
    def __init__(self, filename, data):
        self.filename = filename
        self.data = data

    @abstractmethod
    def serialization(self):
        pass

    @abstractmethod
    def deserialization(self):
        pass


class SerializeJson(SerializationInterface):
    def __init__(self, filename, data):
        super(SerializeJson, self).__init__(filename, data)

    def deserialization(self):
        try:
            with open(self.filename, 'r') as json_file:
                return json.load(json_file)
        except FileNotFoundError:
            return []

    def serialization(self):
        try:
            load_data = SerializeJson(self.filename, self.data).deserialization()
            load_data.extend(self.data)
            with open(self.filename, 'w') as json_file:
                json.dump(load_data, json_file)
        except FileNotFoundError:
            with open(self.filename, 'w') as json_file:
                json.dump(self.data, json_file)


class SerializeBin(SerializationInterface):
    def __init__(self, filename, data):
        super(SerializeBin, self).__init__(filename, data)

    def deserialization(self):
        try:
            with open(self.filename, 'rb') as bin_file:
                return pickle.load(bin_file)
        except FileNotFoundError:
            return []

    def serialization(self):
        try:
            load_data = SerializeBin(self.filename, self.data).deserialization()
            load_data.extend(self.data)
            with open(self.filename, 'wb') as bin_file:
                pickle.dump(load_data, bin_file)
        except FileNotFoundError:
            with open(self.filename, 'wb') as bin_file:
                pickle.dump(self.data, bin_file)
