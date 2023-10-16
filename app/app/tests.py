"""
Sample tests for funcs
"""

from django.test import SimpleTestCase
from app import funcs  # noqa


class CalcTests(SimpleTestCase):
    """Test the calc module."""

    def test_add_numbers(self):
        """Test adding numbers together."""
        args = {"name": "Amos",
                "email": "test@example.com"}
        res = funcs.great(name=args["name"], email=args["email"])
        self.assertEqual(res, f"Hello {args['name']}.\n"
                              f"Here is the email: {args['email']}")
