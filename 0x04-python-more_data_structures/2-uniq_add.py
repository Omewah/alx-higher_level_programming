#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq_int = set()

    for element in my_list:
        if isinstance(element, int):
            uniq_int.add(element)

    add_all = sum(uniq_int)

    return add_all
