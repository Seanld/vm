from __future__ import print_function

from collections import deque
import sys

class Stack (deque):
    push = deque.append

    def top(self):
        return self[-1]

class Machine:
    def __init__(self, code):
        self.data_stack = Stack()
        self.return_addr_stack = Stack()
        self.instruction_pointer = 0
        self.code = code
        self.variables = {}
        self.dispatch_map = {
            "%": self.mod,
            "^": self.exp,
            "*": self.mul,
            "+": self.plus,
            "-": self.minus,
            "/": self.div,
            "cast_int": self.cast_int,
            "cast_float": self.cast_float,
            "cast_str": self.cast_str,
            "concat": self.concat,
            # "drop": self.drop,
            # "dup": self.dup,
            "jmp_if": self.jmp_if_stmt,
            "jmp": self.jmp,
            "==": self.eq,
            ">": self.greater,
            "<": self.less,
            ">=": self.greater_eq,
            "<=": self.less_eq,
            "over": self.over,
            "print": self.print,
            "println": self.println,
            "read": self.read,
            "store": self.store,
            "load": self.load,
            "delete": self.delete,
            # "stack": self.dump_stack,
            # "swap": self.swap,
            "exit_fail": self.exit_fail,
            "exit_good": self.exit_good
        }

    def pop(self):
        return self.data_stack.pop()
    def push(self, value):
        self.data_stack.push(value)
    def top(self):
        return self.data_stack.top()

    def run(self):
        while self.instruction_pointer < len(self.code):
            opcode = self.code[self.instruction_pointer]
            self.instruction_pointer += 1
            self.dispatch(opcode)
    
    def dispatch(self, op):
        if op in self.dispatch_map:
            self.dispatch_map[op]()
        elif isinstance(op, int):
            self.push(op)
        elif isinstance(op, str) and op[0] == op[-1] == '"':
            self.push(op[1:-1])
        else:
            # raise RuntimeError("Unknown opcode: '%s'" % op)
            self.push(op)
    
    # ARITHMETIc

    def plus(self):
        first = self.pop()
        self.push(self.pop() + first)
    def minus(self):
        last = self.pop()
        self.push(self.pop() - last)
    def mul(self):
        self.push(self.pop() * self.pop())
    def div(self):
        last = self.pop()
        self.push(self.pop() / last)
    def mod(self):
        last = self.pop()
        self.push(self.pop() % last)
    def exp(self):
        last = self.pop()
        self.push(pow(self.pop(), last))
    
    # IO FUNCTIONALITY

    def print(self):
        sys.stdout.write(str(self.pop()))
        sys.stdout.flush()
    def println(self):
        sys.stdout.write("%s\n" % self.pop())
        sys.stdout.flush()
    def read(self):
        self.push(input(self.pop()))
    
    # CONDITIONALS AND BRANCHING

    def jmp(self):
        addr = self.pop()
        if isinstance(addr, int) and 0 <= addr <= len(self.code):
            self.instruction_pointer = addr
        else:
            raise RuntimeError("Jump address must be a valid integer.")
    
    def jmp_if_stmt(self):
        false_jump_address = self.pop()
        true_jump_address = self.pop()
        test = self.pop()

        if type(test).__name__ == 'bool':
            if test == True:
                self.instruction_pointer = true_jump_address - 1
            elif test == False:
                self.instruction_pointer = false_jump_address - 1

        else:
            print('ERROR: jump-if condition not boolean')

    # COMPARISON OPERATORS

    def eq(self):
        if self.pop() == self.pop():
            self.push(True)
        else:
            self.push(False)
    def greater(self):
        if self.pop() > self.pop():
            self.push(True)
        else:
            self.push(False)
    def less(self):
        if self.pop() < self.pop():
            self.push(True)
        else:
            self.push(False)
    def greater_eq(self):
        if self.pop() >= self.pop():
            self.push(True)
        else:
            self.push(False)
    def less_eq(self):
        if self.pop() <= self.pop():
            self.push(True)
        else:
            self.push(False)
    
    # TYPE CONVERSIONS

    def cast_int(self):
        self.push(int(self.pop()))
    def cast_float(self):
        self.push(float(self.pop()))
    def cast_str(self):
        self.push(str(self.pop()))
    def concat(self):
        last = self.pop()
        self.push(self.pop() + last)
    
    # DATA STORAGE AND PERSISTENCE

    def store(self):
        last = self.pop()
        first = self.pop()
        # print(last, first)
        self.variables[last] = first
    def load(self):
        self.push(self.variables[self.pop()])
    def delete(self): # Erases stored data to prevent overflow.
        del self.variables[self.pop()]
    
    def exit_fail(self):
        exit(1)
    def exit_good(self):
        exit(0)
    
    def over(self):
        a = self.pop()
        b = self.pop()
        self.push(b)
        self.push(a)
        self.push(b)