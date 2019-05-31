"""module to scrape data from weather.gc.ca page"""

from my_weather import make_soup


def sun(soup):
    """Get the sunrise and sunset values for today"""
    sun = soup.select("td")
    sunset = sun.pop()
    sunrise = sun.pop()
    return sunrise.get_text(), sunset.get_text()


def get_normals(soup):
    """Get the normal temperatures for this time of year"""
    min_max_field = soup.select("td span")
    max = min_max_field[0]
    min = min_max_field[2]
    return max.get_text().strip("."), min.get_text().strip(".")


def get_all_conditions(soup):
    """return multiple common weather conditions"""
    return soup.find_all("dd", class_="mrgn-bttm-0")


def get_current_conditions(soup):
    """Return a tuple of the current conditions
       (sky, humidity, wind_speed)"""
    find_conditions_all = get_all_conditions(soup)
    sky = find_conditions_all[2]
    humidity = find_conditions_all[10]
    wind_speed_html = find_conditions_all[11]
    wind_speed_ugly = wind_speed_html.get_text()
    wind_speed = wind_speed_ugly.strip("\n")
    return sky.get_text(), humidity.get_text(), wind_speed


def get_current_temp(soup):
    """Return the current temperature"""
    current__temp_find = soup.find_all("span", class_="wxo-metric-hide")[0]
    return current__temp_find.get_text()


def get_alerts(soup):
    """Return Weather Alerts"""
    no_alerts = soup.select("div h2")[3]
    multiple_alerts = soup.find_all("div", class_="col-xs-10 text-center")
    single_alert = soup.select("a div")[1].get_text()
    if no_alerts.get_text() == "No Alerts in effect":
        return "No Alerts in effect"
    elif len(multiple_alerts) > 3:
        alert1 = multiple_alerts.pop()
        alert2 = multiple_alerts.pop()
        return alert1.get_text(), alert2.get_text()
    else:
        return single_alert


def get_city(soup):
    """Return the city name"""
    city_find_html = soup.find_all("h1")[0]
    city_find_ugly = city_find_html.get_text()
    city_find = city_find_ugly.strip("\n")
    return city_find


def get_latest_report_date(soup):
    """return the current date and time of the latest report"""
    try:
        todays_date_in_div = soup.find_all("dd", class_="mrgn-bttm-0")[1]
    except IndexError:
        print("Invalid City Code. Get code at weather.gc.ca")
        exit(0)
    return todays_date_in_div.get_text()


def main(soup):
    """main function"""
    city_name = get_city(soup)
    alerts = get_alerts(soup)
    latest_report = get_latest_report_date(soup)
    temperature = get_current_temp(soup)
    current_conditions = get_current_conditions(soup)
    normals = get_normals(soup)
    sunrise_sunset = sun(soup)

    print("{} - {}".format(city_name, latest_report))
    if type(alerts) == str:
        print("{}".format(alerts))
    else:
        print("{}".format(alerts[0]))
        print("{}".format(alerts[1]))
    print("Temperature: {}".format(temperature))
    print("Conditions: {}".format(current_conditions[0]))
    print("Humidity: {}".format(current_conditions[1]))
    print("Wind: {}".format(current_conditions[2]))
    print("Normals: High: {}  Low: {}".format(normals[0], normals[1]))
    print("Sunrise: {}  Sunset:{}".format(sunrise_sunset[0], sunrise_sunset[1]))
