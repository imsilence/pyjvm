#encoding: utf-8

from native.base import Method
from native.method import register

@register(class_name="java/lang/Float", method_name="floatToRawIntBits", descriptor="(F)I")
class MethodFloatToRawIntBits(Method):

    @classmethod
    def execute(cls, frame):
        frame.stack.push(struct.pack('>f', frame.vars[0]))