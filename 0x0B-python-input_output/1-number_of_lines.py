#!/usr/bin/python3

def number_of_lines(filename=""):
    """kdjfdf dfsdfss"""
    lines = 0
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            lines += 1
    return lines
