#!/usr/bin/python3
for i in range(122, 96):
    print("{:c}".format(chr(i - 32)) if i % 2 == 0 else "{:c}".format(chr(i)), end="") 
    
