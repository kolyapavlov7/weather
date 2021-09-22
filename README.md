# weather
weather тестовое задание

- Склонировать проект
  git clone git@github.com:kolyapavlov7/weather.git

- Создать пользователя и базу данных
  sudo -u postgres psql
  CREATE ROLE <role> PASSWORD '<password>' LOGIN;
  CREATE DATABASE <db_name> OWNER <role>;
  \c <db_name>;

- Установить настройки
  Переименовать файл settings/local.py.example.py в settings/local.py 
  Заполнить настройки базы данны и ключ апи

- Запустить сервер
  python3.8 main.py

- Перейти на страницу:
  http://0.0.0.0:8080/weather?country_code=RU&city=Moscow&date=22.09.2022T14:00
