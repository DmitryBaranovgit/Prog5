from functionweather import get_weather_data

weather_api_key = 'b1c3eaf47e2ed5a67cf5cc0dcfffa7f8'

if __name__ == '__main__':
    city = 'Paris'
    data = get_weather_data(city, api_key = weather_api_key)
    if data:
        print(data)
    else:
        print('Failed to get weather data')