from django.shortcuts import render
from app1.forms import *
from django.http import HttpResponse
# Create your views here.

def insert_topic(request):
    TF=TopicForm()
    d={'TF':TF}

    if request.method=='POST':
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('data is inserted successfully')
    return render(request,'insert_topic.html',d)


def insert_webpage(request):
    WF=WebpageForm()
    d={'WF':WF}

    if request.method=='POST':
        WFD=WebpageForm(request.POST)
        if WFD.is_valid():
            WFD.save()
            return HttpResponse('data is inserted successfully')
    return render(request,'insert_webpage.html',d)

def insert_access(request):
    AF=AccessForm()
    d={'AF':AF}

    if request.method=='POST':
        AFD=AccessForm(request.POST)
        if AFD.is_valid():
            AFD.save()
            return HttpResponse('data is inserted successfully')
    return render(request,'insert_access.html',d)

def form1(request):
    WF=Form_1()
    d={'WF':WF}
    return render(request,'insert_webpage.html',d)