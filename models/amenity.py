#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class Amenity(BaseModel):
    name = ""
