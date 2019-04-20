'''Pull data from website and extract the html'''

import requests
from bs4 import BeautifulSoup


def make_soup(code):
    city_code = code
    page = requests.get('https://weather.gc.ca/city/pages/{}_metric_e.html'.format(city_code))
    return BeautifulSoup(page.content, 'html.parser')
