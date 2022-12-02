#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")

    def __init__(self, *args, **kwargs):
        """"""
        super().__init__(*args, **kwargs)

    storage_type = getenv("HBNB_TYPE_STORAGE")
    if storage_type != "db":
        @property
        def cities(self):
            """Getter for the cities"""
            city_list = []
            all_cities = models.storage.all(City)
            for value in all_cities.values():
                if value.state_id == self.id:
                    city_list.append(value)
            return city_list
