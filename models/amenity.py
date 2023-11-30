#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, DateTime, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import uuid
import models
import os
from models.base_model import BaseModel, Base
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class Amenity(BaseModel):
    name = ""
