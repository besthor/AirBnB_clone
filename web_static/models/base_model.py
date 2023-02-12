#!/usr/bin/python3
"""Model Base """
import uuid
import models
from datetime import datetime


class BaseModel:
    """class Base"""
    def __init__(self, *args, **kwargs):
        """ Constructor """
        if kwargs:
            # self.__dict__ = kwargs
            # self.created_at = datetime.strptime(self.created_at,
            #                                     "%Y-%m-%dT%H:%M:%S.%f")

            # self.updated_at = datetime.strptime(self.updated_at,
            #                                     "%Y-%m-%dT%H:%M:%S.%f")
            for key, value in kwargs.items():
                if key == "created_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key == "updated_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())  # unique id
            self.created_at = datetime.now()  # datetime when is created
            self.updated_at = datetime.now()  # date when is updated
            models.storage.new(self)

    def __str__(self):
        """ print() __str__ method """
        """" For pep8 validation"""
        className = self.__class__.__name__
        return "[{}] ({}) {}".format(className, self.id, self.__dict__)

    def save(self):
        """ updates with the current datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''returns a dictionary with all keys/value of the instance'''
        dict_copy = self.__dict__.copy()
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        dict_copy['__class__'] = self.__class__.__name__
        return dict_copy

    # @property
    # def id(self):
    #     return self.id
