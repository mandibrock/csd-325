# ----------------------------------------------
# Author: Amanda Brock
# Date: February 22, 2026
# Assignment: Module 7.2
# Purpose of Code: tests the function in city_functions.py
# ----------------------------------------------

import unittest
from city_functions import city_country


class CityCountryTestCase(unittest.TestCase):
    def test_city_country(self):
        formatted = city_country("santiago", "chile")
        self.assertEqual(formatted, "Santiago, Chile")


if __name__ == "__main__":
    unittest.main()