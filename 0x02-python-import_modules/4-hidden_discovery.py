#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    sortedStr = sorted(dir(hidden_4))
    for x in range(len(sortedStr)):
        if sortedStr[x].startswith("__") == False:
            print(sortedStr[x])
