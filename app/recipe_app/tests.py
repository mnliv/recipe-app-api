"""
Sample tests
"""

from django.test import SimpleTestCase
from recipe_app import calc


class CalcTest(SimpleTestCase):
    """
    Test calc module
    """
    def test_add_number(self):
        """
        Test adding number together
        """
        res = calc.add(5, 6)
        self.assertEqual(res, 11)
