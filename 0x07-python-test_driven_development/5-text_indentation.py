#!/usr/bin/python3

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.replace(".", ".\n\n")
    text = text.replace(":", ":\n\n")
    text = text.replace("?", "?\n\n")
    text = text.split("\n")
    for char in range(0, len(text)):
        print("{:s}".format(text[char].strip()),
              end=("" if (char == len(text) - 1) else "\n"))
