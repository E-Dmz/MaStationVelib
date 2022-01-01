from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from velibapi.query import query_station
import pandas as pd

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
    return dict(running=True)

@app.get("/day-station")
def data_station(code_station, day):
    code_station = int(code_station)
    day = pd.Timestamp(day)
    df = query_station(code_station, 1, day)
    return df.to_dict()

if __name__ == "__main__":
    # print(len(station('12001')))
    data_dict = data_station('12001','2021-11-10')
    df = pd.DataFrame(data_dict)
    print(len(df))