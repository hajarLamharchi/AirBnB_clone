#!/usr/bin/python3
"""  Define class City  that inherit from BaseModel """
from models.base_model import BaseModel


class City(BaseModel):
    """
    This class defines a City
    Attributes:
        state_id(string): state Id
        name(string): city name
    """
    state_id = ""
    name = ""
