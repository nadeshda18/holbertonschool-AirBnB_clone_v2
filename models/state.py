#!/usr/bin/python3
""" State module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class State(BaseModel, Base):
    """ The state class, contains state name """
    __tablename__ = 'states'

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', back_populates='state', cascade='all, delete-orphan')
    else:
        name = ""

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """ Getter attribute that returns the list of City instances
            with state_id equals to the current State.id """
            from models import storage
            city_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
