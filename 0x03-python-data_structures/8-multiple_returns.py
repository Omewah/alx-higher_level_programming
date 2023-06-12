#!/usr/bin/python3

def multiple_returns(sentence):
    l = len(sentence)
    char_1 = sentence[0] if l > 0 else None
    return (l, char_1)
