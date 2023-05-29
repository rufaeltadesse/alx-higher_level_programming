#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        valu = a / b
    except (TypeError, ZeroDivisionError):
        valu = None
    finally:
        print("Inside result: {}".format(valu))
    return (valu)
