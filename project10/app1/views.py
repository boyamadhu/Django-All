from django.shortcuts import render
from django.http import HttpResponse
from app1.models import *
# Create your views here.

def sam(request):
    if request.method=='POST':
        tn=request.POST['topic']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        return HttpResponse('Data has been submitted successfully')
    return render(request,'form.html')

def sab(request):
    if request.method=='POST':
        tn=request.POST['topic']
        n=request.POST['name']
        ur=request.POST['url']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=ur)[0]
        WO.save()
        return HttpResponse('Data has been submitted successfully')
    return render(request,'form.html')

def ram(request):
    TO=Topic.objects.all()
    d={'topic':TO}
    if request.method=='POST':
        tn=request.POST['topic']
        n=request.POST['name']
        ur=request.POST['url']
        TO=Topic.objects.get(topic_name=tn)
        WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=ur)[0]
        WO.save()
        return HttpResponse('data is inserted')
    return render (request,'first.html',d)