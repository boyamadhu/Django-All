from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def sab(request):
    d={'a':10,'b':20,'c':30,}
    return render(request,'condition.html',d)
    # return HttpResponse('RRR got oskar award')