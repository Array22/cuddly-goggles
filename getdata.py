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
def get_eod(ticker: str, fmt: str = 'csv', today: bool = False):
    """Fetches EOD data for a given ticker. If today is True, 
    fetches only today's data; otherwise, fetches a year's worth of data."""
    if today: #Today's data
        url = (f'{BASE_URL}{ticker}.AU?api_token={API_KEY}&fmt={fmt}&from='
        f'{datetime.today().date()}')
    else: #Year of data
        url = f'{BASE_URL}{ticker}.AU?api_token={API_KEY}&fmt={fmt}'
    params = {'api_token': f'{API_KEY}',
              'fmt': fmt}
    data = requests.get(url,params=params, timeout=10)
    data.raise_for_status()
    return data

def get_realtime(ticker: str, fmt: str = 'csv'):
    """Fetches and returns real-time data for a given ticker."""
    url = f'{BASE_URL_LIVE}{ticker}.AU?api_token={API_KEY}&fmt={fmt}'
    data = requests.get(url,timeout=10)
    data.raise_for_status()
    return data

def export_json(ticker: str, data) -> None:
    """Saves the provided data as a JSON file named after the ticker
        in the data directory."""
    filepath = os.path.join(DATA_DIR, f"{ticker}.json")
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data.json(), f, indent=4)

def export_csv(ticker: str, data) -> None:
    """Saves the provided data as a CSV file named after the ticker
        in the data directory."""
    filepath = os.path.join(DATA_DIR, f"{ticker}.csv")
    with open(filepath, "w", newline="", encoding='utf-8') as f:
        f.write(data.text)
    
def update_ticker(ticker: str) -> None:
    """Fetches today's data for the given ticker and appends it to the 
        existing CSV file. May not work if the API does not provide 
        same-day data yet."""
    data_today = get_eod(ticker, today= True).text
    filepath = os.path.join(DATA_DIR, f'{ticker}.csv')
    with open(filepath, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer([file])
        writer.writerow(data_today)

def add_ticker(ticker: str):
    """Reads the existing CSV file for the given ticker, 
    adds a 'ticker' column. This is necessary for compatibility with the 
    SQL table schema."""
    filepath = os.path.join(DATA_DIR, f'{ticker}.csv')
    df = pd.read_csv(filepath)
    df.insert(0, 'ticker', ticker)
    df.to_csv(filepath, index=False)
    
def to_lowercase(): #change headers to lowercase
    """Reads all CSV files in the data directory, converts their headers to 
    lowercase, and saves the modified files back to the data directory."""
    pass
        

if __name__ == "__main__":
    stocks = ['WTM', 'WBT', '4DX', 'AON']
    for i in stocks:
        add_ticker(i)
    # # export_json('DTR', get_eod('DTR'))
    # # export_csv('DTR', get_eod('DTR','csv'))
    # for i in stocks:
    #     data = get_eod('DTR')
    #     export_csv(i, data)
    

    
    # data = get_realtime('DTR',fmt='csv').text
    # export_csv('DTR today', data)
    
    pass