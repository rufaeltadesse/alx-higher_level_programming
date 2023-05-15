#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if len(my_list) < 0 or idx >= len(my_list):
        return
    new_list = []
    for x in range(len(my_list)):
        if x != idx:
            new_list.append(my_list[x])
    my_list.clear()
    for x in new_list:
        my_list.append(x)
    return new_list
