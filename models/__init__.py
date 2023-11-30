#!/usr/bin/python3
""" Init module for HBNB project """
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
