from django.db import models


class Station(models.Model):
    stations_id = models.AutoField(db_column='Stations_id', primary_key=True)
    stationsname = models.TextField(db_column='Stationsname', blank=True, null=True)
    geogr_breite = models.FloatField(db_column='geogr. Breite', blank=True, null=True)
    geogr_laenge = models.FloatField(db_column='geogr. Laenge', blank=True, null=True)
    stationshoehe = models.FloatField(db_column='Stationshoehe', blank=True, null=True)
    bundesland = models.TextField(db_column='Bundesland', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'station'


class Temperature(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    stations = models.ForeignKey(
        Station, models.DO_NOTHING, db_column='Stations_id', to_field='', blank=True, null=True
    )
    bezugszeitraum = models.TextField(db_column='Bezugszeitraum', blank=True, null=True)
    datenquelle = models.IntegerField(db_column='Datenquelle', blank=True, null=True)
    jan_field = models.FloatField(db_column='Jan.', blank=True, null=True)
    feb_field = models.FloatField(db_column='Feb.', blank=True, null=True)
    marz = models.FloatField(db_column='März', blank=True, null=True)
    apr_field = models.FloatField(db_column='Apr.', blank=True, null=True)
    mai = models.FloatField(db_column='Mai', blank=True, null=True)
    jun_field = models.FloatField(db_column='Jun.', blank=True, null=True)
    jul_field = models.FloatField(db_column='Jul.', blank=True, null=True)
    aug_field = models.FloatField(db_column='Aug.', blank=True, null=True)
    sept_field = models.FloatField(db_column='Sept.', blank=True, null=True)
    okt_field = models.FloatField(db_column='Okt.', blank=True, null=True)
    nov_field = models.FloatField(db_column='Nov.', blank=True, null=True)
    dez_field = models.FloatField(db_column='Dez.', blank=True, null=True)
    jahr = models.FloatField(db_column='Jahr', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temperature'
