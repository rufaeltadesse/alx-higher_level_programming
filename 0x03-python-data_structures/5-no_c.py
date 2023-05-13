#!/usr/bin/env python3
def no_c(my_string):
    newstring = ''
    for x in range(len(my_string)):
        if (my_string[x] != 'C' and my_string[x] != 'c'):
            newstring += my_string[x]
    return newstring
