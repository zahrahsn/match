import base64
from itertools import groupby

from django.shortcuts import render

from web.models import Station, Temperature
import matplotlib.pyplot as plt
import numpy as np
import io


def index(request):
    queryset = list(Station.objects.all().order_by('bundesland').values())
    provinces = []
    for key, group in groupby(queryset, lambda x: x['bundesland']):
        provinces.append(
            {
                'name': key,
                'stations': list(group)
            }
        )
    context = {"provinces": provinces}
    return render(request, 'web/station_list.html', context=context)


def chart(request, id):
    temp = Temperature.objects.get(stations__stations_id=id)
    station_name= Station.objects.get(stations_id=id).stationsname
    plot = plotter(temp, station_name)
    context = {'data': plot}
    return render(request, 'web/chart.html', context=context)


def plotter(temp: Temperature, station_name):
    names = ['Jan.', 'Feb.', 'März.', 'Apr.', 'Mai', 'Jun.', 'Jul.', 'Aug.', 'Sept.', 'Okt.', 'Nov.', 'Dez.']
    values = np.array(
        [
            temp.jan_field,
            temp.feb_field,
            temp.marz,
            temp.apr_field,
            temp.mai,
            temp.jun_field,
            temp.jul_field,
            temp.aug_field,
            temp.sept_field,
            temp.okt_field,
            temp.nov_field,
            temp.dez_field
        ]
    )

    plt.plot(names, values, marker='o')
    for i, j in zip(names, values):
        plt.annotate(str(j), xy=(names.index(i), j))
    plt.axhline(y=temp.jahr, color='r', linestyle='-')
    plt.text(0.1, temp.jahr + 0.2, f'Jahr Mean: {temp.jahr}')
    plt.grid(True)
    plt.title(f"Mean Temperature of {station_name} Between 1991-2020", loc="center")
    bio = io.BytesIO()
    plt.savefig(bio, format="png")
    plt.close()
    bio.seek(0)
    return base64.b64encode(bio.read()).decode()
