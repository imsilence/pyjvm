#encoding: utf-8

from .stack import Stack
from .vars_ import Vars


class Frame(object):

    def __init__(self, thread, method):
        self.__lower = None
        self.__stack = Stack(method.max_stack)
        self.__vars = Vars(method.max_locals)
        self.__thread = thread
        self.__method = method
        self.__next_pc = 0


    @property
    def stack(self):
        return self.__stack


    @property
    def vars(self):
        return self.__vars


    @property
    def thread(self):
        return self.__thread


    @property
    def next_pc(self):
        return self.__next_pc


    @next_pc.setter
    def next_pc(self, next_pc):
        self.__next_pc = next_pc


    @property
    def method(self):
        return self.__method

