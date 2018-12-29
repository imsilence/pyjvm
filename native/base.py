#encoding: utf-8
from abc import ABC, abstractmethod


class Method(ABC):

    @abstractmethod
    def execute(self, frame):
        pass


class EmptyMethod(Method):

    def execute(self, frame):
        pass