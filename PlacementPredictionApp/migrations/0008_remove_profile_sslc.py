# Generated by Django 3.2.18 on 2023-04-04 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PlacementPredictionApp', '0007_auto_20230404_1502'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='Sslc',
        ),
    ]