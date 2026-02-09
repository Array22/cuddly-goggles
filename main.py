from typing import Union
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from pydantic import BaseModel
from graphing import plot_candlestick
import plotly.io as pio
from pathlib import Path

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/", response_class=HTMLResponse)
def read_root():
    return FileResponse('test.html')

@app.get("/charts", response_class=HTMLResponse)
def read_charts():
    fig = plot_candlestick('DTR')
    html = pio.to_html(fig)
    return html

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}