import requests
import os
from smtplib import SMTP
# from twilio.rest import Client
# from twilio_ap

API_KEY = os.getenv("OPEN_WEATHER")



parameter = {
    "lat": 51.454514,
    "lon": -2.587910,
    "appid": API_KEY,
    "cnt": 4
}




r = requests.get("https://api.openweathermap.org/data/2.5/forecast",params=parameter)
status = r.status_code

data = r.json()

list = data["list"]

will_rain = True
for hour in list:
    code = hour["weather"][0]["id"]
    if int(code) < 700:
        will_rain = True

if will_rain:
    print("is raining")
    email = os.getenv("MY_EMAIL")
    password = os.getenv("MY_PASSWORD")

    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email,password=password)
        connection.sendmail(from_addr=email,to_addrs=email,msg="Subject: Weather For Today\n\nbring an Umbrella")