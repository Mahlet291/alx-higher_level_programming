#!/usr/bin/python3
def multiple_returns(sentence):
    x = len(sentence)
    return(x, sentence[0] if sentence > 0 else None)
