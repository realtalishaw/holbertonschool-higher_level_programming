#!/usr/bin/python3

"ghksflkshdlf hh lshdf jsdkjfklsdj kljfksdjfkjd"


class Rectangle:
    number_of_instances = 0


    """g lks jdks jl mgddffsdf sdfsd fsd gsfs sfgs s """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

   # Rectangle.number_of_instances += 1

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return self.width * 2 + self.height * 2

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        print_symbol = "#"
        rectangle = str(print_symbol) * self.width
        return "\n".join(list(rectangle for i in range(self.height)))

    def __repr__(self):
        if self.width == 0 or self.height == 0:
            return ""
        return "Rectangle ({}, {})".format(self.width, self.height)

    def __del__(self):
      #  Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("recy_2 must be an instance of Rectangle")
        if rect_1.area == rect_2.area:
            return rect_1
        if rect_2.area() < rect_1.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
