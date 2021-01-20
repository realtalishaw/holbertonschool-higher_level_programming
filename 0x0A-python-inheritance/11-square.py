#!/usr/bin/python3

" jkldfj fdjkl jfdgkj"


class BaseGeometry:
    """ lkjdflkj kjdf jkdfdf"""
    def area(self):
        raise Exception("area() is not implemented")
    """kflkjdkj lksjdfksj kfsjldkfjs"""
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise TypeError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """kdl kjsdjf sjflkjsdkfjsd"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
    """ksdj kjdflksj kjfksj klfsdj"""
    def area(self):
        return self.__width * self.__height
    """dkflsdl kfldskfl;sdkl; kflskdfsld"""
    def __str__(self):
        return("[Rectangle] {}/{}".format(self.__width, self.__height))


class Square(Rectangle):
    """kfdkl lsjfdlksl jfksjfls"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
    """kdldsjflkjds lkjskfjslfjlsdk"""
    def __str__(self):
        return("[Square] {}/{}".format(self.__size, self.__size))
