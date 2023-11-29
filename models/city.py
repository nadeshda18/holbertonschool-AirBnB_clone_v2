#!/usr/bin/python3
""" City module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os
from models.state import State

class City(BaseModel, Base):
    """ The city class, contains state ID and links to state """
    __tablename__ = 'cities'

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        state = relationship('State', back_populates='cities')
    else:
        name = ""

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def state(self):
            """ Getter attribute that returns the state """
            from models import storage
            return storage.all(State).get(self.state_id)
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
