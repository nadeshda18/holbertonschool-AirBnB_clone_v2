#!/usr/bin/python3
"""This module defines the DBStorage class for AirBnB"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User


classes = {"State": State, "City": City, "User": User,
           "Place": Place, "Review": Review, "Amenity": Amenity}


class DBStorage:
    """This class manages storage of AirBnB models in a database"""
    __engine = None
    __session = None

    def __init__(self):
        """Creates the engine"""
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(user, pwd, host, db),
                                      pool_pre_ping=True)

        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        storage_dict = {}
        if cls is None:
            for value in classes.values():
                for obj in self.__session.query(value):
                    key = obj.__class__.__name__ + "." + obj.id
                    storage_dict[key] = obj
        if cls in classes:
            for obj in self.__session.query(classes[cls]):
                key = obj.__class__.__name__ + "." + obj.id
                storage_dict[key] = obj
        return storage_dict

    def new(self, obj):
        """Adds the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes obj from the current database session if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the database and the current database
        session from the engine (optionally drop all tables)"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def get(self, cls, id):
        """Get a specific object of a certain class with a specific id"""
        if cls not in classes.values():
            return None
        objs = self.__session.query(cls).filter(cls.id == id).first()
        return objs

    def close(self):
        """Close the session"""
        self.__session.close()
