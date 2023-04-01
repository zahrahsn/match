from django.urls import path
from django.views.generic import TemplateView

from web import views

urlpatterns = [
    path("", views.index, name="bundes-list"),
    path("chart/<int:id>/", views.chart, name="chart"),
]
