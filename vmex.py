# vm executor for running commands line-by-line in a separate file.

import sys
import vm

opened = open(sys.argv[1], "r")
LINES = opened.read().splitlines()
opened.close()

index_counter = 0
for line in LINES:
    if line[0] == "#": # It's an integer; convert.
        LINES[index_counter] = int(line[1:])
    elif line[0] == "@": # It's a float; convert.
        LINES[index_counter] = float(line[1:])
    index_counter += 1

vm.Machine(LINES).run()