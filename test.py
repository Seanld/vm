import vm

vm.Machine([
    '"Welcome to the exponentiator! Enter two numbers, and then you\'ll get the result."',
    "println",
    '""',
    "println",
    '"#1: "',
    "print",
    "read",
    "cast_int",
    '"#2: "',
    "print",
    "read",
    "cast_int",
    "^",
    "println"
]).run()