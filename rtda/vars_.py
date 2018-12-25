#encoding: utf-8

class Vars(object):

    def __init__(self, length):
        self.__vars = [None] * length


    def __getitem__(self, index):
        return self.__vars[index]


    def __setitem__(self, index, value):
        self.__vars[index] = value


    def __len__(self):
        return len(self.__vars)


    def __repr__(self):
        return '<{0!r}>{1!r}'.format(self.__class__.__name__, vars(self))