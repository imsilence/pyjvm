#encoding: utf-8

class ExceptionTableEntry(object):


    def __init__(self, method, constant_pool, exception):
        self.__start_pc = exception.start_pc
        self.__end_pc = exception.end_pc
        self.__handler_pc = exception.handler_pc
        self.__catch_type = None if exception.catch_type == 0 else constant_pool[exception.catch_type]

    @property
    def start_pc(self):
        return self.__start_pc


    @property
    def end_pc(self):
        return self.__end_pc


    @property
    def handler_pc(self):
        return self.__handler_pc


    @property
    def catch_type(self):
        return self.__catch_type
