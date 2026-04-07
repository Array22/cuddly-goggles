import os
from typing import Union
import json
from datetime import datetime
from dotenv import load_dotenv
import csv
import requests
import pandas as pd

load_dotenv()

API_KEY = os.getenv("EODHD_API_KEY")
BASE_URL = "https://eodhd.com/api/eod/"
BASE_URL_LIVE = "https://eodhd.com/api/real-time/"
DATA_DIR = "data"
TICKERS_LIST = ["DTR", "BNZ", "DRO","4DX", "ZIP", "MEK", "OOO", "SNAS", "GYG", "PLS"]

def get_eod(ticker: str, today: bool = False, from_date: Union[str,None] = None):
    """Fetches EOD data for a given ticker. If today is True, 
    fetches only today's data; otherwise, fetches a year's worth of data.
    from_date should be in 'YYYY-MM-DD' format if provided."""
    url = f'{BASE_URL}{ticker}.AU?'
    params = {'api_token': API_KEY,
              'fmt': 'csv',
              'from': from_date}
    if today: #Today's data
        params['from'] = str(datetime.today().date())
    data = requests.get(url,params=params, timeout=10)
    data.raise_for_status()
    data = data.text
    try:
        if data and data.strip() != 'Value': #API returns 'Value' if no data is available in csv
            return data
        raise ValueError("No data returned from API")
    except ValueError as e:
        print(f"Error: {e}. Data for today may not be available yet.")
        return None

def get_realtime(ticker: str, fmt: str = 'csv'):
    """Fetches and returns real-time data for a given ticker."""
    url = f'{BASE_URL_LIVE}{ticker}.AU?api_token={API_KEY}&fmt={fmt}'
    data = requests.get(url,timeout=10)
    data.raise_for_status()
    return data

def export_csv(ticker: str, data) -> None:
    """Saves the provided data as a CSV file named after the ticker
        in the data directory."""
    filepath = os.path.join(DATA_DIR, f"{ticker}.csv")
    with open(filepath, "w", newline="", encoding='utf-8') as f:
        f.write(data)

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
    adds a 'Ticker' column. This is necessary for compatibility with the 
    SQL table schema."""
    filepath = os.path.join(DATA_DIR, f'{ticker}.csv')
    df = pd.read_csv(filepath)
    df.insert(0, 'Ticker', ticker)
    df.to_csv(filepath, index=False)
  

if __name__ == "__main__":
    # os.makedirs(DATA_DIR, exist_ok=True)
    # stocks = ['WTM', 'WBT', '4DX', 'AON']
    # for i in stocks:
    #     add_ticker(i)
    start_time = datetime.now()
    for i in TICKERS_LIST:
        export_csv(i, get_eod(i))
    end_time = datetime.now()
    print(f"Execution time: {end_time - start_time }")

    pass