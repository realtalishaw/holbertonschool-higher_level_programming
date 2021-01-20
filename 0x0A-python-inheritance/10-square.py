#!/usr/bin/python3


"djfjkhd jhj hdfjkhgkjd gjd"


class BaseGeometry:
    """f jjfjdk jdkfj kdfgdf"""
    def area(self):
        raise Exception("area() is not implemented")
    """vldfkl flk dflkvdfl;k vd;lfkvld;f"""
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise TypeError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """kjffkdjgkskl jkfdjvdjfd"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
    """dkf kfkdl jjgdfkl jkgdfj kgd"""
    def area(self):
        return self.__width * self.__height
    """fkdljfkdj kjdklsjskjlfksjf"""
    def __str__(self):
        return("[Rectangle] {}/{}".format(self.__width, self.__height))


class Square(Rectangle):
    "jfkdj sk hfjkshdjk hsjdhf kshv"
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
