import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_ord_list(self):
        """Test an ordered list of integers."""
        result = max_integer([2, 4, 7])
        self.assertEqual(result, 7)

    def test_unord_list(self):
        """Test UN ordered list of integers."""
        result = max_integer([2, 9, 4, 7])
        self.assertEqual(result, 9)

    def test_max_beg(self):
        """Test UN ordered list of integers."""
        result = max_integer([10, 2, 9, 4, 7])
        self.assertEqual(result, 10)

    def test_empty_list(self):
        """Test empty list of integers."""
        result = max_integer([])
        self.assertEqual(result, None)

    def test_one_elem(self):
        """Test one element list of integers."""
        result = max_integer([7])
        self.assertEqual(result, 7)

    def test_float(self):
        """Test list of floats."""
        result = max_integer([1.1, 1.7, 5.7, 9.1])
        self.assertEqual(result, 9.1)

    def test_string(self):
        """Test string."""
        result = max_integer('doaa')
        self.assertEqual(result, 'o')

    def test_list_string(self):
        """Test list of string."""
        result = max_integer(['doaa', 'abd', 'elfattah'])
        self.assertEqual(result, 'elfattah')

    def test_empty_string(self):
        """Test Empty string"""
        result = max_integer("")
        self.assertEqual(result, None)
