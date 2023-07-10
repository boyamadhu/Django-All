from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def sam(request):
    d=[1,2,3,4]
    return render(request,'app2.html',d)
