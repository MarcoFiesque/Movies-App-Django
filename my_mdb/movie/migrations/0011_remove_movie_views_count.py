# Generated by Django 3.2.9 on 2021-11-02 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0010_movie_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='views_count',
        ),
    ]