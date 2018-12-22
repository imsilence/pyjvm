#encoding: utf-8

from .class_member import ClassMember

class ClassMethod(ClassMember):

    def __init__(self, class_, method):
        super(ClassMethod, self).__init(class_, method)
        self.__max_stack = 0
        self.__max_locals = 0
        self.__code = b''
        if method.code_attr:
            self.__max_stack = method.code_attr.max_stack
            self.__max_locals = method.code_attr.max_locals
            self.__code = method.code_attr.code.byte
