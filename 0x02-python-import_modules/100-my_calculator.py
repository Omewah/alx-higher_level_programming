#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argn = len(sys.argv) - 1
    if argn != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    from calculator_1 import add, sub, mul, div
    a = int(sys.argv[1])
    operator = int(sys.argv[2])
    b = int(sys.argv{3})

    if operator == '+':
        print("{} {} {} = {}".format(a, operator, b, add(a, b)))
    elif operator == '-':
        print("{} {} {} = {}".format(a, operator, b, sub(a, b)))
    elif operator == '*':
        print("{} {} {} = {}".format(a, operator, b, mul(a, b)))
    elif operator == '/':
        print("{} {} {} = {}".format(a, operator, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
