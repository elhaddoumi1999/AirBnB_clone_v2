#!/usr/bin/python3
"""
BaseModel class defines a base model with common
attributes and methodsfor other classes.
"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        self.__dict__[key] = datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f")
                    else:
                        self.__dict__[key] = value
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__

        if isinstance(obj_dict['created_at'], datetime):
            obj_dict['created_at'] = obj_dict['created_at'].isoformat()
        if isinstance(obj_dict['updated_at'], datetime):
            obj_dict['updated_at'] = obj_dict['updated_at'].isoformat()

        return obj_dict
