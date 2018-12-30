#encoding: utf-8
from abc import ABC, abstractclassmethod


class Method(ABC):

    @abstractclassmethod
    def execute(cls, frame):
        pass


class EmptyMethod(Method):

    @classmethod
    def execute(cls, frame):
        pass