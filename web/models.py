from django.db import models


class Station(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    province = models.TextField(blank=True, null=True)


class Temperature(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    station = models.ForeignKey(Station, models.DO_NOTHING)
    period = models.TextField(blank=True, null=True)
    quality = models.IntegerField(blank=True, null=True)
    jan = models.FloatField(blank=True, null=True)
    feb = models.FloatField(blank=True, null=True)
    mar = models.FloatField(blank=True, null=True)
    apr = models.FloatField(blank=True, null=True)
    may = models.FloatField(blank=True, null=True)
    jun = models.FloatField(blank=True, null=True)
    jul = models.FloatField(blank=True, null=True)
    aug = models.FloatField(blank=True, null=True)
    sep = models.FloatField(blank=True, null=True)
    oct = models.FloatField(blank=True, null=True)
    nov = models.FloatField(blank=True, null=True)
    dec = models.FloatField(blank=True, null=True)
    year = models.FloatField(blank=True, null=True)
