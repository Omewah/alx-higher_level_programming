#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    last_list = []
    try:
        for i in range(list_length):
            try:
                E1 = my_list_1[i]
                E2 = my_list_2[i]
                result = E1 / E2
            except (ValueError, TypeError):
                print("wrong type")
                result = 0
            except ZeroDivisionError:
                print("division by 0")
                result = 0
            except IndexError:
                print("out of range")
                result = 0
            finally:
                last_list.append(result)
            return last_list
