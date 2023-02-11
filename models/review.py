#!/usr/bin/python
"""A class review that inherits from BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a class Review
    """
    place_id = ''
    user_id = ''
    text = ''
