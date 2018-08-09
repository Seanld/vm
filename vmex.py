# vm executor for running commands line-by-line in a separate file.

import sys
import vm

opened = open(sys.argv[1], "r")
LINES = opened.read().splitlines()
opened.close()

vm.Machine(LINES).run()