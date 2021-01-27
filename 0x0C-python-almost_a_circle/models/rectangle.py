#!/usr/bin/python3
"""lfkldkfl fdsfsd"""
from models.base import Base


class Rectangle(base):
    """fkkfldfkdkfd;ls lkflkgdfg"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """flklkfldfd fdfsdfsd fdfd"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        def int_validator(self, key, value):
            """fdljkk jkldgjfdklgjdfgdf"""
            if not isinstance(value, int):
                raise TypeError("{} must be an integer".format(key))
            elif key== "width" or key == "height":
                if value <= 0:
                    raise ValueError("{} must be < 0".format(key))
            elif key == "x" or key == "y":
                if value < 0:
                    raise ValueError("{} must be >= 0".format(key))

        @property
        def height(self):
            """fjskjflksjdfjsdlkfj fjsdkjflkdsjs"""
            return self.__height

        @property
        def width(self):
            """fkdkf l;glf"""
            return self.__width

        @property
        def x(self):
            """kfdlk gdfgdf"""
            return self.__x

        @propert
        def y(self):
            """fkdlfk;lskfl;dks;lfdks;l"""
            return self.__y

        @height.setter
        def height(self, value):
            """fdflkd fdgdgdf"""
            if type(value) is not int:
                raise TypeError("height must be an integer")
            if value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value

        @width.setter
        def width(self, value):
            """flsdjfldsj jfdssdfds"""
            if type(value) is not int:
                raise TypeErro("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value

        @x.setter
        def x(self, value):
            """kfdkjksjdkfj fsdsd"""
            if type(value) is not int:
                raise TypeError("x must be an integer")
            if value < 0:
                raise ValueError("x must be >= 0")
            self.__x = value

        @y.setter
        def y(self, value):
            """lfdkljgkldgjlkdfjgkld"""
            if type(value) is not int:
                raise TypeError("y must be an integer")
            if value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value

        def area(self):
            """kfdjk jfgdgdf"""
            return self.__width * self.__height

        def display(self):
            """jfskjs fsdfsfs"""
            for i in range(self.__y):
                print()
            for i in range(self.__height):
                print('' * self.__x + '#' * self.__width)

        def __str__(self):
            """gjfkjgdf gfdgdfgdf"""
            return "[Rectangle] (" + str(self.id) + ") " + str(self._x) + "/" +
            str(self.__y) + " - " + str(self.__width) + "/" + str(self.__height)

        def update(self, *args, **kwargs):
            """kfjdjglkdfjgkl"""
            i = 0
            if args is not None and len(args) != 0:
                for arg in args:
                    i += 1
                    if i == 1:
                        self.id = arg
                    elif i == 2:
                        self.width = arg
                    elif i == 3:
                        self.height = arg
                    elif i == 4:
                        self.x = arg
                    elif i == 5:
                        self.y = arg
            else:
                for key, item in kwargs.items():
                    setattr(self, key, item)

        def to_dictionary(self):
            """jfdklfjklsjd kfjkldsfjkld"""
            dicts = {}
            for a in ["id", "width", "height", "x", "y"]:
                dicts[a] = getattr(self, a)
            return dicts
