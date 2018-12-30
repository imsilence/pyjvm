#encoding: utf-8

from native.base import Method
from native.method import register
from instructions.references.invoke import InvokeMixin

@register(class_name="sun/misc/VM", method_name="initialize", descriptor="()V")
class MethodInitialize(InvokeMixin, Method):

    @classmethod
    def execute(cls, frame):
        pass