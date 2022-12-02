#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from models.user import User
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
import models


class User(BaseModel, Base if (getenv('HBNB_TYPE_STORAGE') == "db")
           else object):
    """This module defines a class User"""
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)

    def __init__(self, *args, **kwargs):
        """"""
        super().__init__(*args, **kwargs)

    storage_type = getenv("HBNB_TYPE_STORAGE")
    if storage_type != "db":
        @property
        def users(self):
            """Getter for the users"""
            user_list = []
            all_users = models.storage.all(User)
            for value in all_users.values():
                if value.state_id == self.id:
                    user_list.append(value)
            return user_list
