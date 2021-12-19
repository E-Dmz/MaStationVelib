from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from velib.data import get_data, get_station

df = get_data()#nrows=100_000)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def index():
    return dict(greeting="hello")

@app.get("/station")
def station(station # 8037
            ):
    station=int(station)
    df_station=get_station(df, station)
    return df_station.to_dict()

if __name__ == "__main__":
    print(index())