# Generated by Django 3.2.9 on 2021-11-02 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_auto_20211102_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='category',
            field=models.CharField(choices=[('action', 'ACTION'), ('comedy', 'COMEDY'), ('drama', 'DRAMA'), ('fantasy', 'FANTASY'), ('horror', 'HORROR'), ('kids', 'KIDS'), ('romance', 'ROMANCE'), ('science-fiction', 'SCIENCE-FICTION')], max_length=15),
        ),
    ]
