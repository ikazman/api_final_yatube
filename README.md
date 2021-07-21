### Описание проекта:

API для блог-платформы Yatube. Позоволяет читать, комментировать и создавать посты, подписываться на понравившихся авторов.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/ikazman/api_final_yatube
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Примеры запросов:


- документация к api:
http://127.0.0.1:8000/redoc/

- получение публикаций:
http://127.0.0.1:8000/api/v1/posts/

- получение комментариев:
http://127.0.0.1:8000/api/v1/posts/

- получение списка групп:
http://127.0.0.1:8000/api/v1/groups/
