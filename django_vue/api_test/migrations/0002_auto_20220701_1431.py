# Generated by Django 3.2 on 2022-07-01 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_test', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='popular_movies',
            name='location',
        ),
        migrations.RemoveField(
            model_name='popular_movies',
            name='moive_id',
        ),
        migrations.RemoveField(
            model_name='popular_movies',
            name='moive_url',
        ),
        migrations.RemoveField(
            model_name='popular_movies',
            name='name',
        ),
        migrations.RemoveField(
            model_name='popular_movies',
            name='photo_url',
        ),
        migrations.RemoveField(
            model_name='popular_movies',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='popular_movies',
            name='type',
        ),
        migrations.AddField(
            model_name='popular_movies',
            name='ACTORS',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='popular_movies',
            name='ACTOR_IDS',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='popular_movies',
            name='ALIAS',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='popular_movies',
            name='COVER',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='popular_movies',
            name='DIRECTORS',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='popular_movies',
            name='DIRECTOR_IDS',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='popular_movies',
            name='DOUBAN_SCORE',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='popular_movies',
            name='DOUBAN_VOTES',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='popular_movies',
            name='GENRES',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='popular_movies',
            name='IMDB_ID',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='popular_movies',
            name='LANGUAGES',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='popular_movies',
            name='MINS',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='popular_movies',
            name='MOVIE_ID',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='popular_movies',
            name='NAME',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='popular_movies',
            name='OFFICIAL_SITE',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='popular_movies',
            name='REGIONS',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='popular_movies',
            name='RELEASE_DATE',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='popular_movies',
            name='SLUG',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='popular_movies',
            name='STORYLINE',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='popular_movies',
            name='TAGS',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='popular_movies',
            name='YEAR',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
