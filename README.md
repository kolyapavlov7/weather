# weather
weather тестовое задание

sudo -u postgres psql

create role and data_base 
git clone git@github.com:kolyapavlov7/weather.git
Создать файл settings.py в корне проекта
и заполнить настройки:

OPEN_WEATHER_MAP_API_KEY = '<api_key>'
DATABASES = {
    'MAIN': {
        'dbname': '<dbname>',
        'user': '<user>',
        'password': '<password>',
        'host': '<host>',
    }
}

Создать таблицы 

python3.8 main.py

Перейти на страницу:
http://0.0.0.0:8080/weather?country_code=RU&city=Moscow&date=22.09.2022T14:00
