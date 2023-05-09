#!/usr/bin/python3
temp = 0
for char in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(char - temp)), end="")
    if temp == 0: 
        temp = 32 
    else:
        temp = 0
