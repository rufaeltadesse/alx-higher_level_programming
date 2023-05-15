#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if len(my_list) < 0 or idx >= len(my_list):
        return
    for x in range(len(my_list)):
        if x == idx:
            del my_list[x]
    return my_list
