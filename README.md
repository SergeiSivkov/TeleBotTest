# TELEBot_Test
###  TELEBot_Test

Telegramm Bot с прикрученым SQLAlchemy + aiosqlite
Python 3.12
Для изучения фрейм ворка aiogram

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

Создать файл в коневой дирректории .env для хранения TOKEN к боту
```text

BOT_TOKEN = 'токен от вашего бота'

```

Запустить проект:

```bash
python3 main.py
```

#### технологии

+ **Python**
+ **aiogram**
+ **SQLALchemy**



#### Автор

[Сергей Сивков](https://github.com/SergeiSivkov)  

Cпецификация проекта: [openapi.json](
http://127.0.0.1:8000/openapi.json
)  
[Swagger](http://127.0.0.1:8000/docs)  
[ReDoc](http://127.0.0.1:8000/redoc)
