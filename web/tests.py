from django.test import TestCase
from matplotlib import pyplot as plt
import numpy as np


#
# from web.preparing import process
#
#
# def test_process():
#     process(435)


def test_plot():
    names = ['Jan.', 'Feb.', 'März.', 'Apr.', 'Mai', 'Jun.', 'Jul.', 'Aug.', 'Sept.', 'Okt.', 'Nov.', 'Dez.']
    values = np.array([1.2, 2.3, 3.4, 4.5, -1, 3.4, 5.6, 6.7, 6.8, 7.9, 3.2, 1])
    plt.plot(names, values, marker='o')
    for i, j in zip(names, values):
        plt.annotate(str(j), xy=(names.index(i), j))
    plt.axhline(y=6, color='r', linestyle='-')
    plt.grid(True)
    plt.title("Mean Temperature Between 1991-2020", loc="center")
    plt.show()
