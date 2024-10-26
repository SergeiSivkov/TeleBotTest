# QRkot_spreadseets
###  приложение QRKot

Фонд собирает пожертвования на различные целевые проекты: 
на медицинское обслуживание нуждающихся хвостатых, на обустройство 
кошачьей колонии в подвале, на корм оставшимся без попечения кошкам — на любые
цели, связанные с поддержкой кошачьей популяции.


### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```bash
git clone git@github.com:SergeiSivkov/cat_charity_fund.git
```

```bash
cd cat_charity_fund
```

Cоздать и активировать виртуальное окружение:

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```
или для пользователей Windows

```bash
source env/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```bash
python3 -m pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

Выполнить миграции:

```bash
alembic upgrade head
```
Запустить проект:

```bash
uvicorn app.main:app --reload
```

#### технологии

+ **Python**
+ **FastAPI**
+ **SQLALchemy**
+ **Alembic**


#### Автор

[Сергей Сивков](https://github.com/SergeiSivkov)  

Cпецификация проекта: [openapi.json](
http://127.0.0.1:8000/openapi.json
)  
[Swagger](http://127.0.0.1:8000/docs)  
[ReDoc](http://127.0.0.1:8000/redoc)
