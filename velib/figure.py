import os
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns

ABS_PATH = os.getcwd()
# if os.path.basename(ABS_PATH) != 'MaStationVelib':
#     os.chdir(os.path.dirname(ABS_PATH))
#     ABS_PATH = os.getcwd()
#     if os.path.basename(ABS_PATH) != 'MaStationVelib':
#         raise NameError("There's a problem with path")

DATA_PATH = os.path.join(ABS_PATH, "data", "data-5m.csv")

class Velib:
    def __init__(self, path=DATA_PATH, clean=True):
        self.df = pd.read_csv(path,
                     low_memory=False
                    )
        self.clean = False
        if clean:
            self.raw_df = self.df.copy()
            self.clean_df()

    def clean_df(self):
        self.df['datetime'] = pd.to_datetime(self.df.datetime, format='%Y-%m-%d %H-%M')
        for col in ['stationCode', 'meca', 'elec', 'park']:
            self.df[col] = pd.to_numeric(self.df[col], errors='coerce')
        self.df = self.df.dropna()
        for col in ['stationCode', 'meca', 'elec', 'park']:
            self.df[col] = self.df[col].astype(int)
        self.clean = True

    def get_df(self, raw=False):
        if raw:
            return self.raw_df
        if self.clean:
            print("dataframe has been cleaned")
            return self.df
        print("dataframe has NOT been cleaned")
        return self.df
    
    def get_number_rows(self):
        return len(self.df)
    
    def get_list_stations(self):
        return self.df.stationCode.unique()
    
    def get_dt_dict(self):
        df = self.df
        dt_dict = {
            "min": self.df.datetime.min(),
            "max": self.df.datetime.max(),
            "period": self.df.datetime.max() - self.df.datetime.min(),
        }
        return dt_dict
    
    def get_station(self, station_code, days=None, first_dt=None, last_dt=None):
        last_dt = last_dt if last_dt else self.df.datetime.max()
        if days:
            if first_dt:
                last_dt = first_dt + dt.timedelta(days=days)
            else:
                first_dt = last_dt - dt.timedelta(days=days)
        if not first_dt:
            first_dt = self.df.datetime.min()
        df = self.df[self.df.stationCode==station_code]
        df = df[(df.datetime >= first_dt) & (df.datetime < last_dt)]
        return df    

    def plot_station(self, station_code, days=None, first_dt=None, last_dt=None):
        df = self.get_station(station_code, days=days, first_dt=first_dt, last_dt=last_dt)
        return df.plot(x="datetime", y=["meca","park"])

def plot_day(velib, station_code, day):
    fig = plt.figure()
    ax = plt.subplot()
    df = velib.get_station(station_code, 1, day)
    df['total'] = df.meca + df.elec
    df['time'] = df.datetime.dt.hour + df.datetime.dt.minute/60

    sns.lineplot(ax=ax, data=df, x="time", y="total", color='g')
    sns.lineplot(ax=ax, data=df, x="time", y="park", color='purple')
    ax.set_xlabel('')
    
    ax.set_xticks([i for i in range(0,24,3)] + [24])
    ax.set_xticklabels([f"{i}:00" for i in range(0,24,3)] + ['0:00'])
    
    
    for label in ax.get_xticklabels():
        label.set_rotation(45)
        label.set_ha('right')
    fig.tight_layout()
    return fig