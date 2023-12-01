#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from models.place import Place, place_amenity
from os import getenv


class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        place_amenities = relationship("Place", secondary="place_amenity",
                                       back_populates="amenities")
