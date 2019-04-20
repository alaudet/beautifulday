'''Pull data from website and extract the html'''

import requests
from bs4 import BeautifulSoup

code = 'on-127'
url = 'https://weather.gc.ca/city/pages/{}_metric_e.html'.format(code)


def make_soup():
    page = requests.get(url)
    return BeautifulSoup(page.content, 'html.parser')
    print(page.content)
