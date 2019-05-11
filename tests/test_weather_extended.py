import unittest
import requests
from bs4 import BeautifulSoup
from my_weather import weather_extended

class test_weather_extended(unittest.TestCase):


    def test_extended_variables(self):
        rlist = weather_extended.extended_variables(self.soup)
        self.assertTrue(type(rlist) is list)


if __name__ == '__main__':
    unittest.main()
