#!/usr/bin/python3
""" User Module for HBNB project """
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """ User class """
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship('Place', cascade='all, delete', backref='user')
