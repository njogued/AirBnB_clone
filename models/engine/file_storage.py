#!/usr/bin/python3
'''
Module contains the FileStorage class
'''
import json


class FileStorage:
    '''
    Class for json.dump and json.load
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''
        Will return _objects dictionary
        '''
        return FileStorage.__objects

    def new(self, obj):
        '''
        Sets the obj in objects
        '''
        obj_name = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[obj_name] = obj.to_dict()

    def save(self):
        '''
        Serialize the objects to JSON file (__file_path)
        '''
        with open(FileStorage.__file_path, "w") as f:
            json.dump(FileStorage.__objects, f, indent=2)

    def reload(self):
        '''
        Deserialize the JSON file to objects
        '''
        if FileStorage.__file_path:
            try:
                with open(FileStorage.__file_path) as f:
                    FileStorage.__objects = json.load(f)
            except Exception:
                pass
