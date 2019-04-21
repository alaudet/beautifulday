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

__Example 1 - Timmins ON, simple forecast__

    my_weather -c on-127

    Timmins, ON - 9:00 PM EDT Saturday 20 April 2019
    Temperature: 5°C
    Conditions: Mainly Clear
    Humidity: 47%
    Wind: calm
    Normals: High: 10°C  Low: -3°C


__Example 2 Halifax NS, extended forecast__

    my_weather -c ns-19 -e

    Halifax, NS - 8:00 AM ADT Sunday 21 April 2019
    Temperature: 12°C
    Conditions: Light Drizzle
    Humidity: 100%
    Wind: SSW 27  gust 48 km/h
    Normals: High: 10°C  Low: 1°C
    ---Extended Forecast---
    Today - Cloudy. 30 percent chance of drizzle early this morning. Showers or drizzle beginning this morning. Fog patches. Amount 2 mm. Wind south 20 km/h gusting to 40. High 16 except 9 along parts of the coast. UV index 3 or moderate.
    Tonight - Showers or drizzle. Fog patches. Amount 2 mm. Wind south 20 km/h gusting to 40. Low 9.
    Mon, 22 Apr - Periods of rain. Fog patches. Amount 10 to 15 mm. Wind south 20 km/h becoming light in the morning. High 12 except 18 inland.
    Night - Periods of rain. Low plus 4.
    Tue, 23 Apr - Periods of rain. High 6.
    Night - Periods of rain. Low plus 3.
    Wed, 24 Apr - Rain. High 7.
    Night - Cloudy with 30 percent chance of showers. Low plus 2.
    Thu, 25 Apr - Rain. High plus 5.
    Night - Cloudy. Low plus 3.
    Fri, 26 Apr - Cloudy. High 7.
    Night - Cloudy with 30 percent chance of showers. Low plus 2.



This project is for learning about webscraping only
============================

If you really need to manipulate weather data you should probably go to the Government of Canada Weather website first. They make xml files available for use and would be a better option for building a web app.  More info at the following link.

http://dd.weather.gc.ca/citypage_weather/docs/README_citypage_weather.txt


Weather Canada has a fairly permissive license with a few conditions.


http://dd.weather.gc.ca/doc/LICENCE_GENERAL.txt
