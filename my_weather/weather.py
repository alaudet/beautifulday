#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup

page = requests.get('https://weather.gc.ca/city/pages/on-127_metric_e.html')
soup = BeautifulSoup(page.content, 'html.parser')


def get_all_conditions():
    '''return multiple common weather conditions'''
    return soup.find_all('dd', class_='mrgn-bttm-0')


def get_wind_speed():
    '''Return the current wind speed and direction'''
    find_conditions_all = get_all_conditions()
    wind_speed_html = find_conditions_all[11]
    wind_speed_ugly = wind_speed_html.get_text()
    # Next line is needed as there are newlines in the string
    # that need to be removed.
    wind_speed = wind_speed_ugly.strip('\n')
    return wind_speed


def get_humidity():
    '''Return the current atmospheric humidity'''
    find_conditions_all = get_all_conditions()
    humidity = find_conditions_all[10]
    return humidity.get_text()


def get_current_conditions():
    '''Return the current conditions'''
    find_conditions_all = get_all_conditions()
    conditions = find_conditions_all[2]
    return conditions.get_text()


def get_current_temp():
    '''Return the current temperature'''
    current__temp_find = soup.find_all('span', class_='wxo-metric-hide')[0]
    return current__temp_find.get_text()


def get_city():
    '''Return the city name'''
    city_find = soup.find_all('h1')[0]
    return city_find.get_text()


def get_latest_report_date():
    '''return the current date and time of the latest report'''
    todays_date_in_div = soup.find_all('dd', class_='mrgn-bttm-0')[1]
    return todays_date_in_div.get_text()


def main():
    '''main function'''
    city_name = get_city()
    latest_report = get_latest_report_date()
    temperature = get_current_temp()
    current_conditions = get_current_conditions()
    humidity = get_humidity()
    wind_speed = get_wind_speed()

    print('{}{}'.format(city_name, latest_report))
    print('Current Temperature: {}'.format(temperature))
    print('Current Conditions: {}'.format(current_conditions))
    print('Humidity: {}'.format(humidity))
    print('Wind: {}'.format(wind_speed))


main()
