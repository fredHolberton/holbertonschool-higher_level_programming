"""Module to test the task 5. Max integer - Unittest"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_at_the_end(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_max_at_the_beginning(self):
        self.assertEqual(max_integer([3, 1, 2]), 3)

    def test_max_in_the_middle(self):
        self.assertEqual(max_integer([2, 3, 1]), 3)

    def test_one_negative_number(self):
        self.assertEqual(max_integer([-1, 2, 3]), 3)
        
    def test_only_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_list_of_one_element(self):
        self.assertEqual(max_integer([3]), 3)

    def test_list_is_empty(self):
        self.assertEqual(max_integer(), None)
