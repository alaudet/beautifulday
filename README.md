Purpose of Program
===========

Print out simple or extended weather reports for any Canadian city to a console.

Web scraping is not the best approach for this problem but is a good skill to have.  Using it for this will require that I update it every time Weather Canada changes the look and feel of their site.  Since this is not a skill I will use often it will force me to go back and fix it so that I can use what I have learned easily.

Info scraped from https://weather.gc.ca/


Contributing
==========

I welcome contributions from others wanting to learn about Webscraping.  Things here can always be improved.

Please do pull requests from the __devel__ branch.  Discussed proposed changes in the __Issue Tracker__ prior to sending a big pull request.

Code should follow __PEP-8__ standards as much as possible.  Also please use doctrings for all functions and classes you want to add.  It will help others that are learning as well.

Install
========

Install in a virtualenv.
    
    for the latest devel branch
    pip install https://github.com/alaudet/my_weather/archive/devel.zip

    for the latest stable master branch
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

__Example 1 - Sudbury ON, simple forecast__

    my_weather -c on-40

    Greater Sudbury, ON - 7:00 AM EDT Monday 22 April 2019
    No Alerts in effect
    Temperature: 4°C
    Conditions: Cloudy
    Humidity: 75%
    Wind: ENE 16 km/h
    Normals: High: 11°C  Low: 0°C
    Sunrise: 6:25 EDT  Sunset:20:20 EDT


__Example 2 - Timmins ON, simple forecast (includes weather alerts)__

    my_weather -c on-127

    Timmins, ON - 7:00 AM EDT Monday 22 April 2019
    FREEZING RAIN WARNING 
    RAINFALL WARNING 
    Temperature: -2°C
    Conditions: Light Freezing Rain
    Humidity: 88%
    Wind: E 13 km/h
    Normals: High: 11°C  Low: -2°C
    Sunrise: 6:23 EDT  Sunset:20:25 EDT



__Example 3 Halifax NS, extended forecast__

    my_weather -c ns-19 -e

    Halifax, NS - 8:38 AM ADT Monday 22 April 2019
    SPECIAL WEATHER STATEMENT 
    Temperature: 11°C
    Conditions: Light Rain
    Humidity: 100%
    Wind: S 9 km/h
    Normals: High: 10°C  Low: 2°C
    Sunrise: 6:19 ADT  Sunset:20:07 ADT
    ---Extended Forecast---
    Today - Periods of rain. Fog patches. Amount 10 to 20 mm. High 12. UV index 2 or low.
    Tonight - Periods of rain. Fog patches. Amount 10 to 20 mm. Low plus 5.
    Tue, 23 Apr - Rain. Fog patches. Amount 10 to 20 mm. Wind east 20 km/h gusting to 40. High 8. UV index 1 or low.
    Night - Showers. Low plus 5.
    Wed, 24 Apr - A mix of sun and cloud with 60 percent chance of showers. High 10.
    Night - Showers. Low plus 2.
    Thu, 25 Apr - Cloudy. High 8.
    Night - Cloudy periods. Low zero.
    Fri, 26 Apr - A mix of sun and cloud. High 8.
    Night - Cloudy with 60 percent chance of showers. Low plus 2.
    Sat, 27 Apr - Rain. High 7.
    Night - Cloudy periods with 60 percent chance of showers. Low plus 1.



This project is for learning about webscraping only
============================

If you really need to manipulate weather data you should probably go to the Government of Canada Weather website first. They make xml files available for use and would be a better option for building a web app.  More info at the following link.

http://dd.weather.gc.ca/citypage_weather/docs/README_citypage_weather.txt


Weather Canada has a fairly permissive license with a few conditions.


http://dd.weather.gc.ca/doc/LICENCE_GENERAL.txt
