#!/usr/bin/python3
if __name__ == "__import__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    result_add = add(a, b)
    result_sub = sub(a, b)
    result_mul = mul(a, b)
    result_div = div(a, b)

    print("The return value of {} + {} = {}".format(a, b, result_add))
    print("The return value of {} - {} = {}".format(a, b, result_sub))
    print("The return value of {} * {} = {}".format(a, b, result_mul))
    print("The return value of {} / {} = {}".format(a, b, result_div))
