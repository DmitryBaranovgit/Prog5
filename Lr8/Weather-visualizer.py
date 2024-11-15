import matplotlib.pyplot as plt
import pandas as pd
import json
from Weather_data_fetcher import getweather
from datetime import datetime

def visualise_data(json_data = ''):
    if json_data:
        data = json.loads(json_data)
        city_name = data.get('city', 'Санкт-Петербурге')
        dates = [datetime.utcfromtimestamp(measure['dt']).strftime('%Y-%m-%d %H:%M') for measure in data['temps']]
        temps = [measure['temp'] for measure in data['temps']]

        if not dates or not temps:
            print("Данные для графиков отсутствуют.")
            return 
        
        plt.figure(figsize = (12, 6))
        plt.subplot(1, 2, 1)
        plt.scatter(dates, temps, color = 'blue')
        plt.title(f"Температура в {city_name} за последние 5 дней")
        plt.xlabel("Дата")
        plt.ylabel("Температура (°C)")
        plt.xticks(rotation = 45)

        plt.subplot(1, 2, 2)
        plt.boxplot(temps, vert = True, patch_artist = True)
        plt.title("Распределение температуры (Boxplot)")
        plt.ylabel("Температура (°C)")

        plt.tight_layout()
        plt.show()

api_key = 'a4611204101ca7a351f889896311963d'
weather_data_json = getweather(api_key)
visualise_data(weather_data_json)