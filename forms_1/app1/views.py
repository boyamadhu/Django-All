from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def sam(request):

    if request.method=='POST':
        name=request.POST['un']
        pw=request.POST['pw']
        print(name)
        print(pw)
        return HttpResponse('Data is sented successfully')
    return render (request,'form.html')