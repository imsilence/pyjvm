#encoding: utf-8

from ..vars_ import Vars

class Object(object):

    def __init__(self, clazz, count):
        self.__clazz = clazz
        self.__fields = Vars(count)


    def is_instance_of(self, clazz):
        return clazz.is_assignable(self.__clazz)


    @property
    def clazz(self):
        return self.__clazz


    @property
    def fields(self):
        return self.__fields