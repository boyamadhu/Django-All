from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
def sab(request):
    d={'name':'madhu', 'age':120}
    return render(request,'first.html',context=d)