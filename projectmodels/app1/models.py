from django.db import models

# Create your models here.

class movies(models.Model):
    movie_name=models.CharField(max_length=100, primary_key=True)
    movie_rating=models.IntegerField()

    def __str__(self):
        return self.movie_name
    

    
class actors(models.Model):
    movies=models.ForeignKey(movies, on_delete=models.CASCADE)
    hero=models.CharField(max_length=100)
    heroine=models.CharField(max_length=100)


