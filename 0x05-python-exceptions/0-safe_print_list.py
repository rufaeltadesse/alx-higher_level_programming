#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        size = 0
        for i in my_list:
            print(i, end='')
            size = size + 1
            if i == x:
                break
        print()
        return size
    except IndexError:
        return size
