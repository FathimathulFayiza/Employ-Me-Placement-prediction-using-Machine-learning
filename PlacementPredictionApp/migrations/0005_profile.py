# Generated by Django 3.2.18 on 2023-04-04 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PlacementPredictionApp', '0004_student_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sslc', models.CharField(default=None, max_length=30)),
                ('StudentId', models.IntegerField(default=None)),
                ('puc', models.CharField(default=None, max_length=30)),
                ('be_cgpa', models.CharField(default=None, max_length=30)),
                ('deploma', models.CharField(default=None, max_length=30)),
                ('be_percentage', models.CharField(default=None, max_length=30)),
                ('backlog', models.CharField(default=None, max_length=30)),
                ('cocubes_total', models.CharField(default=None, max_length=30)),
                ('aptitude', models.CharField(default=None, max_length=30)),
                ('english', models.CharField(default=None, max_length=30)),
                ('quantitative', models.CharField(default=None, max_length=30)),
                ('compuer_fundamental', models.CharField(default=None, max_length=30)),
                ('analytical', models.CharField(default=None, max_length=30)),
                ('coding', models.CharField(default=None, max_length=30)),
                ('domain', models.CharField(default=None, max_length=30)),
                ('wrtten_enhlish', models.CharField(default=None, max_length=30)),
                ('flag', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'Profile',
            },
        ),
    ]
