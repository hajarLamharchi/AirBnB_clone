#!/usr/bin/python3
"""  Define class Review that inherit from BaseModel """
from models.base_model import BaseModel


class Review(BaseModel):
    """
        This class defines a Review
        Attributes:
            place_id(string): place Id
            user_id(string): User Id
            text(string): review text
    """
    place_id = ""
    user_id = ""
    text = ""
