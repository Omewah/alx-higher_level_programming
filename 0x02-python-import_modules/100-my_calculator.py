#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argn = len(sys.argv) - 1
    if argn != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    opr = sys.argv[2]
    if opr != '+' and opr != '-' and opr != '*' and opr != '/':
        print('Unknown operator. Available operators: +, -, * and /')
        sys.exit(1)

    from calculator_1 import add, sub, mul, div
    a = int(sys.argv[1])
    b = int(sys.argv{3})

    if opr == '+':
        print('{} {} {} = {}'.format(a, opr, b, add(a, b)))
    elif opr == '-':
        print('{} {} {} = {}'.format(a, opr, b, sub(a, b)))
    elif opr == '*':
        print('{} {} {} = {}'.format(a, opr, b, mul(a, b)))
    else:
        print('{} {} {} = {}'.format(a, opr, b, div(a, b)))
