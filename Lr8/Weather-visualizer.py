import matplotlib.pyplot as plt
import pandas as pd

def visualise_data(json_data = ''):
    if json_data:
        data = pd.read_json(json_data)
        city_name = data['city']

        dates = [measure['dt'] for measure in data['temps']]
        temps = [measure['temp'] for measure in data['temps']]

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