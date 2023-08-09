#!/usr/bin/python3
"""  Define class Amenity that inherit from BaseModel """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
        This class defines a Amenity
        Attributes:
            name(string): amenity name
    """
    name = ""
