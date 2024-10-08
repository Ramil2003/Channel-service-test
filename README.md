# Google sheets django

Функционал:

- Получение данных из Google Sheets
- Добавление этих данных в БД, с добавлением колонки "стоимость в руб"
  - ДБ созданно с помощью Postgres
  - Доллар получаем из сайта [ЦБ РФ](https://www.cbr.ru/scripts/XML_daily.asp)
- Скрипт работает онлайн с помощью Celery. Через какое-то время проверяется состояние Google Sheets
- Решение упаковано в Docker\Docker-compose
- Разработан на Django

## Инструкция:

Склонируйте проект:
```
https://github.com/Ramil2003/Channel-service-test.git
```

Создайте виртуальное окружение:
```
python3 -m venv venv
```

Активируйте вирт. окружение:
```
source venv/bin/activate
```

Установите зависимости:
```
pip install -r requirements.txt
```

Запустите docker-compose:
```
docker-compose up --build
```

Создайте суперюзера:
```
docker-compose exec web python3 manage.py createsuperuser
```

После использования не забывайте прописать:
```
docker-compose down
```

P.S **Создайте .env и пропишите данные для БД и SECRET_KEY**
