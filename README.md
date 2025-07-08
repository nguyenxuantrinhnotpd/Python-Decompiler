# 🧠 Simple Python Bytecode Decompiler

> **Author**: Nguyễn Xuân Trịnh  
> **Telegram**: [@CalceIsMe](https://t.me/CalceIsMe)

> ⚠️ **Note**:  
> This is a **simple Python decompiler** that supports a limited set of opcodes.  
> You can extend it to handle more instructions depending on your needs.

---

## 📜 Description

This tool decompiles basic Python bytecode back into source code using a custom interpreter that simulates Python’s stack-based virtual machine. It is primarily intended for educational or debugging purposes.

---

## 🔧 How It Works

The decompiler processes bytecode as follows:

1. **Disassemble Bytecode**  
   Uses `dis.get_instructions()` to iterate through bytecode instructions.

2. **Stack Simulation**  
   Maintains an internal stack to simulate Python’s evaluation stack and process values.

3. **Opcode Handling**  
   Each recognized opcode is translated into a corresponding line of source code (e.g., function calls, return statements).

4. **AST Formatting**  
   Reconstructed code is passed through Python’s `ast` module to format it and ensure syntactic correctness.

5. **Output**  
   Displays:
   - List of opcodes encountered
   - Decompiled source code
   - Final stack state

---

## 🔍 Supported Opcodes and Their Handling

| Opcode         | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| `RESUME`       | Ignored. Used internally by the interpreter.                                |
| `PUSH_NULL`    | Pushes `None` onto the stack.                                               |
| `LOAD_CONST`   | Pushes a constant value (e.g. number, string, `None`) onto the stack.       |
| `LOAD_NAME`    | Pushes a variable or function name onto the stack.                          |
| `CALL`         | Pops arguments and function name to reconstruct function calls.             |
| `POP_TOP`      | Discards the top value of the stack.                                        |
| `RETURN_CONST` | Emits a `return` or `return <value>` statement (only if inside a function). |
| _Other_        | Printed as `Unsupported Opcode <NAME>` for extension or debugging.          |

---

## 🧪 Example

### Input Source:
```python
print("Hello World!")
print(a, b)
```
### Output:
```python
LOAD_NAME
LOAD_CONST
CALL
POP_TOP
LOAD_NAME
LOAD_NAME
CALL
POP_TOP
RETURN_CONST
====================
print('Hello World!')
print(a, b)
====================
Stack Remaining: []
```
---

### 📝 License

This project is open-source and free to use or modify.


---

### 📫 Contact

Telegram: [@CalceIsMe](https://t.me/CalceIsMe)
