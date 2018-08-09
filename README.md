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

I've made a simple script that allows you to handwrite `vm` commands into a separate text file, and execute them line-by-line called `vmex.py`. Say we wanted to execute `adder.vm`, we would simply write: `vmex.py adder.vm`, and it would execute.

This should make experimentation easier, instead of writing each command separately in a string, inside of a Python list.