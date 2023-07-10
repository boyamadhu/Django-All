from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def sab(request):
    d=[1,2,3,4]
    return render(request,'app1.html',d)