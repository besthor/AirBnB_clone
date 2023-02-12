#!/usr/bin/python3
""" Class city that inherits from base model"""

from models.base_model import BaseModel


class City(BaseModel):
    """ Class State  that inherits from base model """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """ Constructor """
        super().__init__(self, *args, **kwargs)
