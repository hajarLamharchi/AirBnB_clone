#!/usr/bin/python3
"""  Define class  Place that inherit from BaseModel """
from models.base_model import BaseModel


class Place(BaseModel):
    """
        This class defines a Place
        Attributes:
            city_id(string): city Id
            user_id(string): User ID
            name(string): Place name
            description(string): Place description
            number_rooms(int): place room nbr
            number_bathrooms(int): place bathroom nbr
            max_guest(int): max guest of plce
            price_by_night(int): price by night of place
            latitude(float): place coordinate
            longitude(float): place coordinate
            amenity_ids(list of string): list of amenity ids
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
