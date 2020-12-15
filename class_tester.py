from abc import ABC, abstractmethod


class DataCollector(ABC):

    def __init__(self, value):
        self.data = value

    @abstractmethod
    def set_data(self, value):
        pass

    @abstractmethod
    def display(self):
        pass


class DataDisplay(DataCollector):

    def display(self):
        print(f'Current value = {self.data}')


class DataAction(DataDisplay):

    def custom_dec_function(self):
        pass

    def __init__(self, value: int, homie: str, master_data: str):
        self.data = value
        self.homie_data = homie
        self.master_data = master_data
        self._secret = 'secret'

    def __add__(self, other):
        return DataAction(self.data + other)

    def __str__(self):
        return '[DataAction : $s]' % self.data

    @staticmethod
    def static_data():
        return 'gotta bring some more static homie'

    @classmethod
    def class_data(cls):
        return 'Gotta bring some class fights like in a good old times', cls

    @property
    def property_func(self):
        return self.homie_data + ' ' + self.master_data

    @property
    def secret(self):
        return self._secret

    def get_secret(self):
        return self._secret


if __name__ == "__main__":
    d = DataAction(5, 'aaa', 'aaa')
    print(d.secret)