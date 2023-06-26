#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    last_list = []
    try:
        for i in range(list_length):
            try:
                E1 = my_list_1[i]
                E2 = my_list_2[i]
                if isinstance(E1, (int, float))
                and isinstance(E2, (int, float)):
                    if E2 != 0:
                        last_list.append(E1 / E2)
                    else:
                        last_list.append(0)
                else:
                    print("wrong type")
                    last_list.append(0)
            except IndexError:
                print("out of range")
                last_list.append(0)
            except ZeroDivisionError:
                print("division by 0")
                last_list.append(0)
        finally:
            return last_list
