#!/usr/bin/env python3

"""A flask Weather app"""


from flask import Flask, render_template, request, session, url_for
import requests
import datetime
from forcast import get_forcast

app = Flask(__name__)
api_key = "Your api key"
app.secret_key = "razig"



@app.route("/", methods=["POST", "GET"])
@app.route("/weather", methods=["POST", "GET"])
def weather():
    if request.method == "GET":
        city = "khartoum"
    else:
        city = request.form["city"]
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code != 200:
        city = session["city"]
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)

    data = response.json()
    weather = {}
    weather["description"] = data["weather"][0]["description"]
    weather["temperature"] = (int)(data["main"]["temp"])
    weather["city"] = data["name"]
    weather["main"] = data["weather"][0]["main"]
    weather["wind"] = data["wind"]["speed"]
    weather["humidity"] = data["main"]["humidity"]
    weather["pressure"] = data["main"]["pressure"]
    weather["visibility"] = data["visibility"]
    timestamp = data["dt"]
    timezone = data["timezone"]
    utc_time = datetime.datetime.utcfromtimestamp(timestamp)
    date = utc_time + datetime.timedelta(seconds=timezone)
    weather["date"] = date.strftime("%Y/%m/%d")
    weather["icon"] = data["weather"][0]["icon"]
    weather["day"] = date.strftime("%A")
    session["city"] = city
    forecast = get_forcast(city)
    return render_template("index2.html", weather=weather, forecast=forecast)



if __name__ == "__main__":
    app.run(debug=True)
