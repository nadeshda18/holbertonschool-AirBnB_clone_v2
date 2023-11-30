#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv

class Amenity(BaseModel):
    """This class defines a Amenity class for AirBnB"""
    name = ""
