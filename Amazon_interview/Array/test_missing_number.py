import unittest
import array_missing_number


class TestNumber(unittest.TestCase):

    def test_first(self):
        result = array_missing_number.missing_number([1,2,3,5,6])
        self.assertEqual(result,4)


