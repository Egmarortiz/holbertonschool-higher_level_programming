#!/usr/bin/python3

"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_empty_list(self):
        """Empty list should return None."""
        self.assertIsNone(max_integer([]))

    def test_no_args(self):
        """No argument should use default and return None."""
        self.assertIsNone(max_integer())

    def test_single_element(self):
        """List with one element returns that element."""
        self.assertEqual(max_integer([7]), 7)

    def test_sorted_list(self):
        """List already sorted ascending."""
        data = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer(data), 5)

    def test_max_at_start(self):
        """Maximum at beginning of list."""
        data = [10, 3, 2, 1]
        self.assertEqual(max_integer(data), 10)

    def test_unsorted_list(self):
        """Unsorted list with negative and positive integers."""
        data = [3, 1, -2, 8, 0]
        self.assertEqual(max_integer(data), 8)

    def test_all_negative(self):
        """All negative integers."""
        self.assertEqual(max_integer([-5, -1, -7, -3]), -1)

    def test_floats(self):
        """List of floats."""
        data = [2.5, 3.1, -1.2, 3.1]
        self.assertAlmostEqual(max_integer(data), 3.1)

    def test_mixed_ints_floats(self):
        """Mixed integers and floats."""
        data = [1, 2.2, 3, 2.9]
        self.assertEqual(max_integer(data), 3)

    def test_list_argument_type_error(self):
        """Passing None instead of list should raise TypeError."""
        with self.assertRaises(TypeError):
            max_integer(None)


if __name__ == '__main__':
    unittest.main()

