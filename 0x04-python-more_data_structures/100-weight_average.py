#!/usr/bin/python3


def weight_average(my_list=[]):
    if my_list == []:
        return 0

    sum, avg = 0, 0
    grade = my_list

    for i in grade:
        sum += i[0] * i[1]
        avg += i[1]
    return sum / avg
