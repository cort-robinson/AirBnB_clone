#!/usr/bin/python3
"""unittest for console"""
import unittest
import pep8
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime


class TestConsole(unittest.TestCase):
    """Test class for console"""

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


if __name__ == "__main__":
    unittest.main()
