#!/usr/bin/python3
def multiple_returns(sentence):
    L = len(sentence)
    C = sentence[0] if L > 0 else None
    return L, C
