#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sumValue = 0
    for x in range(len(sys.argv)-1):
        sumValue = sumValue + int(sys.argv[x+1])
    print(sumValue)
