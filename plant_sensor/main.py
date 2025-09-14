### TODO
import water, ph
import requests

# Grab hello World from both py classes
def fetch_data():
    get_ph = ph.humdity()
    get_water = water.weather()

    return {"ph": get_ph, "water": get_water }

# Send Hello World to backend application with post method
def post_data():
    url = 'localhost'
    data = fetch_data()

    x = requests.post(url, json = data)

    print(x.text)

def main():
    print(fetch_data())

main()