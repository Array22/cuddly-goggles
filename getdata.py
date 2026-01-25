import os, requests, json
import pandas as pd
from datetime import datetime
import csv

API_KEY = os.getenv("EODHD_API_KEY")
BASE_URL = "https://eodhd.com/api/eod/"
BASE_URL_LIVE = "https://eodhd.com/api/real-time/"
DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

# TODO: fix params, use dict instead of manual string
def get_EOD(ticker: str, fmt: str = 'csv', today: bool = False):
    if today: #get today's data only
        url = (f'{BASE_URL}{ticker}.AU?api_token={API_KEY}&fmt={fmt}&from='
        f'{datetime.today().date()}')
    else: #get year's worth of data
        url = f'{BASE_URL}{ticker}.AU?api_token={API_KEY}&fmt={fmt}'
    params = {'api_token': f'{API_KEY}',
              'fmt': fmt}
    data = requests.get(url,timeout=10) #make request
    data.raise_for_status()
    return data

def get_realtime(ticker: str, fmt: str = 'csv'):
    url = f'{BASE_URL_LIVE}{ticker}.AU?api_token={API_KEY}&fmt={fmt}'
    data = requests.get(url,timeout=10) #make request
    data.raise_for_status()
    return data

def export_json(ticker: str, data) -> None: #ticker only needed for name
    filepath = os.path.join(DATA_DIR, f"{ticker}.json")
    with open(filepath, "w") as f:
        json.dump(data.json(), f, indent=4)

def export_csv(ticker: str, data) -> None: #ticker only needed for name
    filepath = os.path.join(DATA_DIR, f"{ticker}.csv")
    with open(filepath, "w", newline="") as f:
        f.write(data.text)
        
def update_ticker(ticker: str) -> None: #only works day after
    data_today = get_EOD(ticker, today= True).text
    filepath = os.path.join(DATA_DIR, f'{ticker}.csv')
    with open(filepath, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer([file])
        writer.writerow(data_today)
        

if __name__ == "__main__":
    # export_json('DTR', get_EOD('DTR'))
    # export_csv('DTR', get_EOD('DTR','csv'))
    print(get_EOD('DTR').text)
    
    # data = get_realtime('DTR',fmt='csv').text
    # export_csv('DTR today', data)
    
    pass