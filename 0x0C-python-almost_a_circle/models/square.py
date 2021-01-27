#!/usr/bin/python3
"""fjklsjdfkjd fsdfdsf"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """fjfds fdsfsfsdfs"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """jkdjf fdsfsdfsd"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """fkjdkjfs fsdfsd"""
        return self.width

    @size.setter
    def size(self, value):
        """fsdfsdf fdfsd"""
        self.width = value
        self.height = value

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
