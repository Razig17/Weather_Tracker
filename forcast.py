#!/usr/bin/env python3

"""This module contains get_forcast method"""

import requests

import json
import datetime
import os


def get_forcast(city="khartoum"):
    """Gets 5-day forecast"""

    api_key = os.environ.get('API_KEY')
    
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    data=response.json()
    with open("data2.json", "w") as file:
        json.dump(data, file)
    weather = {}
    for day in data["list"]:
        date = datetime.datetime.fromtimestamp(day["dt"]).strftime("%A")
        print(date, day["dt"])
        if date not in weather:
            weather[date] = {
                "date": date,
                "icon": day["weather"][0]["icon"],
                "temp_min": (int)(day["main"]["temp_min"]),
                "temp_max": (int)(day["main"]["temp_max"]),
            }
        if day["main"]["temp_min"] < weather[date]["temp_min"]:
            weather[date]["temp_min"] = (int)(day["main"]["temp_min"])
        if day["main"]["temp_max"] > weather[date]["temp_max"]:
            weather[date]["temp_max"] = (int)(day["main"]["temp_max"])
    days = []
    for day in weather:
        days.append(weather[day])
    if len(days) > 5:
        return (days[1:])
    return days

get_forcast()