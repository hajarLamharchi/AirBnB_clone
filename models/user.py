#!/usr/bin/python3
"""  Define class  that inherit from BaseModel """
from models.base_model import BaseModel


class User(BaseModel):
    """
        This class defines a user
        Attributes:
            email(string): user email
            password(string): user password
            first_name(string): user first name
            last_name(string): user last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
