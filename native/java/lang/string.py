#encoding: utf-8

from native.base import Method
from native.method import register
from rtda.heap import StringFactory

@register(class_name="java/lang/String", method_name="intern", descriptor="()Ljava/lang/String;")
class MethodIntern(Method):

    @classmethod
    def execute(cls, frame):
        frame.stack.push(StringFactory.get_from_object(frame.vars[0]))