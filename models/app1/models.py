from django.db import models

# Create your models here.


class Sport(models.Model):
    Sport_Name=models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.Sport_Name

class Webpage(models.Model):
    Sport_Name=models.ForeignKey(Sport,on_delete=models.CASCADE)
    Name=models.CharField(max_length=100)
    Url=models.CharField(max_length=100)

    def __str__(self):
        return self.Name

    
class Access_Records(models.Model):
    Name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    Author=models.CharField(max_length=100,)
    Date=models.DateField()

    def __str__(self):
        return self.Author

    