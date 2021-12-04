#!/usr/bin/python3
def uppercase(str):
    for word in str:
        if ord(word) > 96 and ord(word) < 123:
            word1 = chr(ord(word) - 32)
            print("{}".format(word1), end="")
        else:
            print("{}".format(word), end="")
