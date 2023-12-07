import requests
import math
import datetime


def kelvinToCelsius(temp):
    celsius = temp - 273.15
    return celsius


def cardinalDirection(wind_deg):
    val = math.floor((wind_deg / 22.5) + 0.5)
    arr = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    return arr[(val % 16)]


def info(country, time_now, sunrise, sunset, description, temp_celsius, temp_feels_like, pressure, humidity,
         wind_speed, wind_deg, visibility):
    print(f'\n{city.upper()}, {country}\n'
          f'{time_now} {description.capitalize()}. {kelvinToCelsius(temp_celsius):.1f} °C\n'
          f'Sunrise: {sunrise}. Sunset: {sunset}\n'
          f'Feels like {kelvinToCelsius(temp_feels_like):.1f} °C. Pressure: {pressure}hPa.\n'
          f'Humidity: {humidity}%. Wind Speed: {wind_speed}m/s {cardinalDirection(wind_deg)}\n'
          f'Visibility: {visibility / 1000}km\n')


base_url = 'http://api.openweathermap.org/data/2.5/weather?'
api_key = 'secret api key from openweathermap ;)'
city = input('Please enter city name: ').upper()
url = base_url + 'appid=' + api_key + '&q=' + city

response = requests.get(url).json()

country = response['sys']['country']
time_now = datetime.datetime.utcfromtimestamp(response['dt'])
sunrise = datetime.datetime.utcfromtimestamp(response['sys']['sunrise'])
sunrise = sunrise.strftime('%H:%M:%S')
sunset = datetime.datetime.utcfromtimestamp(response['sys']['sunset'])
sunset = sunset.strftime('%H:%M:%S')
description = response['weather'][0]['description']
temp_celsius = response['main']['temp']     # temp in kelvin to celsius
temp_feels_like = response['main']['feels_like']
pressure = response['main']['pressure']
humidity = response['main']['humidity']
wind_speed = response['wind']['speed']
wind_deg = response['wind']['deg']
visibility = response['visibility']


info(country, time_now, sunrise, sunset, description, temp_celsius, temp_feels_like, pressure, humidity, wind_speed,
     wind_deg, visibility)
