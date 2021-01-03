#!/usr/bin/python3


def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0

    rs = roman_string
    res = 0
    key = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    for i in range(len(rs)):
        if i < len(rs) - 1 and key[rs[i]] < key[rs[i + 1]]:
            res -= key[rs[i]]
        else:
            res += key[rs[i]]
    return res
