import pandas as pd
from django.shortcuts import render
from web.models import Station, Temperature
from itertools import groupby
import matplotlib.pyplot as plt
import numpy as np
import io
import base64

base_url = 'https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/multi_annual/mean_91-20/'
temperature_url = base_url + 'Temperatur_1991-2020.txt'
stations_url = base_url + 'Temperatur_1991-2020_Stationsliste.txt'


def index(request):
    """
    Landing page.
     - Retrieves all stations' list
     (attempts to read from database. If does not exist in db, fetches from "stations_url" and stores in db.)
     - Groups them by Province's name
     - Sends the grouped stations to the template
     - Renders the template
    :param request: The http request.
    :return: The rendered 'stations_list' template
    """
    stations = list(Station.objects.all().order_by('province'))
    if len(stations) == 0:
        stations = read_stations()
    provinces = []
    for key, group in groupby(stations, lambda x: x.province):
        provinces.append(
            {
                'name': key,
                'stations': list(group)
            }
        )
    context = {"provinces": provinces}
    return render(request, 'web/station_list.html', context=context)


def chart(request, id):
    """
    Chart view
     - Receives the id of station from the url
     - retrieves the temperature object
     (attempts to read from database. If does not exist in db, fetches from "temperature_url" and stores in db.)
     - renders chart template with base64-encoded plot
    :param request: The http request
    :param id: The station id
    :return: The rendered 'chart' template
    """
    try:
        temp = Temperature.objects.get(station__id=id)
    except Temperature.DoesNotExist:
        temp = read_temp_data(id)
    plot = plotter(temp, temp.station.province, temp.station.name)
    context = {'data': plot}
    return render(request, 'web/chart.html', context=context)


def read_temp_data(station_id) -> Temperature:
    """
    Reads temperature data from 'temperature_url'
    creates an object of temperature model and saves retrieved data in it
    saves the temperature object in database
    :param station_id: the station id
    :return: saved temperature object.
    """
    station = Station.objects.get(id=station_id)
    temper_df = pd.read_csv(temperature_url, delimiter=';', encoding="ISO-8859-1")
    del temper_df[temper_df.columns[-1]]
    temper_df.columns = [
        'st_id', 'period', 'quality', 'jan', 'feb', 'mar',
        'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct',
        'nov', 'dec', 'year'
    ]
    data = temper_df.loc[temper_df.st_id == station_id].iloc[0, :]
    temp = Temperature()
    temp.station = station
    temp.period = data.period.strip()
    temp.quality = data.quality
    temp.jan = data.jan
    temp.feb = data.feb
    temp.mar = data.mar
    temp.apr = data.apr
    temp.may = data.may
    temp.jun = data.jun
    temp.jul = data.jul
    temp.aug = data.aug
    temp.sep = data.sep
    temp.oct = data.oct
    temp.nov = data.nov
    temp.dec = data.dec
    temp.year = data.year
    temp.save()
    return temp


def read_stations():
    """
    If the stations table is empty, fetches the stations data of Germany from 'stations_url'
    and stores them in database.
    :return: the saved stations list.
    """
    df = pd.read_csv(
        stations_url,
        delimiter=';',
        encoding="ISO-8859-1"
    )
    del df[df.columns[-1]]
    df.columns = ['id', 'st_name', 'lat', 'long', 'height', 'province']
    stations = []
    for idx, st in df.iterrows():
        obj = Station()
        obj.id = st.id
        obj.name = st.st_name.strip()
        obj.province = st.province.strip()
        obj.latitude = st.lat
        obj.longitude = st.long
        obj.height = st.height
        obj.save()
        stations.append(obj)
    return stations


def plotter(temp: Temperature, province, station_name):
    """
    Plots the temperature data using matplotlib
    :param province: the province name
    :param temp: the temperature object
    :param station_name: the station name
    :return: base-64 encoded version of plot
    """
    names = ['Jan.', 'Feb.', 'Mar.', 'Apr.', 'May.', 'Jun.', 'Jul.', 'Aug.', 'Sep.', 'Oct.', 'Nov.', 'Dec.']
    values = np.array(
        [
            temp.jan,
            temp.feb,
            temp.mar,
            temp.apr,
            temp.may,
            temp.jun,
            temp.jul,
            temp.aug,
            temp.sep,
            temp.oct,
            temp.nov,
            temp.dec
        ]
    )

    plt.plot(names, values, marker='o')
    for i, j in zip(names, values):
        plt.annotate(str(j), xy=(names.index(i), j))
    plt.axhline(y=temp.year, color='r', linestyle='-')
    plt.text(0.1, temp.year + 0.2, f'Year Mean: {temp.year}')
    plt.grid(True)
    plt.title(f"Mean Temperature of '{station_name}' in {province}, Between 1991-2020", loc="center")
    bio = io.BytesIO()
    plt.savefig(bio, format="png")
    plt.close()
    bio.seek(0)
    return base64.b64encode(bio.read()).decode()
