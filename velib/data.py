import pandas as pd

def get_data(path='/data/data-5m-2021-16-12.csv',
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

def get_station(df, station):
    return df[df.stationCode==station]

if __name__ == "__main__":
    df = get_data(nrows=100_000)
    df_station=get_station(df, 8037)
    print(len(df_station))