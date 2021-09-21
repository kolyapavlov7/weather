import psycopg2

from psycopg2 import sql
from psycopg2.extras import DictCursor

class WeatherDBApi:
    def __init__(self, db_conf):
        self.db_conf = db_conf
        
    def get_weather(self, country_code, city, date):
        country_id = self.get_country_id(country_code)
        if country_id is None:
            return None
            
        city_id = self.get_city_id(country_id, city)
        if city_id is None:
            return None
            
        return self.get_weather_data(city_id, date)
        
    def set_weather(self, country_code, city, date, data):
        country_id = self.get_country_id(country_code)
        if country_id is None:
            country_id = self.insert_country(country_code)
            
        city_id = self.get_city_id(country_id, city)
        if city_id is None:
            city_id = self.insert_city(country_id, city)
            
        return self.insert_weather(city_id, date, data)
        
    def get_country_id(self, *args):
        query = '''SELECT id FROM countries WHERE code='{}';'''.format(*args)
        row = self.__sql(query)
        if row is not None:
            return row['id']
            
    def insert_country(self, *args):
        query = '''INSERT INTO countries (code) VALUES ('{}');'''.format(*args)
        self.__sql(query, response=False)
        return self.get_country_id(*args)
            
    def get_city_id(self, *args):
        query = '''SELECT id FROM cities WHERE country_id={} AND name='{}';'''.format(*args)
        row = self.__sql(query)
        if row is not None:
            return row['id']
            
    def insert_city(self, *args):
        query = '''INSERT INTO cities (country_id, name) VALUES ({}, '{}');'''.format(*args)
        row = self.__sql(query, response=False)
        return self.get_city_id(*args)
            
    def get_weather_data(self, *args):
        query = """SELECT data FROM weather WHERE city_id={} AND date='{}';""".format(*args)
        row = self.__sql(query)
        if row is not None:
            return row['data']
            
    def insert_weather(self, city_id, date, data):
        query = '''INSERT INTO weather (city_id, date, data) VALUES ({}, '{}', '{}');'''.format(city_id, date, data)
        row = self.__sql(query, response=False)
        return self.get_weather_data(city_id, date)
        
    def __sql(self, query, response=True, single=True):
        with psycopg2.connect(**self.db_conf) as conn:
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute(query)
                if not response or not cursor.rowcount:
                    return
                if single:
                    return cursor.fetchone()
                return cursor.fetchall()
