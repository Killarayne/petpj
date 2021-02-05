from flask import current_app
import requests


def get_weather(city_name):
    weather_url = current_app.config['WEATHER_URL']
    params = {'key': current_app.config['WEATHER_API_KEY'],
              'q': city_name,
              'format': 'json',
              'num_of_days': '1',
              'showlocaltime': 'yes',
              'lang': 'ru'}
    try:
        res = requests.get(url=weather_url, params=params)
        res.raise_for_status()
        weather = res.json()
        if 'data' in weather:
            if "current_condition" in weather['data']:
                try:
                    return weather['data']['current_condition'][0]
                except(IndexError, TypeError):
                    return False
    except (requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False
    return False
