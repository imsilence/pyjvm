#encoding: utf-8

class ExceptionTableEntryFactory(object):

    @classmethod
    def parse(cls, reader):
        count = int(reader.read_16_byte())
        entries = []
        for _ in range(count):
            entry = ExceptionTableEntry()
            entry.read(reader)
            entries.append(entry)
        return entries


class ExceptionTableEntry(object):

    def __init__(self):
        self.__start_pc = 0
        self.__end_pc = 0
        self.__handler_pc = 0
        self.__catch_type = 0

    def read(self, reader):
        self.__start_pc = reader.read_16_byte()
        self.__end_pc = reader.read_16_byte()
        self.__handler_pc = reader.read_16_byte()
        self.__catch_type = reader.read_16_byte()

    def __repr__(self):
        return '<{0!r}>{1!r}'.format(self.__class__.__name__, vars(self))