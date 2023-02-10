#!/usr/bin/python3
'''
Base model for HBNB project
'''
from models import storage
from dateutil import parser
from datetime import datetime
import json
from uuid import uuid4


class BaseModel():
    '''
    Methods: save, to_dict, __str__, __init__
    Attributes: id, created_at, updated_at
    '''
    def __init__(self, *args, **kwargs):
        '''
        id - Unique ID
        created_at - Time when object is instantiated
        updated_at - Defaults to created_at when an object is instantiated
        '''
        if kwargs:
            del kwargs["__class__"]
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = parser.parse(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
            '''
            strftime("%A %d %B %Y at %H:%M:%S")
            '''

    def __str__(self):
        '''
        return a string representation of the class
        '''
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        '''
        Update the updated_at instance attribute
        '''
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        '''
        returns a dict of key/value pairs of the instance
        '''
        dict_rep = self.__dict__.copy()
        dict_rep.update({"__class__": self.__class__.__name__})
        dict_rep.update({"created_at": self.created_at.isoformat()})
        dict_rep.update({"updated_at": self.updated_at.isoformat()})
        return dict_rep
