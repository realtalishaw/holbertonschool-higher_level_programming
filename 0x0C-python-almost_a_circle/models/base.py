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
        """kflk lgkfdl kgldf"""
        if list_dictionaries is None:
            return '[]'
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """fmlflkjd lfjlkgjldflg """
        if list_objs is None:
            json_string = "[]"
        else:
            json_string = cls.to_json_string([obj.to_dictionary() for objs in
                                              list_objs])
        with open(cls.__name__ + '.json', mode='w+', encoding='utf-8') as a_file:
            a_file.write(json_string)

    def from_json_string(json_string):
        """fkdl klfdjgldf ;gd"""
        if json_string is None or len(json_string) == 0:
            return '[]'
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """jfdkljflk djflkjdkljglkdjg"""
        data = class(3, 3, 3)
        data.update(**dictionary)
        return data
