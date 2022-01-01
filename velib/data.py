import pandas as pd
import datetime as dt
import os

today = dt.date.today()

def get_data(path='./data/data-5m.csv',
             nrows=None):
    df = pd.read_csv(path,
                     nrows=nrows,
                     low_memory=False
                    )
    df['datetime'] = pd.to_datetime(df.datetime, format='%Y-%m-%d %H-%M')
    for col in ['stationCode', 'meca', 'elec', 'park']:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    df = df.dropna()
    for col in ['stationCode', 'meca', 'elec', 'park']:
        df[col] = df[col].astype(int)
    return df

path='./data/data-5m-2021-16-12.csv'

def get_last_data(days=7):
    df = pd.read_csv(path, low_memory=False)
    df['datetime'] = pd.to_datetime(df.datetime, format='%Y-%m-%d %H-%M')
    
    # select last week
    last_dt = df.datetime.max()
    first_dt = last_dt - dt.timedelta(days=days)
    df = df[df.datetime > first_dt]
    for col in ['stationCode', 'meca', 'elec', 'park']:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    df = df.dropna()
    for col in ['stationCode', 'meca', 'elec', 'park']:
        df[col] = df[col].astype(int)
    return df

def get_station(df, station):
    return df[df.stationCode==station]

if __name__ == "__main__":
    # df = get_data(nrows=100_000)
    # df_station=get_station(df, 8037)
    # df = get_last_data(1)
    # df = get_station(df, 12001)
    # print(len(df))
    print(os.getcwd())