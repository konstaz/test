from abc import ABC, abstractmethod
from collections import Counter


class ProtoGermanicAlphabet(ABC):
    _LETTERS = None
    _LANGUAGE = None

    @abstractmethod
    def count_symbols(self):
        pass

    @abstractmethod
    def print_symbols(self):
        pass


class EnglishAlphabet(ProtoGermanicAlphabet):

    def __init__(self):
        self._LETTERS = 'abcdefghijklmnopqrstuvwxyz'
        self._LANGUAGE = 'English'

    def count_symbols(self):
        return len(self._LETTERS)

    def print_symbols(self):
        return self._LETTERS

    @property
    def language(self):
        return self._LANGUAGE

    # @language.setter
    # def language(self, value):
    #     self._LANGUAGE = value

    def f(self):
        raise NotImplemented

    @staticmethod
    def sentence_example():
        return 'Here comes a typical sentence in English. If you wanna know more you better get starting right now'

    def check_letter(self, letter: str):
        # add error
        return letter in self._LETTERS


