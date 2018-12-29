#encoding: utf-8


from .. import register
from ..base import NoOperandsInstruction
from ..exceptions import InstructionException
from native import MethodFactory

@register(opcode=0XFE)
class INVOKE_NATIVE(NoOperandsInstruction):

    def execute(self, frame):
        method = frame.method
        native_method = MethodFactory.get_method(method.clazz.name, method.name, method.descriptor)
        native_method(frame)
