def calculator(operation:str, z1:complex, z2:complex)->complex:
    if operation == "add":
        return z1+z2
    elif operation == "subtraction":
        return z1-z2
    elif operation == "multiplication":
        return z1*z2
    elif operation == "division":
        return z1/z2

assert calculator('add',complex(2,3),complex(4,5)) == 6+8j
assert calculator('add',complex(2,3),complex(4,5)) == -2+2j
assert calculator('add',complex(2,3),complex(4,5)) == -2+2j
print(calculator('add',complex(2,3),complex(4,5)))
print(calculator('subtraction',complex(2,3),complex(4,5)))
print(calculator('multiplication',complex(2,3),complex(4,5)))
print(calculator('division',complex(2,3),complex(4,5)))