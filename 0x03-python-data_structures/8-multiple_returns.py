#!/usr/bin/python3
def multiple_returns(sentence):
    first = sentence[:1]
    length = len(sentence)
    if len(sentence) == 0:
        first = None
    return length, first
