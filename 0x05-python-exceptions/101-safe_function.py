#!/usr/bin/python3
from sys import stderr
def safe_function(fct, *args):
    try:
        safe = fct(*args)
    except Exception as fail:
        stderr.write("Exception: {}\n".format(fail))
        return None
    return safe
