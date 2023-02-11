#!/usr/bin/python3

import unittest
from models.state import State
from models.base_model import BaseModel


class stateTest(unittest.TestCase):
    '''
    Test cases for base_model class
    '''
    def setUp(self):
        """
        simple set up
        """
        self.new_inst = State()

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
        checks if new_inst has attr 'name'
        """
        self.assertTrue(hasattr(self.new_inst, 'name'))

    def test_to_dict_on_State(self):
        """
        checks to_dict method
        """
        new_dict = self.new_inst.to_dict()
        self.assertEqual(new_dict['__class__'], 'State')
        self.assertEqual(str(type(new_dict['created_at'])), "<class 'str'>")
        self.assertEqual(str(type(new_dict['updated_at'])), "<class 'str'>")
