#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    can_div = []

    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            can_div.append(True)
        else:
            can_div.append(False)

    return (can_div)
