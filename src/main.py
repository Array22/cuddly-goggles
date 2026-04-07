from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
# from graphing import plot_candlestick
# from supabase import create_client, Client
# import plotly.io as pio

app = FastAPI()

# supabase: Client = create_client(os.environ.get("SUPABASE_URL"),
#                                  os.environ.get("SUPABASE_PUBLISHABLE_KEY"))

class StockData(BaseModel):
    """Stock data from EODHD API"""
    Date: str
    Open: float
    High: float
    Low: float
    Close: float
    Adjusted_close: float
    Volume: int
  
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
    return FileResponse('test.html')

# @app.get("/table")
# def read_table():
#     data = supabase.table()

# @app.get("/charts", response_class=HTMLResponse)
# def read_charts():
#     fig = plot_candlestick('DTR')
#     html = pio.to_html(fig)
#     return html