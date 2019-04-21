#!/usr/bin/env python

import sys
import argparse
from my_weather import make_soup, weather, weather_extended


def get_args():
    '''Parse command line arguments.'''

    parser = argparse.ArgumentParser(
        description='Use argparsing to allow more control over output')

    parser.add_argument('-c',
                        '--code',
                        type=str,
                        help='Enter the city code from weather.gc.ca',
                        required=True
                        )

    parser.add_argument('-e',
                        '--extended',
                        help='Add the extended forecast',
                        action='store_true',
                        )

    args = parser.parse_args()
    code = args.code
    extended = args.extended
    return code, extended


def main():
    '''Main function'''
    code, extended = get_args()
    soup = make_soup.make_soup(code)
    if len(sys.argv) == 3:
        weather.main(soup)
    elif code and extended:
        weather.main(soup)
        weather_extended.main(soup)
