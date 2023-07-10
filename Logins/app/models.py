from django.db import models
from django import forms
# Create your models here.
class Login(models.Model):
    Username=models.CharField(max_length=100)
    Password=models.IntegerField()
    Re_EnterPassword=models.IntegerField()

    def __str__(self):
        return self.Username

class Register(models.Model):
    Username=models.CharField(max_length=100)
    Password=models.IntegerField()
    
    def __str__(self):
        return str(self.Register_ID)

    

class Student(models.Model):
    Sid=models.IntegerField(primary_key=True)
    Sname=models.CharField(max_length=20)
    Sage=models.IntegerField()
    Semail=models.EmailField()
    JDate=models.DateField()

    def __str__(self):
        return str(self.Sid)