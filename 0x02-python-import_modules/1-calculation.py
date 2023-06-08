#!/usr/bin/python3
if __name__ == "__import__":
    from calculator_1 import add, subtract, multiply, divide

    a = 10
    b = 5

    result_add = add(a, b)
    result_subtract = subtract(a, b)
    result_multiply = multiply(a, b)
    result_divide = divide(a, b)

    print("The return value of {} + {} = {}".format(a, b, result_add))
    print("The return value of {} - {} = {}".format(a, b, result_subtract))
    print("The return value of {} * {} = {}".format(a, b, result_multiply))
    print("The return value of {} / {} = {}".format(a, b, result_divide))
