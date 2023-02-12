#!/usr/bin/python3
"""Unittest module for the FileStorage class."""

import unittest
from datetime import datetime
import time
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import re
import json
import os


class TestFileStorage(unittest.TestCase):
    """Test Cases for the FileStorage class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def test_5_instantiation(self):
        """Tests instantiation of storage class."""
        self.assertEqual(type(storage).__name__, "FileStorage")

    def test_3_init_no_args(self):
        """Tests __init__ with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.__init__()
        msg = "descriptor '__init__' of 'object' object needs an argument"
        self.assertEqual(str(e.exception), msg)

    def test_3_init_many_args(self):
        """Tests __init__ with many arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            b = FileStorage(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        msg = "object() takes no parameters"
        self.assertEqual(str(e.exception), msg)

    def test_5_attributes(self):
        """Tests class attributes."""
        self.resetStorage()
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))
        self.assertEqual(getattr(FileStorage, "_FileStorage__objects"), {})

    def help_test_all(self, classname):
        """Helper tests all() method for classname."""
        self.resetStorage()
        self.assertEqual(storage.all(), {})

        o = storage.classes()[classname]()
        storage.new(o)
        key = "{}.{}".format(type(o).__name__, o.id)
        self.assertTrue(key in storage.all())
        self.assertEqual(storage.all()[key], o)

    def test_5_all_base_model(self):
        """Tests all() method for BaseModel."""
        self.help_test_all("BaseModel")

    def test_5_all_user(self):
        """Tests all() method for User."""
        self.help_test_all("User")

    def test_5_all_state(self):
        """Tests all() method for State."""
        self.help_test_all("State")

    def test_5_all_city(self):
        """Tests all() method for City."""
        self.help_test_all("City")

    def test_5_all_amenity(self):
        """Tests all() method for Amenity."""
        self.help_test_all("Amenity")

    def test_5_all_place(self):
        """Tests all() method for Place."""
        self.help_test_all("Place")

    def test_5_all_review(self):
        """Tests all() method for Review."""
        self.help_test_all("Review")

    def help_test_all_multiple(self, classname):
        """Helper tests all() method with many objects for classname."""
        self.resetStorage()
        self.assertEqual(storage.all(), {})

        cls = storage.classes()[classname]
        objs = [cls() for i in range(1000)]
        [storage.new(o) for o in objs]
        self.assertEqual(len(objs), len(storage.all()))
        for o in objs:
            key = "{}.{}".format(type(o).__name__, o.id)
            self.assertTrue(key in storage.all())
            self.assertEqual(storage.all()[key], o)

    def test_5_all_multiple_base_model(self):
        """Tests all() method with many objects."""
        self.help_test_all_multiple("BaseModel")

    def test_5_all_multiple_user(self):
        """Tests all_multiple() method for User."""
        self.help_test_all_multiple("User")

    def test_5_all_multiple_state(self):
        """Tests all_multiple() method for State."""
        self.help_test_all_multiple("State")

    def test_5_all_multiple_city(self):
        """Tests all_multiple() method for City."""
        self.help_test_all_multiple("City")

    def test_5_all_multiple_amenity(self):
        """Tests all_multiple() method for Amenity."""
        self.help_test_all_multiple("Amenity")

    def test_5_all_multiple_place(self):
        """Tests all_multiple() method for Place."""
        self.help_test_all_multiple("Place")

    def test_5_all_multiple_review(self):
        """Tests all_multiple() method for Review."""
        self.help_test_all_multiple("Review")

    def test_5_all_no_args(self):
        """Tests all() with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.all()
        msg = "all() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_5_all_excess_args(self):
        """Tests all() with too many arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.all(self, 98)
        msg = "all() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msg)

    def help_test_new(self, classname):
        """Helps tests new() method for classname."""
        self.resetStorage()
        cls = storage.classes()[classname]
        o = cls()
        storage.new(o)
        key = "{}.{}".format(type(o).__name__, o.id)
        self.assertTrue(key in FileStorage._FileStorage__objects)
        self.assertEqual(FileStorage._FileStorage__objects[key], o)

    def test_5_new_base_model(self):
        """Tests new() method for BaseModel."""
        self.help_test_new("BaseModel")

    def test_5_new_user(self):
        """Tests new() method for User."""
        self.help_test_new("User")

    def test_5_new_state(self):
        """Tests new() method for State."""
        self.help_test_new("State")

    def test_5_new_city(self):
        """Tests new() method for City."""
        self.help_test_new("City")

    def test_5_new_amenity(self):
        """Tests new() method for Amenity."""
        self.help_test_new("Amenity")

    def test_5_new_place(self):
        """Tests new() method for Place."""
        self.help_test_new("Place")

    def test_5_new_review(self):
        """Tests new() method for Review."""
        self.help_test_new("Review")

    def test_5_new_no_args(self):
        """Tests new() with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            storage.new()
        msg = "new() missing 1 required positional argument: 'obj'"
        self.assertEqual(str(e.exception), msg)

    def test_5_new_excess_args(self):
        """Tests new() with too many arguments."""
        self.resetStorage()
        b = BaseModel()
        with self.assertRaises(TypeError) as e:
            storage.new(b, 98)
        msg = "new() takes 2 positional arguments but 3 were given"
        self.assertEqual(str(e.exception), msg)

    def help_test_save(self, classname):
        """Helps tests save() method for classname."""
        self.resetStorage()
        cls = storage.classes()[classname]
        o = cls()
        storage.new(o)
        key = "{}.{}".format(type(o).__name__, o.id)
        storage.save()
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        d = {key: o.to_dict()}
        with open(FileStorage._FileStorage__file_path,
                  "r", encoding="utf-8") as f:
            self.assertEqual(len(f.read()), len(json.dumps(d)))
            f.seek(0)
            self.assertEqual(json.load(f), d)

    def test_5_save_base_model(self):
        """Tests save() method for BaseModel."""
        self.help_test_save("BaseModel")

    def test_5_save_user(self):
        """Tests save() method for User."""
        self.help_test_save("User")

    def test_5_save_state(self):
        """Tests save() method for State."""
        self.help_test_save("State")

    def test_5_save_city(self):
        """Tests save() method for City."""
        self.help_test_save("City")

    def test_5_save_amenity(self):
        """Tests save() method for Amenity."""
        self.help_test_save("Amenity")

    def test_5_save_place(self):
        """Tests save() method for Place."""
        self.help_test_save("Place")

    def test_5_save_review(self):
        """Tests save() method for Review."""
        self.help_test_save("Review")

    def test_5_save_no_args(self):
        """Tests save() with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.save()
        msg = "save() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_5_save_excess_args(self):
        """Tests save() with too many arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.save(self, 98)
        msg = "save() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msg)

    def help_test_reload(self, classname):
        """Helps test reload() method for classname."""
        self.resetStorage()
        storage.reload()
        self.assertEqual(FileStorage._FileStorage__objects, {})
        cls = storage.classes()[classname]
        o = cls()
        storage.new(o)
        key = "{}.{}".format(type(o).__name__, o.id)
        storage.save()
        storage.reload()
        self.assertEqual(o.to_dict(), storage.all()[key].to_dict())

    def test_5_reload_base_model(self):
        """Tests reload() method for BaseModel."""
        self.help_test_reload("BaseModel")

    def test_5_reload_user(self):
        """Tests reload() method for User."""
        self.help_test_reload("User")

    def test_5_reload_state(self):
        """Tests reload() method for State."""
        self.help_test_reload("State")

    def test_5_reload_city(self):
        """Tests reload() method for City."""
        self.help_test_reload("City")

    def test_5_reload_amenity(self):
        """Tests reload() method for Amenity."""
        self.help_test_reload("Amenity")

    def test_5_reload_place(self):
        """Tests reload() method for Place."""
        self.help_test_reload("Place")

    def test_5_reload_review(self):
        """Tests reload() method for Review."""
        self.help_test_reload("Review")

    def help_test_reload_mismatch(self, classname):
        """Helps test reload() method for classname."""
        self.resetStorage()
        storage.reload()
        self.assertEqual(FileStorage._FileStorage__objects, {})

        cls = storage.classes()[classname]
        o = cls()
        storage.new(o)
        key = "{}.{}".format(type(o).__name__, o.id)
        storage.save()
        o.name = "Laura"
        storage.reload()
        self.assertNotEqual(o.to_dict(), storage.all()[key].to_dict())

    def test_5_reload_mismatch_base_model(self):
        """Tests reload() method mismatch for BaseModel."""
        self.help_test_reload_mismatch("BaseModel")

    def test_5_reload_mismatch_user(self):
        """Tests reload_mismatch() method for User."""
        self.help_test_reload_mismatch("User")

    def test_5_reload_mismatch_state(self):
        """Tests reload_mismatch() method for State."""
        self.help_test_reload_mismatch("State")

    def test_5_reload_mismatch_city(self):
        """Tests reload_mismatch() method for City."""
        self.help_test_reload_mismatch("City")

    def test_5_reload_mismatch_amenity(self):
        """Tests reload_mismatch() method for Amenity."""
        self.help_test_reload_mismatch("Amenity")

    def test_5_reload_mismatch_place(self):
        """Tests reload_mismatch() method for Place."""
        self.help_test_reload_mismatch("Place")

    def test_5_reload_mismatch_review(self):
        """Tests reload_mismatch() method for Review."""
        self.help_test_reload_mismatch("Review")

    def test_5_reload_no_args(self):
        """Tests reload() with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.reload()
        msg = "reload() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_5_reload_excess_args(self):
        """Tests reload() with too many arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.reload(self, 98)
        msg = "reload() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msg)


if __name__ == '__main__':
    unittest.main()
