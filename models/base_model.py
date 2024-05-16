#!/usr/bin/env bash
"""this script is to creat BaseModel"""
import uuid
from datetime import datetime


class BaseModel:
    """Partent class Model"""

    def __init__(self):
        """init thr psrsmter"""
        self.updated_at = datetime.now()
        self.created_at = datetime.now()
        self.id = str(uuid.uuid4())

    def save(self):
        """updates the public instance attribute updated_at"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all keys/value"""
        my_obj = self.__dict__.copy()
        my_obj['id'] = self.id
        my_obj['updated_at'] = self.updated_at.isoformat()
        my_obj['created_at'] = self.created_at.isoformat()
        my_obj['__class__'] = type(self).__name__
        return my_obj

    def __str__(self):
        """
        print all the attribute
        """
        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)
