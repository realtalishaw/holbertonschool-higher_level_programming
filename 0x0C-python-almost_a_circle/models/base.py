#!/usr/bin/python3
"""kdfkd gjkfdlkglkdl gfd"""
import json


class Base():
    """kfldljkgl;d kgfl;kglfkdlgk fdkgfd"""
    __nb_objects = 0

    def __init__(self, id=None):
        """gkdfljgld jgkfjkgdfg"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """kdjf sdfsfsd fdss"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """edsf fdsds fdsfds"""
        with open(cls.__name__ + ".json", "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                n_obj = [o.to_dictionary() for o in list_objs]
                f.write(cls.to_json_string(n_obj))

    @staticmethod
    def from_json_string(json_string):
        """df fds dsfsfsdsdfsfs"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """elrjkldf fdgsd fdsfsdfs"""
        if cls.__name__ == "Rectangle":
            check = cls(1, 1)
        else:
            check = clas(1)
        check.update(**dictionary)
        return check

    @classmethod
    def load_from_file(cls):
        """fsdf sfdsfsgfg dfsdfsdfs"""
        try:
            with open(cls.__name__ + ".json", "r") as f:
                json_string = f.read()
                n_list = cls.from_json_string(json_string)
                inst = []
                for i in n_list:
                    inst.append(cls.create(**d))
                return inst
        except:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """fdfs dfsf sdfd"""
        with open(cls.__name__ + '.csv', "w") as f:
            if list_objs is not None:
                list_objs = [d.to_dictionary() for d in list_objs]
                sq_list = ['id', 'size', 'x', 'y']
                rc_list = ['id', 'width', 'height', 'x', 'y']
                if cls._name_ == "Square":
                    w = csv.DictWriter(f, fieldnames=sq_list)
                else:
                    w = csv.DictWrtier(f, fieldnames=rc_list)
                w.writeheader()
                w.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """fsdfs fdsfsd fsdfsd"""
        n_list = []
        try:
            with open(cls.__name__ + '.csv', "r") as f:
                r = csv.DictReader(f)
                for obj in r:
                    for key, value in obj.items():
                        obj[key] = int(value)
                    n_list.append(obj)
            return [cls.create(**dicts) for dicts in n_list]
        except BaseException:
            return n_list
