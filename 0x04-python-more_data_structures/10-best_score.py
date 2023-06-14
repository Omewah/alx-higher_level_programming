#!/usr/bin/python3

def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    high_key = list(a_dictionary.keys())[0]
    high_score = a_dictionary[high_key]

    for key, value in a_dictionary.items():
        if high_score is None or value > high_score:
            high_score = value
            high_key = key

    return high_key
