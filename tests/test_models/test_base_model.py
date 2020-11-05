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

    def test_to_dict(self):
        """testing to dict"""
        model = BaseModel()
        model.name = "reese"
        model.my_number = 55
        model_types_json = {
            "my_number": int,
            "name": str,
            "__class__": str,
            "id": str,
            "created_at": str
        }
        model_json = model.to_dict()
        for k, v in model_types_json.items():
            with self.subTest(k=k, v=v):
                self.assertIn(k, model_json)
                self.assertIs(type(model_json[k]), v)

    def test_file_save(self):
        """Test that info is saved to file"""
        b3 = BaseModel()
        b3.save()
        with open("file.json", 'r') as f:
            self.assertIn(b3.id, f.read())

if __name__ == "__main__":
    unittest.main()
