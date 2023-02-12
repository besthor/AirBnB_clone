#!/usr/bin/python3
""" Class review that inherits from base model"""

from models.base_model import BaseModel


class Review(BaseModel):
    """ Class Review that inherits from base model """
    place_id = ""  # it will be the Place.id
    user_id = ""  # it will be the User.id
    text = ""

    def __init__(self, *args, **kwargs):
        """ Constructor """
        super().__init__(self, *args, **kwargs)
