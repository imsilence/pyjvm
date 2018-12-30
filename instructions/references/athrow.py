#encoding: utf-8

from .. import register
from ..base import NoOperandsInstruction
from ..exceptions import InstructionException
from rtda.heap import StringFactory


@register(opcode=0XBF)
class ATHROW(NoOperandsInstruction):

    def execute(self, frame):
        exception = frame.stack.pop()

        if exception is None:
            raise InstructionException('exception is None')


        if self.handle_caught_exception(frame.thread, exception):
            return

        self.handle_uncaught_exception(frame.thread, exception)


    def handle_caught_exception(self, thread, exception):
        while True:
            frame = thread.current_frame()
            pc = frame.next_pc - 1
            handler_pc = frame.method.find_exception_handler(exception.clazz, pc)
            if handler_pc > 0:
                frame.stack.clear()
                frame.stack.push(exception)
                frame.next_pc = handler_pc
                return True

            thread.pop_frame()
            if thread.is_empty_stack():
                break
        return False


    def handle_uncaught_exception(self, thread, exception):

        obj = exception.get_field_var('detailMessage', 'Ljava/lang/String;')
        string = StringFactory.object_2_string(obj)

        print('{0}:{1}'.format(exception.clazz.java_name, string))
        for line in exception.extra:
            print(line)