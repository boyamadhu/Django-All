from django.shortcuts import render
from app1.models import *
from django.http import HttpResponse
# Create your views here.

def insert(request):
    n=input('enter name of the institute : ')
    IO=institute.objects.get_or_create(institute_name=n)[0]
    IO.save()
    return HttpResponse('inserted institute name successfully')

def insert_trainers_data(request):
    n=input('enter name of the institute : ')
    IO=institute.objects.get_or_create(institute_name=n)[0]
    IO.save()
    tname=input('enter trainer name : ')
    tsal=input('enter trainer salary : ')
    tdob=input('enter trainer dob : ')
    TO=trainers_data.objects.get_or_create(institute_name=IO,trainer_name=tname,trainer_sal=tsal,trainer_DOB=tdob)[0]
    TO.save()
    return HttpResponse('inserted institute name successfully')

def insert_trainers_sal(request):
    n=input('enter name of the institute : ')
    IO=institute.objects.get_or_create(institute_name=n)[0]
    IO.save()
    tname=input('enter trainer name : ')
    tsal=input('enter trainer salary : ')
    tdob=input('enter trainer dob : ')
    TO=trainers_data.objects.get_or_create(institute_name=IO,trainer_name=tname,trainer_sal=tsal,trainer_DOB=tdob)[0]
    TO.save()
    msal=int(input('enter trainer month sal'))
    ysal=int(input('enter trainer year sal'))
    SO=trainer_sal_details.objects.get_or_create(trainer_name=TO,trainer_month_sal=msal,trainer_year_sal=ysal)[0]
    SO.save()
    return HttpResponse('inserted trainers sal successfully')



