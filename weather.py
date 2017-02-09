import requests

def get_weather_forecast():
    # sign up to https://openweathermap.org/ to get your API key and then connect to the weather API
    url = 'http://api.openweathermap.org/data/2.5/weather?q=Southampton,uk&appid=addyouridhere'
    weather_request = requests.get(url)
    weather_json = weather_request.json()

    # parse json
    description = weather_json["weather"][0]["description"]
    min_temp = weather_json["main"]["temp_min"]
    max_temp = weather_json["main"]["temp_max"]

    # create forecast string
    forecast = 'The weather forecast for today is '
    forecast += description + ' with a high of ' + str(int(max_temp))
    forecast += ' and a low of ' + str(int(min_temp)) + '.'
    return forecast
