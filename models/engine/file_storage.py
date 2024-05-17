#!/usr/bin/python3
"""Script to be able to store attributes"""
import os
import json


class FileStorage:
    """class to be able to store using it"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return the all values store in dictionary"""
        return self.__objects

    def new(self, obj):
        """ sets in  __objects the obj"""
        id_value = obj.id
        obj_key = '{}.{}'.format(obj.__class__.__name__, id_value)
        self.__objects[obj_key] = obj

    def save(self):
        """ serializes __objects to the Json file"""
        with open(FileStorage.__file_path, 'w') as file:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, 'r') as file:
            json_data = json.load(file)
