# Generated by Django 3.2 on 2021-05-08 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_movielinks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movielinks',
            name='imdbId',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='movielinks',
            name='movieId',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='movielinks',
            name='tmdbId',
            field=models.FloatField(null=True),
        ),
    ]
