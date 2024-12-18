# Bonus Program REST API

## Описание проекта
Это REST API-сервис, реализованный с использованием FLASK, который позволяет пользователям получать информацию о текущем уровне бонусной программы и следующем уровне. Сервис защищён с использованием JWT-аутентификации, чтобы каждый пользователь мог видеть только свои данные.

## Функциональность
1. Аутентификация пользователя с использованием JWT.
2. Получение информации о текущем бонусном уровне, тратах и следующем уровне.
3. Токены безопасности имеют ограниченный срок действия (30 минут).

## Установка

### Требования

- Python 3.10 или выше
- Установленные зависимости

### Установка зависимостей

```
git clone 
cd bonus-program-api
pip install -r requirements.txt
```

Создайте файл requirements.txt:

```
Flask
flask-jwt-extended
```

### Запуск проекта

1. Откройте терминал и перейдите в директорию проекта.
2. Запустите сервер:

```
python Lr9.py
```

3. API будет доступен по адресу: http://127.0.0.1:5000/

### Использование API

1. Корневой маршрут (/)

Метод: GET

Описание: Возвращает приветственное сообщение с описанием доступных эндпоинтов.

Пример ответа:

```
{
        "message": "Welcome to the Bonus Program API!",
        "endpoints": {
            "login": "/login (POST)",
            "get_bonus_info": "/bonus (GET)"
        }
    }
```
2. Аутентификация (/login)

Метод: POST

Описание: Используется для получения JWT-токена. Укажите логин и пароль пользователя.

Пример запроса:

{
    username = data.get("username")
    password = data.get("password")
}

Пример ответа:

```
{
    "token": ""
}

Коды ответа:

200 OK - Успешная авторизация.

401 Unauthorized - Неверный логин или пароль.

3. Получение данных о бонусах (/bonus)

Метод: GET

Описание: Возвращает информацию о текущем бонусном уровне и следующем уровне. Требуется токен.

Заголовки:

```
Authorization: Bearer <>
```

Пример ответа:

```
{
        "current_level": "Silver",
        "spending": 500,
        "next_level": "Gold",
        "next_level_min_spending": 1000,
    }
```

Коды ответа:

200 OK - Успешное получение данных.

401 Unauthorized - Токен отсутствует или недействителен.

404 Not Found - Пользователь не найден.

# Пример данных о пользователях и бонусной программе
users = {
    "user1": {"password": "password1", "spending": 500, "level": "Silver"},
    "user2": {"password": "password2", "spending": 1500, "level": "Gold"},
    }

bonus_levels = {
    "Silver": {"next_level": "Gold", "min_spending": 1000},
    "Gold": {"next_level": "Platinum", "min_spending": 2000},
    "Platinum": {"next_level": None, "min_spending": None},
}

### Пример пользования

1. Получение токена

Отправьте запрос:

```
curl -X POST http://127.0.0.1:5000/login -H "Content-Type: application/json" -d '{"username": "user1", "password": "password1"}'
```

Пример ответа:

```
{
    "token": ""
}

2. Получение данных о бонусах

Используйте полученный токен:

```
curl -X GET http://127.0.0.1:5000/bonus -H "Authorization: Bearer your-jwt-token"
```

Пример ответа:

```
{
    "current_level": "Silver",
    "spending": 500,
    "next_level": "Gold",
    "next_level_min_spending": 1000,
}

# Структура проекта

```
bonus-program-api/
--- Lr9.py # Основной файл приложения
--- Requirements.txt # Зависимости
--- Readme.md # Документация проекта