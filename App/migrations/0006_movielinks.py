# Generated by Django 3.2 on 2021-05-08 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_auto_20210420_1745'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movielinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movieId', models.IntegerField()),
                ('imdbId', models.IntegerField()),
                ('tmdbId', models.FloatField()),
            ],
        ),
    ]
