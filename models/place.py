#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from sqlalchemy import Column, ForeignKey, String, Float, Integer
from sqlalchemy.orm import relationship
from sqlalchemy import Table
import models


place_amenity = Table("place_amenity", Base.metadata,
                            Column("place_id", String(60),
                            ForeignKey("places.id"),
                            primary_key=True, nullable=False),
                            Column("amenity_id", String(60),
                            ForeignKey("amenities.id"),
                            primary_key=True, nullable=False))

class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship('Review', backref='place',cascade='all, delete')
    amenities = relationship("Amenity", secondary=place_amenity, viewonly=False)

    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """"""
        super().__init__(*args, **kwargs)

    if models.storage_type != "db":
        @property
        def amenities(self):
            """"""
            amenity_list = []
            for amenity in list(models.storage.all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list
        
        @amenities.setter
        def amenities(self, value):
            """"""
            print(self.amenity_ids)
            if isinstance(value, Amenity):
                print(self.amenity_ids)
                self.amenities.append(value.id)
