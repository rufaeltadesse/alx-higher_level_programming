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
        return(my_list[x-1])
    except IndexError:
        return my_list[size-1]
