# Generated by Django 3.2.9 on 2021-11-02 23:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0013_movie_trailer'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 11, 2, 23, 38, 8, 765608, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
