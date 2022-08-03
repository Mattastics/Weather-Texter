import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "*********************"
account_sid = "**********************"
auth_token = "*************************"
client = Client(account_sid, auth_token)



weather_params = {
    "lat": 38.391392,
    "lon":-85.755127,
    "exclude": "current,minutely,daily",
    "units": "imperial",
    "appid": api_key
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:15]

will_rain = False

for hour_data in weather_slice:
    condition_code = (hour_data["weather"][0]["id"])
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    message = client.messages \
        .create(
        body="Rain incoming today!",
        from_='+***********',
        to='+***********'
    )
    print(message.status)
