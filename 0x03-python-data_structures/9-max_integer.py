#!/usr/bin/python3
def max_integer(my_list=[]):
    x = len(my_list)
    if my_list is not None:
        for i in range(x - 1):
            if my_list[i] > my_list[i + 1]:
                new_list = my_list[i + 1]
                my_list[i] = my_list[i + 1]
                my_list[i + 1] = new_list
            return(my_list[x - 1])       
    else:
        return(None)
