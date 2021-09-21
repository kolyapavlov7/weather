import psycopg2
import asyncio
import json

from psycopg2 import sql
from psycopg2.extras import DictCursor
from aiohttp import web

from api import OpenWeatherMapApi, WeatherDBApi
from settings import DATABASES, OPEN_WEATHER_MAP_API_KEY

async def weather_view(request):
    country_code = request.rel_url.query.get('country_code', '')
    city = request.rel_url.query.get('city', '')
    date = request.rel_url.query.get('date')

    if not all([country_code, city, date]):
        return web.Response(text='Не передан обязательный параметр!', status=400)

    country_code = country_code.lower()
    city = city.lower()

    db_api = WeatherDBApi(DATABASES['MAIN'])
    weather_from_db = db_api.get_weather(country_code, city, date)
    if weather_from_db is None:
        weather_api = OpenWeatherMapApi(token=OPEN_WEATHER_MAP_API_KEY)
        weather_data = await weather_api.weather(country_code, city, date)
        weather_data = json.dumps(weather_data)
        db_api.set_weather(country_code, city, date, weather_data)
    else:
        weather_data = json.dumps(weather_from_db)

    return web.Response(text=weather_data)
    

