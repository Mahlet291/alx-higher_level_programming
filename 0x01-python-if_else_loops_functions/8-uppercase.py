#!/usr/bin/python3
def uppercase(str):
    for word in str:
        if ord(word) >= 97 and ord(word) <= 127:
            print("{}".format(chr(ord(word) - 32)), end="")
        else:
            print("{}".format(word), end="")
