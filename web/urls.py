from django.urls import path
from django.views.generic import TemplateView

from web import views

urlpatterns = [
    path("", views.index, name="bundes-list"),
    path("chart/<int:id>/", views.chart, name="chart"),
    path("chart_by_name", views.chart_by_name, name="chart_by_name"),
]
