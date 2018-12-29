#encoding: utf-8

from ..vars_ import Vars
from .array_object import ArrayObjectMixin

class Object(ArrayObjectMixin, object):

    def __init__(self, clazz, fields):
        self.__clazz = clazz
        self.__fields = fields


    def is_instance_of(self, clazz):
        return clazz.is_assignable(self.__clazz)


    @property
    def clazz(self):
        return self.__clazz


    @property
    def fields(self):
        return self.__fields


    def __str__(self):
        return '<{0!r}>{1!r}'.format(self.clazz.name, [str(field) for field in self.fields])