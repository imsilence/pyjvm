#encoding: utf-8

from .exceptions import MethodException
from .base import EmptyMethod

class MethodFactory(object):
    METHOD_MAP = {}

    @classmethod
    def get_method(cls, class_name, method_name, descriptor):
        key = '{1}.{2}.{3}'.format(class_name, method_name, descriptor)
        method = cls.METHOD_MAP.get(key)
        if method is None:
            if method_name == 'registerNatives' and descriptor == '()V':
                return EmptyMethod
            raise MethodException('method [{0}] not found'.format(key))
        return method


def register(opcode):
    def wrapper(cls, class_name, method_name, descriptor):
        key = '{1}.{2}.{3}'.format(class_name, method_name, descriptor)
        MethodFactory.METHOD_MAP[key] = cls
        return cls
    return wrapper