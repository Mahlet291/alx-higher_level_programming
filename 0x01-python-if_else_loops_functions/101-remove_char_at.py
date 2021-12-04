#!/usr/bin/python3
def remove_char_at(str, n):
    string = ""
    for count, c in enumerate(str):
        if (count != n):
            string += c
    return (string)
