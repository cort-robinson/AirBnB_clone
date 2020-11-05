#!/usr/bin/python3
"""unittest for class FileStorage"""
import unittest
import pep8
import os

from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
import models

class TestFileStorage(unittest.TestCase):
    """Test class for class FileStorage"""

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_file_objects(self):
        """tests for __objects functionality"""
        self.storage = FileStorage()
        self.storage.save()
        obj = self.storage.all()
        self.assertIs(obj, self.storage._FileStorage__objects)

    def test_all(self):
        """testing the all module"""
        self.storage = FileStorage()
        self.storage.save()
        obj = self.storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, self.storage._FileStorage__objects)
        self.assertEqual(dict, type(self.storage.all()))

    def test_saves_new_instance(self):
        """Tests if file is being created """
        b1 = BaseModel()
        models.storage.new(b1)
        models.storage.save()
        file_exist = os.path.exists(os.path.isfile("./file.json"))
        self.assertTrue(file_exist)

if __name__ == "__main__":
    unittest.main()
