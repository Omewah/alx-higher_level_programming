#!/usr/bin/python3

def common_elements(set_1, set_2):
    ident_ele = set()

    for element in set_1:
        if element in set_2:
            ident_ele.add(element)

    return ident_ele
