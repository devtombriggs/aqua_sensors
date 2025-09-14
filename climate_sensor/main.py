### TODO
import humidity, weather
import requests

# Grab hello World from both py classes
def fetch_data():
    get_humidity = humidity.humdity()
    get_weather = weather.weather()

    return {"humidity": get_humidity, "weather": get_weather }

# Send Hello World to backend application with post method
def post_data():
    url = 'localhost'
    data = fetch_data()

    x = requests.post(url, json = data)

    print(x.text)

def main():
    print(fetch_data())

main()



