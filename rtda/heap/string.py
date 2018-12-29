#encoding: utf-8

from .object_ import Object

class StringFactory(object):

    __interneds = {}

    @classmethod
    def get(cls, loader, string):
        s = cls.__interneds.get(string)
        if s is None:
            chars = cls.utf8_2_utf16(string)
            chars_object = Object(loader.load('[C'), chars)

            s = loader.load('java/lang/String').create_object()
            field = s.clazz.get_field("value", "[C", False)
            s.fields[field.index] = chars_object
            cls.__interneds[string] = s

        return s


    @classmethod
    def utf8_2_utf16(cls, string):
        return list(string.encode('utf-16'))


    @classmethod
    def utf16_2_utf8(cls, chars):
        return bytes(chars).decode('utf-16')


    @classmethod
    def object_2_string(cls, s):
        field = s.clazz.get_field("value", "[C", False)
        chars = s.fields[field.index].fields
        return cls.utf16_2_utf8(chars)
