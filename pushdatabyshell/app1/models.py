from django.db import models

# Create your models here.


class institute(models.Model):
    institute_name=models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.institute_name

class trainers_data(models.Model):
    institute_name=models.ForeignKey(institute,on_delete=models.CASCADE)
    trainer_name=models.CharField(max_length=100,primary_key=True)
    trainer_sal=models.IntegerField()
    trainer_DOB=models.DateField()

    def __str__(self):
        return self.trainer_name

class trainer_sal_details(models.Model):
    trainer_name=models.ForeignKey(trainers_data, on_delete=models.CASCADE)
    trainer_month_sal=models.IntegerField()
    trainer_year_sal=models.IntegerField()

    def __str__(self):
        return str(self.trainer_month_sal)


