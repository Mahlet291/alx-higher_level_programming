#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is not None:
        x = len(my_list)
        for i in range(x - 1):
            if my_list[i] > my_list[i + 1]:
                new_list = my_list[i]
                my_list[i] = my_list[i + 1]
                my_list[i + 1] = new_list
        return(my_list[x - 1])       
    else:
        return(None)
