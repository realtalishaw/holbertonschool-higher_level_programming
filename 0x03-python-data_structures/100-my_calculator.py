#!/usr/bin/python3

from sys import argv, exit
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    if(len(argv) != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    av_a = int(argv[1])
    av = argv[2]
    av_b = int(argv[3])
    if(av == "+"):
        print("{} + {} = {}".format(av_a, av_b, add(av_a, av_b)))
    elif(av == '/'):
        print("{} / {} = {}".format(av_a, av_b, div(av_a, av_b)))
    elif(av == "-"):
        print("{} - {} = {}".format(av_a, av_b, sub(av_a, av_b)))
    elif(av == '*'):
        print("{} * {} = {}".format(av_a, av_b, mul(av_a, av_b)))
    else:
        print("Unknown operator. Available operators: +, -, * and / ")
        exit(1)
