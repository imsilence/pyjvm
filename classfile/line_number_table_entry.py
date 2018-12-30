#encoding: utf-8

class LineNumberTableEntryFactory(object):

    @classmethod
    def parse(cls, reader):
        count = int(reader.read_16_byte())
        entries = []
        for _ in range(count):
            entry = LineNumberTableEntry()
            entry.read(reader)
            entries.append(entry)
        return entries


class LineNumberTableEntry(object):

    def __init__(self):
        self.__start_pc = 0
        self.__line_number = 0

    def read(self, reader):
        self.__start_pc = reader.read_16_byte()
        self.__line_number = reader.read_16_byte()


    @property
    def start_pc(self):
        return int(self.__start_pc)


    @property
    def line_number(self):
        return int(self.__line_number)


    def __repr__(self):
        return '<{0!r}>{1!r}'.format(self.__class__.__name__, vars(self))