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
####
#     if type(city) is not str:
#         raise ValueError('параметр city не является строкой')
#     if not my_secret:
#         raise ValueError('ключ для отправки запросов к API не задан')

#     query = f"http://api.openweathermap1.org/data/2.5/weather?q={city}&units=metric&appid={my_secret}"
#     try:
#         r = requests.get(query)
#     except requests.RequestException as e:
#         print(f'Ошибка отправки или получения ответа от API openweathermap.org  ')
#     else:
#         if r.status_code == 200:
#             data = r.text
#             # return data
#             return json.loads(data)
#         if r.status_code == 404:
#             print(f'В параметрах запроса (вероятно, в параметре город - ошибка. Ответ 404')


# if type(get_weather_data('anadyr', key=my_secret)) is dict:
#     print((get_weather_data('anadyr', key=my_secret)['main']['pressure']))

# print(get_weather_data('kdkfjsdf', key=my_secret))

# # if type(get_weather_data('kdkfjsdf', key=my_secret)) is dict:
# #     print((get_weather_data('skdfjslfjslkdf', key=my_secret)['main']['pressure']))
####
