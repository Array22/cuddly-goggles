import plotly.graph_objs as go
import pandas as pd
from pathlib import Path
from getdata import DATA_DIR

def to_df(ticker: str):
    filepath = Path(DATA_DIR) / f"{ticker}.csv"
    df = pd.read_csv(filepath)
    return df

def prep_candlestick(ticker, df): #takes pandas df
    chart = go.Candlestick(
        x=df['Date'],
        open=df['Open'],
        high=df['High'],
        low=df['Low'],
        close=df['Close']
    )
    layout = go.Layout(
        title=f'{ticker} Price Chart',
        xaxis={'title': 'Time', 'type': "category"},
        yaxis={'title': 'Price (AUD)'},
        dragmode='zoom'
    )
    return chart, layout

def plot_candlestick(ticker: str) -> None:
    df = to_df(ticker)
    chart, lay = prep_candlestick(ticker, df)
    fig = go.Figure(data=chart, layout=lay)
    return fig
    

if __name__ == "__main__":
    plot_candlestick('DTR').show()
    pass