#encoding: utf-8

class ArrayObjectMixin(object):

    def __len__(self):
        return len(self.fields)


    def __getitem__(self, index):
        return self.fields[index]


    def __setitem__(self, index, value):
        self.fields[index] = value