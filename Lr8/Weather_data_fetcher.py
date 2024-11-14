import requests
import json

city, lat, lon = "Saint Petersburg, RU", 59.57, 30.19
api_key = 'a4611204101ca7a351f889896311963d'
dt = 1671354770

def getweather(api_key = None):
    city, lat, lon = "Saint Petersburg, RU", 59.57, 30.19
    dt = 1671354770

    if api_key:
        result = dict()
        req = requests.get(
            f'http://api.openweathermap.org/data/2.5/forecast?'
            f'lat={lat}&lon={lon}&dt={dt}&'
            f'appid={api_key}&lang=ru&units=metric'
        )
        req_obj = json.loads(req.text)
        result['cirt'] = city
        measures = [{"dt": measure['dt'], "temp": measure['main']['temp']} for measure in req_obj["list"]]
        result['temps'] = measures
        return json.dumps(result)

weather_data_json = getweather(api_key)
print(weather_data_json)