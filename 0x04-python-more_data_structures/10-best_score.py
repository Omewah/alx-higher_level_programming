#!/usr/bin/python3

def best_score(a_dictionary):
    high_score = None
    high_key = None

    for key, value in a_dictionary.items():
        if high_score is None or value > high_score:
            high_score = value
            high_key = key

    return high_key
