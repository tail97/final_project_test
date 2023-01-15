from django.db import models

class Action_adventure_model(models.Model):
        movie_id = models.IntegerField(unique=True)
        title = models.CharField(unique=True,max_length=20)
        released_date = models.CharField(unique=True,max_length=10)
        overview = models.CharField(unique=True,max_length=200)
        poster_path = models.CharField(unique=True,max_length=50)
        genres = models.CharField(unique=False,max_length=10)
    
class Comedy_model(models.Model):
        movie_id = models.IntegerField(unique=True)
        title = models.CharField(unique=True,max_length=20)
        released_date = models.CharField(unique=True,max_length=10)
        overview = models.CharField(unique=True,max_length=200)
        poster_path = models.CharField(unique=True,max_length=50)
        genres = models.CharField(unique=False,max_length=10)   

class Drama_Famile_model(models.Model):
        movie_id = models.IntegerField(unique=True)
        title = models.CharField(unique=True,max_length=20)
        released_date = models.CharField(unique=True,max_length=10)
        overview = models.CharField(unique=True,max_length=200)
        poster_path = models.CharField(unique=True,max_length=50)
        genres = models.CharField(unique=False,max_length=10)

class Fantasy_SF_model(models.Model):
        movie_id = models.IntegerField(unique=True)
        title = models.CharField(unique=True,max_length=20)
        released_date = models.CharField(unique=True,max_length=10)
        overview = models.CharField(unique=True,max_length=200)
        poster_path = models.CharField(unique=True,max_length=50)
        genres = models.CharField(unique=False,max_length=10)

class TVmovie_Animation_Music_model(models.Model):
        movie_id = models.IntegerField(unique=True)
        title = models.CharField(unique=True,max_length=20)
        released_date = models.CharField(unique=True,max_length=10)
        overview = models.CharField(unique=True,max_length=200)
        poster_path = models.CharField(unique=True,max_length=50)
        genres = models.CharField(unique=False,max_length=10)

class Thriller_Fear_model(models.Model):
        movie_id = models.IntegerField(unique=True)
        title = models.CharField(unique=True,max_length=20)
        released_date = models.CharField(unique=True,max_length=10)
        overview = models.CharField(unique=True,max_length=200)
        poster_path = models.CharField(unique=True,max_length=50)
        genres = models.CharField(unique=False,max_length=10)

class Romance_model(models.Model):
        movie_id = models.IntegerField(unique=True)
        title = models.CharField(unique=True,max_length=20)
        released_date = models.CharField(unique=True,max_length=10)
        overview = models.CharField(unique=True,max_length=200)
        poster_path = models.CharField(unique=True,max_length=50)
        genres = models.CharField(unique=False,max_length=10)

class Youtube_for_sadness(models.Model):
        video_name = models.CharField(max_length=30)
        video_url= models.CharField(max_length=30)
        video_date= models.CharField(max_length=20)
        video_thumbnails=models.CharField(null= False, max_length=30)


class Youtube_For_Pleasure(models.Model):
        video_name = models.CharField(max_length=30)
        video_url= models.CharField(max_length=30)
        video_date= models.CharField(max_length=20)
        video_thumbnails=models.CharField(max_length=30)

class Youtube_For_Terror(models.Model):
        video_name = models.CharField(max_length=30)
        video_url= models.CharField(max_length=30)
        video_date= models.CharField(max_length=20)
        video_thumbnails=models.CharField(max_length=30)

class Youtube_For_Loathing(models.Model):
        video_name = models.CharField(max_length=30)
        video_url= models.CharField(max_length=30)
        video_date= models.CharField(max_length=20)
        video_thumbnails=models.CharField(max_length=30)

class Youtube_For_Angry(models.Model):
        video_name = models.CharField(max_length=30)
        video_url= models.CharField(max_length=30)
        video_date= models.CharField(max_length=20)
        video_thumbnails=models.CharField(max_length=30)

class Youtube_For_Expect(models.Model):
        video_name = models.CharField(max_length=30)
        video_url= models.CharField(max_length=30)
        video_date= models.CharField(max_length=20)
        video_thumbnails=models.CharField(max_length=30)

class Youtube_For_Shock(models.Model):
        video_name = models.CharField(max_length=30)
        video_url= models.CharField(max_length=30)
        video_date= models.CharField(max_length=20)
        video_thumbnails=models.CharField(max_length=30)

class Youtube_For_Calmness(models.Model):
        video_name = models.CharField(max_length=30)
        video_url= models.CharField(max_length=30)
        video_date= models.CharField(max_length=20)
        video_thumbnails=models.CharField(max_length=30)