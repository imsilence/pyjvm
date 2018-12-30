#encoding: utf-8

from native.base import Method
from native.method import register
from instructions.references.invoke import InvokeMixin

@register(class_name="sun/misc/VM", method_name="initialize", descriptor="()V")
class MethodInitialize(InvokeMixin, Method):

    @classmethod
    def execute(cls, frame):
        loader = frame.method.clazz.loader
        clazz = loader.load('java/lang/System')
        method = clazz.get_static_method("initializeSystemClass", "()V")
        self.invoke_method(frame, method)