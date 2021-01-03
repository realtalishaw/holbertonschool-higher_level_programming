#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    a = a_dictionary
    for i in list(a):
        if a[i] == value:
            del a[i]
    return a
