# Generated by Django 4.2.6 on 2023-10-10 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0004_rename_name_measurement_sensor_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='measurement',
            old_name='sensor_id',
            new_name='sensor',
        ),
    ]
