#!/usr/bin/python3
'''Module for the review class'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''The Review Class'''
    place_id = ""
    user_id = ""
    text = ""
