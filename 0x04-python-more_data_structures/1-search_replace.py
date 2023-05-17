#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newlist = my_list.copy()
    for i in range(len(my_list)):
        newlist = list(map(lambda x: x if x != search else replace, my_list))
    return newlist
