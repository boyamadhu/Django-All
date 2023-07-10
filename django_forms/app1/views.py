from django.shortcuts import render
from app1.forms import *
# Create your views here.
from django.http import HttpResponse

def student_info(request):
    SO=student()
    d={'SO':SO}
    if request.method=='POST':
        SO1=student(request.POST)
        if SO1.is_valid():
            return HttpResponse(str(SO1.cleaned_data))
    return render(request,'student.html',d)