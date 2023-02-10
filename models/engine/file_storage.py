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
        FileStorage.__objects[obj_name] = obj

    def save(self):
        '''
        Serialize the objects to JSON file (__file_path)
        '''
        tcid = {}
        for key, value in FileStorage.__objects.items():
            value = value.to_dict()
            tcid[key] = value

        with open(FileStorage.__file_path, "w") as f:
            json.dump(tcid, f, sort_keys=True, indent=2)

    def reload(self):
        '''
        Deserialize the JSON file to objects
        '''
        from models.base_model import BaseModel
        all_models = {"BaseModel": BaseModel}
        if FileStorage.__file_path:
            try:
                with open(FileStorage.__file_path) as f:
                    obj_dicts = json.load(f)
                    '''empty = {}'''
                    for key, value in obj_dicts.items():
                        mod_name = all_models[value["__class__"]]
                        model = mod_name(**(obj_dicts[key]))
                        '''empty[key] = model'''
                        FileStorage.__objects[key] = model
            except FileNotFoundError:
                pass
