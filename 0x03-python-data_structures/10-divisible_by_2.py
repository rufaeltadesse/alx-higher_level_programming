#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    newlist = my_list.copy();
    for x in range(len(my_list)):
        if my_list[x] % 2 == 0:
            newlist[x] = True
        else:
            newlist[x] = False
    return newlist
