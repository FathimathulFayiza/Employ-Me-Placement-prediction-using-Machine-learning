# Generated by Django 3.2.18 on 2023-04-05 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PlacementPredictionApp', '0012_auto_20230404_1727'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerformanceUpdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Field', models.CharField(default=None, max_length=50)),
                ('userId', models.IntegerField(default=None)),
                ('flag', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'PerformanceUpdate',
            },
        ),
    ]