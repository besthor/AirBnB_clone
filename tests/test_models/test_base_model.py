#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
import datetime


class TestBaseModel(unittest.TestCase):
    '''
    Test cases for base_model class
    '''

    def setUp(self):
        '''
        simple set up
        '''
        self.new_instance = BaseModel()

    def tearDown(self):
        '''
        tear down method
        '''
        del self.new_instance

    def test_id_is_string(self):
        '''
        testing to verify id is a string
        '''
        self.assertEqual(str(type(self.new_instance.id)), "<class 'str'>")

    def test_created_at_is_datetimeobj(self):
        '''
        tests if created_at is a datetime object
        '''
        self.assertEqual(str(type(self.new_instance.created_at)),
                         "<class 'datetime.datetime'>")

    def test_updated_at_is_datetimeobj(self):
        '''
        tests if updated_at is a datetime object
        '''
        self.assertEqual(str(type(self.new_instance.updated_at)),
                         "<class 'datetime.datetime'>")

    def test_to_dict_type(self):
        '''
        test type of to_dict method
        '''
        basemodel_dict = self.new_instance.to_dict()
        self.assertEqual(str(type(basemodel_dict)), "<class 'dict'>")

    def test_to_dict_created_at(self):
        '''
        test to_dict created_at type
        '''
        new_dict = self.new_instance.to_dict()
        self.assertEqual(str(type(new_dict["created_at"])), "<class 'str'>")

    def test_to_dict_updated_at(self):
        '''
        test to_dict updated_at type
        '''
        new_dict = self.new_instance.to_dict()
        self.assertEqual(str(type(new_dict["updated_at"])), "<class 'str'>")

    def test_to_dict_classKey(self):
        '''
        checks if key class exists in the dict
        '''
        new_dict = self.new_instance.to_dict()
        self.assertEqual(new_dict["__class__"], "BaseModel")

    def test_save(self):
        '''
        tests created_at and updated_at values after call to save
        '''
        first_dict = self.new_instance.to_dict()
        self.new_instance.save()
        second_dict = self.new_instance.to_dict()
        self.assertEqual(first_dict["created_at"], second_dict["created_at"])
        self.assertNotEqual(
            first_dict["updated_at"], second_dict["updated_at"])

    def test_kwargs_id(self):
        '''
        tests if id stays the same during serialization - deserialization
        process
        '''
        first_inst = self.new_instance
        new_dict = first_inst.to_dict()
        second_inst = BaseModel(**new_dict)
        self.assertEqual(first_inst.id, second_inst.id)

    def test_args(self):
        '''
        tests args
        '''
        new_instance = self.new_instance
        new_instance.name = "Holberton"
        self.assertEqual(new_instance.name, "Holberton")
