#!/usr/bin/python3
"""
    Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_default_list(self):
        self.assertEqual(max_integer(), None)

    def test_max_list_first(self):
        lst = [69, 5, 3, 44]
        self.assertEqual(max_integer(lst), 69)

    def test_max_list_last(self):
        lst = [0, 1, 3, 69]
        self.assertEqual(max_integer(lst), 69)

    def test_max_mixed_list(self):
        lst = [-1, -4, 0, 4, -6]
        self.assertEqual(max_integer(lst), 4)

    def test_max_list_with_string(self):
        lst = ['issam', 5, 6, 9]
        with self.assertRaises(TypeError):
            max_integer(lst)
    def test_max_int_neg(self):
        """ tests if list has a negative int
        """
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
    def test_negative(self):
        l = [-2, -6, -1]
        result = max_integer(l)
        self.assertEqual(result, -1)

    def test_maximum_integer(self):
        self.assertEqual(max_integer([-1, -9, -2]), -1)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))




if __name__ == "__main__":
    unittest.main()
