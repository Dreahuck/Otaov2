# Generated by Django 2.2.24 on 2021-08-28 10:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('HomeManager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personne',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 28, 10, 3, 17, 267729, tzinfo=utc)),
        ),
    ]