#!/usr/bin/python3

"ghksflkshdlf hh lshdf jsdkjfklsdj kljfksdjfkjd"


class Square:
    """g lks jdks jl mgddffsdf sdfsd fsd gsfs sfgs s """
    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size > 0:
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                for n in range(self.__position[0]):
                    print(" ", end="")
                for n in range(self.__size):
                    print("#", end="")
                print("")
        else:
            print("")
