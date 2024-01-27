import unittest
from project import get_exchange_rate, convert_currency

class TestProjectFunctions(unittest.TestCase):

    def test_get_exchange_rate(self):
        # Your test cases for get_exchange_rate function
        self.assertEqual(get_exchange_rate("USD", "EUR"), expected_result)

    def test_convert_currency(self):
        # Your test cases for convert_currency function
        self.assertEqual(convert_currency("USD", "EUR", 100), expected_result)

if __name__ == '__main__':
    unittest.main()
