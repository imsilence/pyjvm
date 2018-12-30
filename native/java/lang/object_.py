#encoding: utf-8

import copy

from native.base import Method
from native.method import register
from rtda.heap import StringFactory
from native.exceptions import MethodException


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



@register(class_name="java/lang/Object", method_name="clone", descriptor="()Ljava/lang/Object;")
class MethodClone(Method):

    @classmethod
    def execute(cls, frame):
        this = frame.vars[0]
        cloneable = this.clazz.loader.load('java/lang/Cloneable')
        if not this.clazz.is_implements(cloneable):
            raise MethodException("object not implements cloneable")

        frame.stack.push(this.copy())
