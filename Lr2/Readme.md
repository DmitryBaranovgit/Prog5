# Использование Weather API
# В данной лабораторной работе показано, как использовать API OpenWeatherMap для получения данных о погоде для различных местоположений. Лабораторная работа состоит из трех основных файлов:

## functionweather.py:
* Содержит функцию, которая получает данные о погоде из API OWM. ```get_weather_data```
* Функция принимает два параметра: (название города) и (ключ API)#
```location``` ```api_key```
* Если ключ API не указан, выводится сообщение и None
* Функция выполняет GET-запрос к API OWN и возвращает текст ответа в случае успеха, либо сообщение об ошибке.
```
import requests
import json

def get_weather_data(location, api_key = None):
    if not api_key:
        print("API not found")
        return None
    try:
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather', params = {'q': location, 'appid': api_key, 'units': 'metric'})
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Data request error: {e}")
        return None
```
## test_function_weather.py:
* test_key: Возращает функцию, если ключ API не предоставлен
* test_type: Проверяет, возвращает ли функция строку при действительном ключе API
* test_coords: Проверяет, содержит ли ответ координаты (долготу и широту)
* test_temp: Гарантирует, что температура плавающая
* test_countries: Использует параметризованное тестирование для проверки того, что код страны в ответе правильный
```
import pytest
import json
from functionweather import get_weather_data

key = 'b1c3eaf47e2ed5a67cf5cc0dcfffa7f8'

def test_key():
    assert get_weather_data("Moscow") is None
def test_type():
    assert isinstance(get_weather_data("Moscow", api_key = key), str)
def test_coords():
    data = json.loads(get_weather_data('Moscow', api_key = key ))
    assert len(data.get('coord', {})) == 2, "Dimension is 2: lon and lat"
def test_temp():
    data = json.loads(get_weather_data('Moscow', api_key = key))
    assert isinstance(data.get('main', {}).get('feels_like'), float)
params = "city, api_key, country"
countries =  [
    ("Paris", key, 'FR'),
    ("Rome", key, 'IT'),
    ("Toronto", key, 'CA'),
    ("Berlin", key, 'DE'),
    ("Sydney", key, 'AU'),
    ("London", key, 'GB'),
    ("Madrid", key, 'ES')
]

@pytest.mark.parametrize(params, countries)
def test_countries(city, api_key, country):
    data = json.loads(get_weather_data(city, api_key = key))
    assert data.get('sys', {}).get('country', 'NoValue') == country
```
## main.py
* Демонстрирует, как пользоваться get_weather_data
* Устанавливает и извлекает данные о погоде для города weather_api_key
* Выводит данные о погоде в случае успешного выполнения запроса, в противном случае выводит сообщение об ошибке
```
from functionweather import get_weather_data

weather_api_key = 'b1c3eaf47e2ed5a67cf5cc0dcfffa7f8'

if __name__ == '__main__':
    city = 'Paris'
    data = get_weather_data(city, api_key = weather_api_key)
    if data:
        print(data)
    else:
        print('Failed to get weather data')
```
Результат:
![Результат:](/Lr2/Lr2.png "Результат")
