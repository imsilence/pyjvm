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
        loop(thread, method.code)
    except Exception as e:
        print(e)
        print(traceback.format_exc())
    finally:
        print(frame.stack)
        print(frame.localvars)


def loop(thread, code):
    frame = thread.pop_frame()
    reader = ClassReader(code)

    while True:
        pc = frame.next_pc
        thread.pc = pc

        reader.index = pc

        opcode = reader.read_8_byte()
        instruction = InstructionFactory.get_instruction(int(opcode))
        instruction.fetch_operands(reader)
        frame.next_pc = reader.index

        print(pc, instruction)
        instruction.execute(frame)