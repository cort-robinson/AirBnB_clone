#!/usr/bin/python3
"""unittest for model Review"""
import unittest
import pep8
from models.review import Review


class TestReview(unittest.TestCase):
    """Test class for model Review"""

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


if __name__ == "__main__":
    unittest.main()
