Fun teaching myself webscraping.  Info is from weather.gc.ca

Currently provides the following output
=====================

Scraped from https://weather.gc.ca/city/pages/on-127_metric_e.html

    Timmins, ON - 7:00 AM EDT Saturday 20 April 2019
    Temperature: -3°C
    Conditions: Sunny
    Humidity: 84%
    Wind: SSE 4 km/h
    Normals: High: 10°C  Low: -3°C


Install
========

This is the beginning of the my_weather app.  Currently hardcoded to on-127 (Timmins) in my_weather/make_soup.py


Install in a virtualenv.

    pip install https://github.com/alaudet/my_weather/archive/devel.zip


To run

    my_weather


This project is for learning about webscraping only
============================

If you really need to manipulate weather data you should probably go to the Government of 
Canada Weather Website first. They make everything available for use.

http://dd.weather.gc.ca/citypage_weather/docs/README_citypage_weather.txt


Weather Canada has a fairly permissive license with a few conditions.


http://dd.weather.gc.ca/doc/LICENCE_GENERAL.txt
