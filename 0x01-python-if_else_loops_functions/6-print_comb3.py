#!/usr/bin/python3
for n in range(1, 90, 11):
    for i in range(n, int(n/10)*10+10):
        if i in range(89):
            print("{}, ".format(format(i, '02d')), end='')
        else:
            print(n)
