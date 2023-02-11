#!/usr/bin/python3

import unittest
from models.city import City
from models.base_model import BaseModel


class cityTest(unittest.TestCase):
    '''
    Test cases for base_model class
    '''
    def setUp(self):
        """
        simple set up
        """
        self.new_inst = City()

    def tearDown(self):
        """
        tear down method
        """
        del self.new_inst

    def test_is_basemodel_inst(self):
        """
        tests if new_inst is an instance of BaseModel
        """
        self.assertIsInstance(self.new_inst, BaseModel)

    def test_if_name_exists(self):
        """
        test if attribute 'name' is present in instance of city
        """
        self.assertTrue(hasattr(self.new_inst, 'name'))
        self.assertTrue(hasattr(self.new_inst, 'state_id'))

    def test_value_attributes(self):
        """
        checks value of City attributes
        """
        self.assertEqual(self.new_inst.name, "")
        self.assertEqual(self.new_inst.state_id, "")

    def test_to_dict_on_Amenity(self):
        """
        checks __class__ key in to_dict instance
        """
        new_dict = self.new_inst.to_dict()
        self.assertEqual(new_dict['__class__'], 'City')
        self.assertEqual(str(type(new_dict['created_at'])), "<class 'str'>")
        self.assertEqual(str(type(new_dict['updated_at'])), "<class 'str'>")
