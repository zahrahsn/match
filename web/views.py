from itertools import groupby

from django.shortcuts import render

from web.models import Station


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
    context = {"province": provinces}
    return render(request, 'web/station_list.html', context=context)

#
