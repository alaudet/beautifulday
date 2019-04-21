#!/usr/bin/env python

import sys
import argparse
from my_weather import weather, weather_extended


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
    if len(sys.argv) == 3:
        weather.main(code)
    elif code and extended:
        weather.main(code)
        weather_extended.main(code)
    else:
        print('something went wrong, check your arguments')
