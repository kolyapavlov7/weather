# weather тестовое задание

- Склонировать проект
```
git clone git@github.com:kolyapavlov7/weather.git
```

- Создать пользователя, БД
```
sudo -u postgres psql
CREATE ROLE <role> PASSWORD '<password>' LOGIN;
CREATE DATABASE <db_name> OWNER <role>;
```

- Перейти в папку проекта и установить настройки проекта
- - Перейти в папку проекта 
```cd weather```
- - Создать файл локальных настроек
```cp settings/local.py.example.py settings/local.py```
- - Заполнить в файле ```settings/local.py``` настройки базы данны и ключ к апи ```openweathermap```

- Запустить сервер
```  python3.8 main.py ```

- Перейти на страницу:
```  http://0.0.0.0:8080/weather?country_code=RU&city=Moscow&date=23.09.2021T18:00 ```
