import ph, temp
import requests
import time

def fetch_data():
    get_ph = ph.ph()
    get_temp = temp.temp()

    return {"message": get_ph, "weather": get_temp }

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

