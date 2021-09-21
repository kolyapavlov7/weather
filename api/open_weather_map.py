import aiohttp
import asyncio
import json
import time
from dateutil.parser import parse


class OpenWeatherMapApi:
    URL = 'https://api.openweathermap.org'
    
    def __init__(self, token):
        self.token = token
        
    def weather(self, country_code, city, date):
        self.country_code = country_code
        self.city = city
        self.date = parse(date)
        self.timestamp = int(time.mktime(self.date.timetuple()))
        return self._start()
        
    def _start(self):
        loop = asyncio.get_running_loop()
        return loop.create_task(self.__start(), name='START_TASK')
        
    async def __start(self):
        coords_data = await self._coords()
        coords_data = coords_data[0]
        weather_data = await self._weather(coords_data['lat'], coords_data['lon'])
        item = None
        for item in weather_data.get('hourly', []):
            if item.get('dt') == self.timestamp:
                break
        return item

    def _weather(self, lat, lon):
        url = '{url}/data/2.5/onecall?lat={lat}&lon={lon}&exclude=current,daily,alerts,minutely&appid={token}'.format(url=self.URL, token=self.token, lat=lat, lon=lon)
        loop = asyncio.get_running_loop()
        task = loop.create_task(self.send_request(url), name='WEATHER_TASK')
        return task
    
    def _coords(self):
        url = '{url}/geo/1.0/direct?q={city},{country_code}&limit=1&appid={token}'.format(url=self.URL, token=self.token, city=self.city, country_code=self.country_code)
        loop = asyncio.get_running_loop()
        task = loop.create_task(self.send_request(url), name='COORDS_TASK')
        return task
        
    async def send_request(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                html = await response.read()
                data = json.loads(html)
        return data

