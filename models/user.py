#!/usr/bin/python3
'''
Module with a class User that inherits from the BaseModel
'''
from models.base_model import BaseModel


class User(BaseModel):
    '''class User that inherits from the BaseModel'''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
