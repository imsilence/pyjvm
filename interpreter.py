#encoding: utf-8

from rtda import Thread
from classfile import ClassReader
from instructions import InstructionFactory

def interpret(method):
    max_stack = method.code_attr.max_stack
    max_locals = method.code_attr.max_locals
    code = method.code_attr.code

    thread = Thread()
    frame = thread.create_frame(max_stack, max_locals)
    thread.push_frame(frame)
    try:
        loop(thread, code)
    except Exception as e:
        import traceback
        print(e)
        print(traceback.format_exc())
    finally:
        print(frame.stack)
        print(frame.localvars)

def loop(thread, code):
    frame = thread.pop_frame()
    reader = ClassReader(code.byte)

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