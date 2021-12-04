#!/usr/bin/python3
def uppercase(str):
    word1 = ""
    for word in str:
        if ord(word) > 96 and ord(word) < 123:
            word1 += chr(ord(word) - 32)
        else:
            word1 += word
    print("{} ".format(word1), end="")
