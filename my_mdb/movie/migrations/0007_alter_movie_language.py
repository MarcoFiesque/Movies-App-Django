# Generated by Django 3.2.9 on 2021-11-02 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_alter_movie_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='language',
            field=models.CharField(choices=[('english', 'ENGLISH'), ('french', 'FRENCH')], max_length=8),
        ),
    ]
