#!/usr/bin/python
"""A class City that inherits from BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """Represents a class City
    """
    state_id = ''
    name = ''
