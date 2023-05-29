#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    mylist = []
    for val in range(0, list_length):
        try:
            valu = my_list_1[val] / my_list_2[val]
        except TypeError:
            print("wrong type")
            valu = 0
        except ZeroDivisionError:
            print("division by 0")
            valu = 0
        except IndexError:
            print("out of range")
            valu = 0
        finally:
            mylist.append(valu)
    return (mylist)
