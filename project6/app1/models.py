from django.db import models

# Create your models here.

class Country(models.Model):
    cname=models.CharField(max_length=100)
    code=models.IntegerField()

class capital(models.Model):
    cname=models.ForeignKey(Country,on_delete=models.CASCADE,unique=True)
    code=models.IntegerField()