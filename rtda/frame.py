#encoding: utf-8

from .stack import Stack

class LocalVars(object):
    def __init__(self, max_locals):
        self.__vars = [None] * max_locals

    def __getitem__(self, index):
        return self.__vars[index]

    def __setitem__(self, index, value):
        self.__vars[index] = value

    def __repr__(self):
        return '<{0!r}>{1!r}'.format(self.__class__.__name__, vars(self))


class Frame(object):

    def __init__(self, max_stack, max_locals, thread):
        self.__lower = None
        self.__stack = Stack(max_stack)
        self.__local_vars = LocalVars(max_locals)
        self.__thread = thread
        self.__next_pc = 0

    @property
    def stack(self):
        return self.__stack

    @property
    def localvars(self):
        return self.__local_vars

    @property
    def thread(self):
        return self.__thread

    @property
    def next_pc(self):
        return self.__next_pc

    @next_pc.setter
    def next_pc(self, next_pc):
        self.__next_pc = next_pc
