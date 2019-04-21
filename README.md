Fun teaching myself webscraping.  Info is from weather.gc.ca

Info scraped from https://weather.gc.ca/

Install
========

This is the beginning of the my_weather app.  


Install in a virtualenv.
    
    for devel branch
    pip install https://github.com/alaudet/my_weather/archive/devel.zip

    for master branch
    pip install https://github.com/alaudet/my_weather/archive/master.zip


Usage
=====

Find the weather code for your city by visiting  https://weather.gc.ca/

The code is in the url of your weather report.

__help menu__

    my_weather -h
    usage: my_weather [-h] -c CODE [-e]

    Use argparsing to allow more control over output

    optional arguments:
    -h, --help            show this help message and exit
    -c CODE, --code CODE  Enter the city code from weather.gc.ca
    -e, --extended        Add the extended forecast

__Example 1__

my_weather -c on-127

    Timmins, ON - 9:00 PM EDT Saturday 20 April 2019
    Temperature: 5°C
    Conditions: Mainly Clear
    Humidity: 47%
    Wind: calm
    Normals: High: 10°C  Low: -3°C


__Example 2__

my_weather c- on-143 -e

    Toronto, ON - 9:42 PM EDT Saturday 20 April 2019
    Temperature: 7°C
    Conditions: Cloudy
    Humidity: 91%
    Wind: SSE 10 km/h
    Normals: High: 13°C  Low: 4°C
    ---Extended Forecast---
    Tonight - Periods of rain or drizzle ending late this evening then cloudy with 60 percent chance of drizzle. Risk of a thunderstorm early this evening. Fog patches developing late this evening. Wind northeast 20 km/h becoming light this evening. Low 6.
    Sun, 21 Apr - Mainly cloudy. 40 percent chance of drizzle in the morning and early in the afternoon. Fog patches dissipating in the morning. High 16 except 11 near Lake Ontario. UV index 5 or moderate.
     Night - Partly cloudy. Low 6.
    Mon, 22 Apr - A mix of sun and cloud with 40 percent chance of showers. High 16.
     Night - Cloudy periods with 40 percent chance of showers. Low 9.
    Tue, 23 Apr - Cloudy with 40 percent chance of showers. High 16.
     Night - Cloudy with 60 percent chance of showers. Low 7.
    Wed, 24 Apr - Cloudy with 30 percent chance of showers. High 12.
     Night - Clear. Low plus 4.
    Thu, 25 Apr - Sunny. High 16.
     Night - Cloudy periods. Low 7.
    Fri, 26 Apr - Cloudy with 40 percent chance of showers. High 13.


This project is for learning about webscraping only
============================

If you really need to manipulate weather data you should probably go to the Government of 
Canada Weather Website first. They make everything available for use.

http://dd.weather.gc.ca/citypage_weather/docs/README_citypage_weather.txt


Weather Canada has a fairly permissive license with a few conditions.


http://dd.weather.gc.ca/doc/LICENCE_GENERAL.txt
