# weather тестовое задание

- Склонировать проект
```
git clone git@github.com:kolyapavlov7/weather.git
```

- Создать пользователя, БД и таблицы
```
sudo -u postgres psql
CREATE ROLE <role> PASSWORD '<password>' LOGIN;
CREATE DATABASE <db_name> OWNER <role>;
\c <db_name>;
CREATE TABLE countries (
  id SERIAL primary key,
  code varchar(10) UNIQUE NOT NULL
);
CREATE TABLE cities (
  id SERIAL primary key,
  country_id integer REFERENCES countries (id) NOT NULL,
  name varchar(100) NOT NULL,
  CONSTRAINT constraint1 UNIQUE (country_id, name)
);
CREATE TABLE weather (
  id SERIAL primary key,
  city_id integer REFERENCES cities (id) NOT NULL,
  date timestamp NOT NULL,
  data json,
  CONSTRAINT constraint2 UNIQUE (city_id, date)
);
GRANT ALL PRIVILEGES ON TABLE countries TO <role>;
GRANT ALL PRIVILEGES ON TABLE cities TO <role>;
GRANT ALL PRIVILEGES ON TABLE weather TO <role>;
GRANT USAGE, SELECT ON SEQUENCE countries_id_seq TO <role>;
GRANT USAGE, SELECT ON SEQUENCE cities_id_seq TO <role>;
GRANT USAGE, SELECT ON SEQUENCE weather_id_seq TO <role>;
```

- Установить настройки проекта
- - Переименовать файл settings/local.py.example.py в settings/local.py 
- - Заполнить настройки базы данны и ключ апи

- Запустить сервер
```  python3.8 main.py ```

- Перейти на страницу:
```  http://0.0.0.0:8080/weather?country_code=RU&city=Moscow&date=23.09.2021T12:00 ```
