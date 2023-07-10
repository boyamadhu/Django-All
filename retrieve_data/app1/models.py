from django.db import models

# Create your models here.

class sport(models.Model):
    sport_name=models.CharField(max_length=100,primary_key=True)
    no_of_players=models.IntegerField()

    def __str__(self):
        return self.sport_name
    
class players(models.Model):
    sport_name=models.ForeignKey(sport,on_delete=models.CASCADE)
    pname=models.CharField(max_length=100,)
    
    def __str__(self):
        return self.pname

class players_data(models.Model):
    pname=models.ForeignKey(players,on_delete=models.CASCADE)
    page=models.IntegerField()
    pgender=models.CharField(max_length=100,)

    def __str__(self):
        return self.pgender