# Generated by Django 4.1.10 on 2023-11-14 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geomanager', '0031_remove_geomanagersettings_cap_auto_refresh_interval_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='rasterfilelayer',
            name='auto_ingest_nc_data_variable',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Data variable for netCDF data auto ingest'),
        ),
    ]
