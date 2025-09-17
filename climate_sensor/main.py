### TODO
import humidity, weather
import requests
import time

# Grab hello World from both py classes
def fetch_data():
    get_humidity = humidity.humdity()
    get_weather = weather.weather()

    return {"message": get_humidity, "weather": get_weather }

# Send Hello World to backend application with post method
def post_data():
    url = 'http://172.18.0.1:8080/api/ingest'
    data = fetch_data()

    x = requests.post(url, json = data)

    print(x.text)

def main():
    print(fetch_data())
    post_data()

while True:
    time.sleep(300)
    main()

