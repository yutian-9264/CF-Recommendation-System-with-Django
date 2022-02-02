from django.db import models

# Create your models here.
class User(models.Model):
    Username=models.CharField(max_length=150)
    Pwd=models.CharField(max_length=150)
    Email=models.CharField(max_length=150)

class MovieData(models.Model):
    Movieid=models.CharField(max_length=200)
    Title=models.CharField(max_length=200)
    Userid=models.CharField(max_length=200)
    rating=models.IntegerField()

class data_movies(models.Model):
    # id=models.IntegerField(max_length=200)
    movieId=models.CharField(max_length=200)
    title=models.CharField(max_length=200)
    genres=models.CharField(max_length=200)

class Movieratings(models.Model):
    user = models.ForeignKey(User,related_name='user_movieratings',on_delete=models.CASCADE)
    moviename=models.CharField(max_length=200)
    movieindex=models.IntegerField()
    userratings=models.IntegerField()

class Movielinks(models.Model):
    movieId=models.IntegerField(null=True)
    imdbId=models.IntegerField(null=True)
    tmdbId=models.FloatField(null=True)
