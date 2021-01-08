#!/usr/bin/python3
from doctest import testmod

def add_integer(a, b=98):
    """
    define input and expected output:
    >>> add_integer(1, 2)
    3
    >>> add_integer(100, -2)
    98
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b

if __name__ == "__main__":
    testmod(name="add_integer", verbose = True)
