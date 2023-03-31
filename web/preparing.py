import os
from pathlib import Path
import sqlite3
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('id_station.txt', delimiter=';')
del df[df.columns[-1]]
# connection= sqlite3.connect('../db.sqlite3')
# df.to_sql('station',connection, if_exists='replace')
# connection.close()
bundesland_name = input('Enter Bundesland to find:\n').title()
possible_station = df.loc[df.Bundesland.str.contains(bundesland_name), ['Stations_id', 'Stationsname', 'Bundesland']]
print(possible_station)
station_id = int(input("Please Enter the Station_id of Desired Station:"))


def process(station):
    file_path = os.path.join(Path(__file__).parent.resolve(), 'temperature.txt')
    temper_df = pd.read_csv(file_path,delimiter=';')
    del temper_df[temper_df.columns[-1]]

    # temper_df.to_sql('temperature', connection, if_exists='replace')
    # connection.close()
    # temper_df.set_index("Stations_id")
    station_year_df = temper_df.loc[temper_df.Stations_id == station]

    data = station_year_df.iloc[:, 3:].to_dict()
    names = list(data.keys())
    values = list(data.values())
    v = []
    for i in values:
        x = list(i.values())
        v.append(x[0])
    plt.plot(range(len(data)), v)
    for i, j in zip(names, v):
        plt.annotate(str(j), xy=(names.index(i), j))
    plt.xticks(ticks=list(range(13)), labels=names)
    plt.yticks(list(range(int(min(v)), int(max(v))+2)))
    plt.grid(True)
    plt.title("Mean Temperature Between 1991-2020", loc="center")
    plt.show()

# row.plot(kind='bar')
# plt.show()
if __name__ == "__main__":
    process(station_id)
