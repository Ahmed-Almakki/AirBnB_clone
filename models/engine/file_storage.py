#!/usr/bin/python3
"""Script to be able to store attributes"""
import os
import json
from datetime import datetime


class FileStorage:
    """class to be able to store using it"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return the all values store in dictionary"""
        return self.__objects

    def new(self, obj):
        """ sets in  __objects the obj"""
        obj_key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__objects[obj_key] = obj

    def save(self):
        """ serializes __objects to the Json file"""
        with open(self.__file_path, 'w') as file:
            d = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(d, file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        from models.base_model import BaseModel
        from models.user import User
        from models.review import Review
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.amenity import Amenity

        class_map = {"BaseModel": BaseModel, "User": User,
                     "Place", Place, "State": State,
                     "City": City, "Amenity": Amenity,
                     "Review": Review}

        if not os.path.isfile(self.__file_path):
            return
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as file:
                json_data = json.load(file)
                for key, value in json_data.items():
                    cls = value.get("__class__")
                    cls = class_map.get(cls)
                    obj = cls(**value)
                    self.__objects[key] = obj
