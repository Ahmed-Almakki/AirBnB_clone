#!/usr/bin/python3
"""this script is to creat BaseModel"""
import uuid
from datetime import datetime
from models.engine import file_storage
from  models import storage
import json


class BaseModel:
    """Partent class Model"""

    def __init__(self, *args, **kwargs):
        """init thr psrsmter"""
        if kwargs is not None and  len(kwargs) != 0:
            for ke, v in kwargs.items():
                if ke == 'created_at':
                    setattr(self, ke, datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f'))
                elif ke == 'updated_at':
                    setattr(self, ke, datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f'))
                elif ke != '__class__':
                    setattr(self, ke, v)

        else:
            self.created_at = datetime.now()
            self.id = str(uuid.uuid4())
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """updates the public instance attribute updated_at"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/value"""
        obj = self.__dict__.copy()
        obj['id'] = self.id
        obj['updated_at'] = self.updated_at.isoformat()
        obj['created_at'] = self.created_at.isoformat()
        obj['__class__'] = type(self).__name__
        return obj

    def __str__(self):
        """
        print all the attribute
        """
        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)
