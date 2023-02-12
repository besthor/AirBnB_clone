#!/usr/bin/python3
""" Class user that inherits from base model"""

from models.base_model import BaseModel


class User(BaseModel):
    """ Class user that inherits from base model """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    # def __init__(self, *args, **kwargs):
    #     """ Constructor """
    #     super().__init__(self, *args, **kwargs)
