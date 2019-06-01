# Generated by Django 2.2.1 on 2019-06-01 15:09

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllSweepsV02',
            fields=[
                ('ogc_fid', models.AutoField(primary_key=True, serialize=False)),
                ('reportdate', models.TextField(blank=True, null=True)),
                ('cleantype', models.TextField(blank=True, null=True)),
                ('location', models.TextField(blank=True, null=True)),
                ('maintenanceproject', models.TextField(blank=True, null=True)),
                ('green_space', models.TextField(blank=True, db_column='green.space', null=True)),
                ('excessive_heat_cold', models.TextField(blank=True, db_column='excessive.heat.cold', null=True)),
                ('estimated_geocode', models.TextField(blank=True, db_column='estimated.geocode', null=True)),
                ('polygon_as_point_field', models.TextField(blank=True, db_column='polygon.as.point?', null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('long', models.FloatField(blank=True, null=True)),
                ('accuracy', models.TextField(blank=True, null=True)),
                ('checked_aurelia_2018_09_2018_11_field', models.TextField(blank=True, db_column='checked_aurelia(2018_09/2018_11)', null=True)),
                ('flag_alex', models.FloatField(blank=True, null=True)),
                ('row_num_alex', models.FloatField(blank=True, null=True)),
                ('still_need_checked_y_n_dan', models.TextField(blank=True, db_column='still need checked (y/n)_dan', null=True)),
                ('changed_y_n_dan', models.TextField(blank=True, db_column='changed(y/n)_dan', null=True)),
                ('repeats_not_matching_dan', models.FloatField(blank=True, db_column='repeats not matching?_dan', null=True)),
                ('wkb_geometry', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326)),
            ],
            options={
                'db_table': 'all_sweeps_v02',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RlisNeighborhoods',
            fields=[
                ('ogc_fid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, null=True)),
                ('sum_area', models.FloatField(blank=True, null=True)),
                ('sum_sqmile', models.FloatField(blank=True, null=True)),
                ('wkb_geometry', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326)),
            ],
            options={
                'db_table': 'rlis_neighborhoods',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('metadata_endpoint', models.URLField()),
                ('creator', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('value', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Layer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('version', models.IntegerField()),
                ('data_endpoint', models.URLField()),
                ('metadata_endpoint', models.URLField()),
                ('rating', models.CharField(choices=[('OP', 'Open'), ('CU', 'Curated'), ('BL', 'Blocked')], default='OP', max_length=2)),
                ('visualization_type', models.CharField(choices=[('SM', 'ScatterPlotMap'), ('TX', 'Text'), ('CM', 'ChoroplethMap')], default='SM', max_length=2)),
                ('creator', models.CharField(max_length=50)),
                ('package', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Package')),
                ('tags', models.ManyToManyField(to='api.Tag')),
            ],
        ),
    ]
