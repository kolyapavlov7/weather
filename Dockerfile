# образ на основе которого создаём контейнер
FROM python:3.8

# рабочая директория внутри проекта
WORKDIR /usr/src/app

# переменные окружения для python
ENV  PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -yyq netcat
    # && apt install python3.8
# RUN apk update \
#    && apk add postgresql-dev gcc python3-dev musl-dev

# устанавливаем зависимости
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./entrypoint.sh .

# копируем содержимое текущей папки в контейнер
COPY . .

# run entrypoint.sh
# ENTRYPOINT ["entrypoint.sh"]
