#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return (None)
    else:
        keys = a_dictionary.keys()
        firstData = 1
        maxValue = 0
        maxReturn = ""
        for i in keys:
            if firstData == 1:
                maxValue = a_dictionary[i]
                maxReturn = i
                firstData = 0
            if maxValue < a_dictionary[i]:
                maxReturn = i
                maxValue = a_dictionary[i]
        return maxReturn
