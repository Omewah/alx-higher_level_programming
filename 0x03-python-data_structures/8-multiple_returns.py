#!/usr/bin/python3

def multiple_returns(sentence):
    lg = len(sentence)
    char_1 = sentence[0] if lg > 0 else None
    return (lg, char_1)
