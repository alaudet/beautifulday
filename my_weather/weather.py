'''module to scrape data from weather.gc.ca page'''

from my_weather import make_soup


def get_normals(soup):
    '''Get the normal temperatures for this time of year'''
    min_max_field = soup.select('td span')
    max = min_max_field[0]
    min = min_max_field[2]
    return max.get_text().strip('.'), min.get_text().strip('.')


def get_all_conditions(soup):
    '''return multiple common weather conditions'''
    return soup.find_all('dd', class_='mrgn-bttm-0')


def get_current_conditions(soup):
    '''Return a tuple of the current conditions
       (sky, humidity, wind_speed)'''
    find_conditions_all = get_all_conditions(soup)
    sky = find_conditions_all[2]
    humidity = find_conditions_all[10]
    wind_speed_html = find_conditions_all[11]
    wind_speed_ugly = wind_speed_html.get_text()
    wind_speed = wind_speed_ugly.strip('\n')
    return sky.get_text(), humidity.get_text(), wind_speed


def get_current_temp(soup):
    '''Return the current temperature'''
    current__temp_find = soup.find_all('span', class_='wxo-metric-hide')[0]
    return current__temp_find.get_text()


def get_city(soup):
    '''Return the city name'''
    city_find_html = soup.find_all('h1')[0]
    city_find_ugly = city_find_html.get_text()
    city_find = city_find_ugly.strip('\n')
    return city_find


def get_latest_report_date(soup):
    '''return the current date and time of the latest report'''
    try:
        todays_date_in_div = soup.find_all('dd', class_='mrgn-bttm-0')[1]
    except IndexError:
        print('Invalid City Code. Get code at weather.gc.ca')
        exit(0)
    return todays_date_in_div.get_text()


def main(soup):
    '''main function'''
    city_name = get_city(soup)
    latest_report = get_latest_report_date(soup)
    temperature = get_current_temp(soup)
    current_conditions = get_current_conditions(soup)
    normals = get_normals(soup)

    print('{} - {}'.format(city_name, latest_report))
    print('Temperature: {}'.format(temperature))
    print('Conditions: {}'.format(current_conditions[0]))
    print('Humidity: {}'.format(current_conditions[1]))
    print('Wind: {}'.format(current_conditions[2]))
    print('Normals: High: {}  Low: {}'.format(normals[0], normals[1]))
