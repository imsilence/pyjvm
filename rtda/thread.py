#encoding: utf-8

from .stack import Stack

class Thread(object):

    def __init__(self):
        self.__pc = 0
        self.__stack = Stack()

    @property
    def pc(self):
        return self.__pc

    @pc.setter
    def pc(self, pc):
        self.__pc = pc

    def push_frame(self, frame):
        self.__jstack.push(frame)

    def pop_frame(self):
        return self.__jstack.pop()

    def current_frame(self):
        return self.__jstack.top()