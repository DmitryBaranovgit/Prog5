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