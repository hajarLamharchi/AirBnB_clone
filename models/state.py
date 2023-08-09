#!/usr/bin/python3
"""  Define class  State that inherit from BaseModel """
from models.base_model import BaseModel


class State(BaseModel):
    """
    This class define a State
    Attributes:
        name(string): state name
    """
    name = ""
