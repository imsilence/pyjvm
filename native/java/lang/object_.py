#encoding: utf-8

from native.base import Method
from native.method import register
from rtda.heap import StringFactory

@register(class_name="java/lang/Object", method_name="getClass", descriptor="()Ljava/lang/Class;")
class MethodGetClass(Method):

    @classmethod
    def execute(cls, frame):
        this = frame.vars[0]
        clazz = this.clazz.base_class
        frame.stack.push(clazz)



@register(class_name="java/lang/Object", method_name="hashCode", descriptor="()I")
class MethodHashCode(Method):

    @classmethod
    def execute(cls, frame):
        frame.stack.push(id(frame.vars[0]))

