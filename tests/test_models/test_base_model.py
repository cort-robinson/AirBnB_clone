#!/usr/bin/python3
"""unittest for class BaseModel"""
import unittest
import pep8
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test class for class BaseModel"""

    def test_types(self):
        """Test for BaseModel types"""
        self.test1 = BaseModel()
        self.test2 = BaseModel()
        self.assertEqual(BaseModel, type(BaseModel()))
        self.assertEqual(str, type(self.test1.id))
        self.assertEqual(str, type(self.test2.id))
        self.assertEqual(datetime, type(self.test1.created_at))
        self.assertEqual(datetime, type(self.test2.created_at))
        self.assertEqual(datetime, type(self.test1.updated_at))
        self.assertEqual(datetime, type(self.test2.updated_at))

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def TestModels(self):
        """Test model name"""
        self.my_model.name = 'Holberton'
        self.assertEqual(self.my_model.name, 'Holberton')
        """Test model numbers"""
        self.my_model.my_number = 55
        self.assertEqual(self.my_model.my_number, 55)
        """Test model exist"""
        self.assertTrue(path.isfile('my_file.json'))
        """Test model to dict"""
        model = self.my_model.to_dict()
        self.assertIsInstance(model["created_at"], str)
        self.assertIsInstance(model["updated_at"], str)
        self.assertIsInstance(model["my_number"], int)
        self.assertIsInstance(model["id"], str)

if __name__ == "__main__":
    unittest.main()
