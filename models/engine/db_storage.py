#!/usr/bin/python3
""""""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """"""
        user = getenv('HBNB_MYSQL_USER')
        pw = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')

        dir = "mysql+mysqldb://{}:{}@{}/{}"\
            .format(user, pw, host, db)

        self.__engine = create_engine(dir, pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

        self.__session = sessionmaker(bind=self.__engine)

    def all(self, cls=None):
        """"""
        list_class = cls
        if cls is None:
            list_class = [User, State, City, Amenity, Place, Review]

        sc = self.__session().query(list_class).all()
        dict = {}
        for element in sc:
            dict[f"{element.__class__.__name__}.{element.id}"] = element
        return dict

    def new(self, obj):
        """"""
        self.__session(bind=self.__engine.connect()).add(obj)

    def save(self):
        """"""
        self.__session(bind=self.__engine.connect()).commit()

    def delete(self, obj=None):
        """"""
        if obj is not None:
            self.__session(bind=self.__engine.connect()).delete(obj)

    def reload(self):
        """"""
        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker(bind=self.__engine)
        self.__session = scoped_session(self.__session)
