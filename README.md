Fun teaching myself webscraping.  Info is from weather.gc.ca

Info scraped from https://weather.gc.ca/

Install
========

This is the beginning of the my_weather app.  


Install in a virtualenv.

    pip install https://github.com/alaudet/my_weather/archive/devel.zip


Usage
=====

Find the weather code for your city by visiting  https://weather.gc.ca/

The code is in the url of your weather report.


Example 1

    my_weather on-127
    
    Timmins, ON - 7:00 AM EDT Saturday 20 April 2019
    Temperature: -3°C
    Conditions: Sunny
    Humidity: 84%
    Wind: SSE 4 km/h
    Normals: High: 10°C  Low: -3°C

Example 2

    my_weather bc-50

    Squamish, BC - 12:00 PM PDT Saturday 20 April 2019
    Temperature: 17°C
    Conditions: Not observed
    Humidity: 36%
    Wind: NW 7 km/h
    Normals: High: 11°C  Low: 2°C

Example 3

    my_weather qc-20

    Pointe-à-la-Croix, QC - 4:00 PM ADT Saturday 20 April 2019
    Temperature: 5°C
    Conditions: Not observed
    Humidity: 93%
    Wind: ENE 13 km/h
    Normals: High: 8°C  Low: -1°C


This project is for learning about webscraping only
============================

If you really need to manipulate weather data you should probably go to the Government of 
Canada Weather Website first. They make everything available for use.

http://dd.weather.gc.ca/citypage_weather/docs/README_citypage_weather.txt


Weather Canada has a fairly permissive license with a few conditions.


http://dd.weather.gc.ca/doc/LICENCE_GENERAL.txt
