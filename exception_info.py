#encoding: utf-8

class ExceptionFactory(object):

    @classmethod
    def parse(cls, reader):
        count = int(reader.read_16_byte())
        exceptions = []
        for _ in exceptions:
            exception = ExceptionInfo()
            exception.parse(reader)
            exceptions.append(exception)
        return exceptions


class ExceptionInfo(object):

    def __init__(self):
        self.__start_pc = 0
        self.__end_pc = 0
        self.__handler_pc = 0
        self.__catch_type = 0

    def parse(self):
        self.__start_pc = int(reader.read_16_byte())
        self.__end_pc = int(reader.read_16_byte())
        self.__handler_pc = int(reader.read_16_byte())
        self.__catch_type = int(reader.read_16_byte())