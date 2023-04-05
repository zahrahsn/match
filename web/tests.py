import pytest
from _pytest.fixtures import fixture

from web.models import Temperature
from web.views import plotter, read_temp_data, read_stations


@fixture
def temperature():
    temp = Temperature()
    temp.jan = 1.2
    temp.feb = 2.3
    temp.mar = 3.4
    temp.apr = 4.5
    temp.may = -1
    temp.jun = 3.4
    temp.jul = 5.6
    temp.aug = 6.7
    temp.sep = 6.8
    temp.oct = 7.9
    temp.nov = 3.2
    temp.dec = 1
    temp.year = 5
    return temp


def test_plot(temperature):
    """
    Testing that plotter raises no exceptions
    :param temperature: The sample Temperature object
    """
    plotter(temperature, 'test_province', 'test_station')


@pytest.mark.django_db
def test_read_station():
    df = read_stations(2)
    assert df is not None
