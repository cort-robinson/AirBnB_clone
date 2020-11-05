#!/usr/bin/python3
"""unittest for model Place"""
import unittest
import pep8
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test class for model Place"""

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


if __name__ == "__main__":
    unittest.main()
