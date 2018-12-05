#encoding: utf-8

from .stack import Stack

class LocalVars(object):
    def __init__(self, max_locals):
        self.__vars = [None] * max_locals

    def __getitem__(self, index):
        return self.__vars[index]

    def __setitem__(self, index, value):
        self.__vars[index] = value


class Frame(object):

    def __init__(self, max_stack, max_locals):
        self.__stack = Stack(max_stack)
        self.__local_vars = LocalVars(max_locals)

