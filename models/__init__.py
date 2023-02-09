#!/usr/bin/python3
'''
init file
'''
from .engine import file_storage
storage = file_storage.FileStorage()
storage.reload()
