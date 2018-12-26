#encoding: utf-8

from .stack import Stack
from .frame import Frame

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


    @property
    def stack(self):
        return self.__stack


    def create_frame(self, method):
        return Frame(self, method)


    def push_frame(self, frame):
        self.__stack.push(frame)


    def pop_frame(self):
        return self.__stack.pop()


    def current_frame(self):
        return self.__stack.top()