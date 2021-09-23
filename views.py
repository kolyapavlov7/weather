import json

from aiohttp import web
from dateutil.parser import parse

from api import OpenWeatherMapApi, WeatherDBApi
from settings import DATABASES, OPEN_WEATHER_MAP_API_KEY


async def weather_view(request):
    country_code = request.rel_url.query.get('country_code', '')
    city = request.rel_url.query.get('city', '')
    date = request.rel_url.query.get('date')

    if not country_code:
        return web.Response(text='Не передан обязательный параметр country_code!', status=400)

    if not city:
        return web.Response(text='Не передан обязательный параметр city!', status=400)

    if not date:
        return web.Response(text='Не передан обязательный параметр date!', status=400)

    country_code = country_code.lower()
    city = city.lower()

    try:
        parse(date)
    except ValueError:
        return web.Response(text='Не удалось распознать дату!')

    db_api = WeatherDBApi(DATABASES['MAIN'])
    date_for_db = parse(date)
    weather_from_db = db_api.get_weather(country_code, city, date_for_db)
    if weather_from_db is None:
        weather_api = OpenWeatherMapApi(token=OPEN_WEATHER_MAP_API_KEY)
        weather_data = await weather_api.weather(country_code, city, date)

        if weather_data is None:
            return web.Response(text='Не удалось найти погоду за указанный день!')

        is_success_response = isinstance(weather_data, dict) and weather_data.get('cod', 200) == 200
        weather_data = json.dumps(weather_data)
        if is_success_response:
            db_api.set_weather(country_code, city, date_for_db, weather_data)

    else:
        weather_data = json.dumps(weather_from_db)

    return web.Response(text=weather_data)
