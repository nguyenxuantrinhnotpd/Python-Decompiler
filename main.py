"""
@Author: Nguyễn Xuân Trịnh 
@Telegram: CalceIsMe
@Note:
THIS IS A SIMPLE DECOMPILER THAT SUPPORTS SIMPLE PYTHON OPCODES.
IF YOU WANT MORE, THEN CODE TO SUPPORT OTHER OPCODES.
"""
import dis
class DECOMPILER:
    def __init__(self, bytecode):
        self.bytecode = bytecode
        self.stack = []
        self.source_code = []
        self.in_function = False
    def decompile(self):
        opcodes = []
        for instr in dis.get_instructions(self.bytecode):
            if instr.opname == 'RESUME':
                pass
            elif instr.opname == 'PUSH_NULL':
                self.stack.append(None)
            elif instr.opname == 'LOAD_CONST':
                self.stack.append(instr.argrepr)
            elif instr.opname == 'LOAD_NAME':
                self.stack.append(instr.argval)
            elif instr.opname == 'CALL':
                args = []
                for _ in range(instr.arg):
                    args.append(self.stack.pop())
                args = args[::-1]
                func = self.stack.pop()
                self.stack.pop()
                self.stack.append(f"{func}({', '.join(args)})")
            elif instr.opname == 'POP_TOP':
                if self.stack:
                    self.source_code.append(self.stack.pop())
            elif instr.opname == 'RETURN_CONST':
                v = instr.argval
                if self.in_function:
                    if v is None:
                        self.source_code.append("return")
                    else:
                        self.source_code.append(f"return {repr(v)}")
            else:
                self.source_code.append(f"# Unsupported Opcode {instr.opname}")
            opcodes.append(instr.opname)
        for opcode in opcodes:
            print(opcode)
        print("= "*10)
        self.source_code = '\n'.join(self.source_code)
        print(self.source_code)
        print("= "*10)
        print("Stack Remaning:",self.stack)
code = """
print("Hello Wolrd!")
print(a, b)
"""
bytecode = compile(code,"<string>","exec")
dis.dis(bytecode)
decompile = DECOMPILER(bytecode).decompile()
