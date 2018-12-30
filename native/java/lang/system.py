#encoding: utf-8

from native.base import Method
from native.method import register
from rtda.heap import StringFactory
from native.exceptions import MethodException

@register(class_name="java/lang/System", method_name="arrayCopy", descriptor="(Ljava/lang/Object;ILjava/lang/Object;II)V")
class MethodArrayCopy(Method):

    @classmethod
    def execute(cls, frame):
        src = frame.vars[0]
        src_pos = frame.vars[1]
        dst = frame.vars[2]
        dst_pos = frame.vars[3]
        length = frame.vars[4]

        if src is None or dst is None:
            raise MethodException('copy src or dst is None')

        if not src.clazz.is_array or not dst.clazz.is_array:
            raise MethodException('src or dst if not array object')

        if (src.clazz.component_class.is_primitive or dst.clazz.component_class.is_primitive) and src.clazz != dst_clazz:
            raise MethodException('src or dst is is_primitive but class is not equals')


        dst.fields[dst_pos:dst_pos + length] = src.fields[src_pos:src_pos + length]