from django.db import models

class Action_adventure_model(models.Model):
        movie_id = models.IntegerField(unique=True)
        title = models.CharField(unique=True,max_length=20)
        released_date = models.CharField(unique=True,max_length=10)
        overview = models.CharField(unique=True,max_length=200)
        poster_path = models.CharField(unique=True,max_length=50)
        genres = models.CharField(unique=True,max_length=10)



