# Generated by Django 4.1.10 on 2023-11-09 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geomanager', '0029_rasterfilelayer_auto_ingest_from_directory'),
    ]

    operations = [
        migrations.DeleteModel(
            name='GeoStationSettings',
        ),
    ]
