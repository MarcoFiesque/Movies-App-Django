# Generated by Django 3.2.9 on 2021-11-02 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0012_movie_views_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='trailer',
            field=models.URLField(blank=True),
        ),
    ]
