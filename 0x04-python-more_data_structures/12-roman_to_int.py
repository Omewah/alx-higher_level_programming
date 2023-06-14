#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_val =
    {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    convert = 0
    p_val = 0

    for char in reversed(roman_string):
        val = roman_val.get(char, 0)

        if val < p_val:
            convert -= val
        else:
            convert += val

        p_val = val

    return convert
