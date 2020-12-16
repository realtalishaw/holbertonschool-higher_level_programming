#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    total = 0
    if len(argv) - 1 > 0:
        if len(argv) - 1 == 1:
            print("{:d}".format(int(argv[1])))
        else:
            for i in range(len(argv) - 1):
                total = total + int(argv[i + 1])
            print('{:d}'.format(total))
    else:
        print("0")
