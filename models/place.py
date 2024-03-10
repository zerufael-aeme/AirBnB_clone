#!/usr/bin/python3
"""Defines the Place module"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represent a place.
    Attributes:
        city_id: The City id.
        user_id: The User id.
        name: The name of the place.
        description: The description of the place.
        number_rooms: The number of rooms of the place.
        number_bathrooms: The number of bathrooms of the place.
        max_guest: The maximum number of guests of the place.
        price_by_night: The price by night of the place.
        latitude: The latitude of the place.
        longitude: The longitude of the place.
        amenity_ids: A list of Amenity ids.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
