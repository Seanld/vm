# VM

My own personal stack-based virtual machine.

Mainly implemented for use as a compile target for my other personal programming language projects.

## Features

- Currently has support for many math operators
    - Addition
    - Subtraction
    - Multiplication
    - Division
    - Modulus
    - Exponents
- Value printing (ints and strings), so console output is possible
- Jump instruction support coming soon
- Other more advanced instructions pending

## Line-by-line Execution

Executing instructions is now easier. You can use `vmex.py` as a terminal command to execute a separate line-by-line bytecode file, rather than constructing your own `Machine` class instance, and then writing the code as a Python list of strings. Now just put it in a file.

To test it on the multiplication calculator program, type `python3 vmex.py multiplier.vm`, and then start multiplying!

---

**NOTE:** When writing programs in separate text files, integers must be defined specifically by putting a `#` before the number. As for floats, use a `@`.

For example, if you wanted to use the integer `5` in your code somewhere, you can't just write `5` as if you were putting it in a Python list as an integer. Since it's in a separate file, the interpreter will think it's an opcode, and will fail. You would need to write `#5` for it to work. Say you had the float `0.5`, you'd need to write `@0.5` for `vmex.py` to recognize that it's a float, not an opcode.