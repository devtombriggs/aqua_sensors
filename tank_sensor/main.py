### TODO
import ph, temp
import requests
import time

# Grab hello World from both py classes
def fetch_data():
    get_ph = ph.ph()
    get_temp = temp.temp()

    return {"message": get_ph, "weather": get_temp }

# Send Hello World to backend application with post method
def post_data():
    url = 'http://localhost:8080/api/ingest'
    data = fetch_data()

    x = requests.post(url, json = data)

    print(x.text)

def main():
    print(fetch_data())
    post_data()

while True:
    time.sleep(3)
    main()

