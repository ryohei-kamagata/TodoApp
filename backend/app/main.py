import sys
sys.path.append("/Users/kamariyo2/opt/anaconda3/lib/python3.9/site-packages")
from fastapi import FastAPI
import requests

ROOT_PATH = '/api'

app = FastAPI()

@app.get("/")
def read_root():
    url = "https://www.jma.go.jp/bosai/forecast/data/forecast/130000.json"
    r = requests.get(url).json()
    return {"response": r[0]["timeSeries"][0]["areas"][0]["area"]["name"]}
