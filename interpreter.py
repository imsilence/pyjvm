#encoding: utf-8
import traceback

from rtda import Thread
from classfile import ClassReader
from instructions import InstructionFactory

def interpret(method):
    thread = Thread()
    frame = thread.create_frame(method)
    thread.push_frame(frame)
    try:
        loop(thread)
    except Exception as e:
        print(e)
        print(traceback.format_exc())
    finally:
        print(frame.stack)
        print(frame.vars)


def loop(thread):

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

        print(frame.method.clazz.name, frame.method.name, pc, instruction)
        instruction.execute(frame)
