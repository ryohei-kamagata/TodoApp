import fastapi
import requests

app = fastapi.FastAPI()

@app.get("/weather/")
def read_root():
    url = "https://www.jma.go.jp/bosai/forecast/data/forecast/130000.json"
    r = requests.get(url)
    return {"Hello": "World"}

