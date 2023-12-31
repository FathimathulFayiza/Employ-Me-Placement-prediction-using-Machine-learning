# Generated by Django 3.2.18 on 2023-04-03 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=30)),
                ('username', models.CharField(default=None, max_length=30)),
                ('contact', models.CharField(default=None, max_length=30)),
                ('email', models.CharField(default=None, max_length=50)),
                ('age', models.CharField(default=None, max_length=30)),
                ('address', models.CharField(default=None, max_length=250)),
                ('gender', models.CharField(default=None, max_length=10)),
                ('fatherName', models.CharField(default=None, max_length=50)),
                ('branch', models.CharField(default=None, max_length=250)),
                ('year', models.CharField(default=None, max_length=250)),
                ('Image', models.CharField(default=None, max_length=50)),
                ('is_register', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'Student',
            },
        ),
    ]
