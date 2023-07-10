from django.shortcuts import render
from app1.models import *
# Create your views here.
from django.http import HttpResponse

def insert_sport(request):
    sname=input('enter sport name : ')
    sno=int(input('enter no of players : '))
    SO=sport.objects.get_or_create(sport_name=sname,no_of_players=sno)[0]
    SO.save()
    return HttpResponse('inserted into sport table successfully')

def insert_players(request):
    sname=input('enter sport name : ')
    sno=int(input('enter no of players'))
    SO=sport.objects.get_or_create(sport_name=sname,no_of_players=sno)[0]
    SO.save()
    playername=input('enter player name : ')
    PO=players.objects.get_or_create(sport_name=SO, pname=playername)[0]
    PO.save()
    return HttpResponse('inserted into sport table successfully')

def insert_players_data(request):
    sname=input('enter sport name : ')
    sno=int(input('enter no of players'))
    SO=sport.objects.get_or_create(sport_name=sname,no_of_players=sno)[0]
    SO.save()
    playername=input('enter player name : ')
    PO=players.objects.get_or_create(sport_name=SO, pname=playername)[0]
    PO.save()

    i1=int(input('enter player age  :'))
    i2=input('enter player gender : ')
    PD=players_data.objects.get_or_create(pname=PO,page=i1,pgender=i2)
    return HttpResponse('inserted into sport table successfully')

def retrieve_sport(request):
    TO=sport.objects.all()
    d={'sport':TO}
    return render(request,'first.html',d)

def retrieve_players(request):
    TO=players.objects.all()
    d={'player':TO}
    return render(request,'players.html',d)

def retrieve_players_data(request):
    TO=players_data.objects.all()
    d={'players':TO}
    return render(request,'players_data.html',d)