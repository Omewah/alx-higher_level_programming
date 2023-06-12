#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list

    update_list = []
    for integer in range(len(my_list)):
        if integer != idx:
            update_list.append(my_list[integer])

    return update_list
