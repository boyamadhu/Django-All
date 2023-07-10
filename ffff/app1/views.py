from django.shortcuts import render
from django.http import HttpResponse
from app1.models import *
# Create your views here.

def sam(request):
    top=input('eneter topic : ')
    TO=topic.objects.get_or_create(topic_name=top)[0]
    TO.save()

    nam=input('enter name : ')
    urls=input('eneter url : ')
    WO=webpage.objects.get_or_create(topic_name=TO,name=nam,url=urls)[0]
    WO.save()

    dat=input('enetr date : ')
    aut=input('eneter author : ')
    AO=access.objects.get_or_create(name=WO,author=aut,date=dat)[0]
    AO.save()

    d={'display':access.objects.all()}
    return render(request,'sam.html',d)

def display(request):
    d={'display':access.objects.all()}
    return render(request,'sam.html',d)