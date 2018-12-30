#encoding: utf-8
import traceback

from classfile import ClassReader
from instructions import InstructionFactory

class Interpreter(object):

    def __init__(self, thread):
        self.__thread = thread


    def interpret(self):
        thread = self.__thread
        try:
            self.loop(thread)
        except Exception as e:
            print(e)
            print(traceback.format_exc())


    def loop(self, thread):

        reader = ClassReader()
        while len(thread.stack) > 0:
            frame = thread.current_frame()
            pc = frame.next_pc
            thread.pc = pc

            reader.reset(frame.method.code, pc)

            opcode = reader.read_8_byte()
            instruction = InstructionFactory.get_instruction(int(opcode))
            instruction.fetch_operands(reader)
            frame.next_pc = reader.index

            #print(frame.method.clazz.name, frame.method.name, pc, instruction)
            instruction.execute(frame)
