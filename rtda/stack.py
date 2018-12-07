#encoding: utf-8

from collections import deque

class StackEmpty(Exception):
    pass

class StackFull(Exception):
    pass

class Stack(object):

    def __init__(self, maxlen=1024):
        self.__stack = deque()
        self.__maxlen = maxlen

    def pop(self):
        if len(self.__stack) == 0:
            raise StackEmpty()
        return self.__stack.pop()

    def push(self, e):
        if len(self.__stack) >= self.__maxlen:
            raise StackFull()
        self.__stack.append(e)

    def top(self):
        if len(self.__stack) == 0:
            raise StackEmpty()
        return self.__stack[-1]

    def __repr__(self):
        return '<{0!r}>{1!r}'.format(self.__class__.__name__, vars(self))
