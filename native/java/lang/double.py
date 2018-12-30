#encoding: utf-8

from native.base import Method
from native.method import register

@register(class_name="java/lang/Double", method_name="doubleToRawIntBits", descriptor="(D)I")
class MethodDoubleToRawIntBits(Method):

    @classmethod
    def execute(cls, frame):
        frame.stack.push(struct.pack('>d', frame.vars[0]))