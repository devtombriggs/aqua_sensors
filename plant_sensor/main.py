### TODO
import ph, water
import requests
import time

# Grab hello World from both py classes
def fetch_data():
    get_ph = ph.ph()
    get_water = water.water()

    return {"message": get_ph, "waterr": get_water }

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

