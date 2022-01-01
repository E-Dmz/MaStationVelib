# module query in package velibapi
import os
import sqlite3
import pandas as pd
import datetime as dt

DB_PATH = os.path.join('data', 'velib.sqlite')

def query_station(
    station_code: int, 
    days: int = None,
    first_dt: pd.Timestamp = None,
    last_dt: pd.Timestamp = None
    ) -> pd.DataFrame:
    """
    returns the data corresponding to a station and a period of time
    requires (days & (first_dt | last_dt)) | (first_dt & last_dt)
    """

    if days:
        if first_dt:
            last_dt = first_dt + dt.timedelta(days=days)
        else:
            first_dt = last_dt - dt.timedelta(days=days)
            
    query = """
        SELECT s.datetime, s.meca + s.elec AS bikes, s.park
        FROM stations s
        WHERE (s.stationCode = ? 
            AND s.datetime BETWEEN ? AND ?)
    """
    params = (str(station_code), str(first_dt), str(last_dt))
    
    with sqlite3.connect(DB_PATH) as conn:
        df = pd.read_sql_query(query, conn, params=params, 
                               parse_dates="datetime")
    return df

if __name__ == '__main__':
    df = query_station(7001, days=1, first_dt=pd.Timestamp('2021-12-16'))
    print(df.shape == (289,3))