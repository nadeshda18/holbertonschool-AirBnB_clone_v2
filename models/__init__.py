#!/usr/bin/python3
""" Init module for HBNB project """
from os import getenv
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage


HBNB_TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE')

if HBNB_TYPE_STORAGE == 'db':
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()
