#!/usr/bin/python3
for i in range(100):
    if i in range(99):
        print('{}, '.format(format(i, '02d')), end='')
    else:
        print(i)
