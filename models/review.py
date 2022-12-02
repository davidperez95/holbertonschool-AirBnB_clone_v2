#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, Integer


class Review(BaseModel):
    """ Review classto store review information """
    __tablename__ = "reviews"
    place_id = ""
    user_id = ""
