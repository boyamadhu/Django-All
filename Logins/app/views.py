from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
from app.forms import *
# Create your views here.
def Login_Form(request):
    SFO=LoginForm()
    d={'SFO':SFO}
    if request.method=='POST':
        SO=LoginForm(request.POST)
        if SO.is_valid():
            TO=Login.objects.get_or_create(Username=SO.cleaned_data["Username"],Password=SO.cleaned_data['Password'],Re_EnterPassword=SO.cleaned_data['Re_EnterPassword'])[0]
            TO.save()
            return HttpResponse(str(SO.cleaned_data))
        else:
            return HttpResponse("Password is not matched")
    return render(request,'Login_Form.html',d)

def Reister_Form(request):
    RFO=RegisterForm()
    d={"RFO":RFO}
    if request.method=='POST':
        RO=LoginForm(request.POST)
        if RO.is_valid():
            return HttpResponse(str(RO.cleaned_data))
        else:
            return HttpResponse("Password is not matched")
    

    return render(request,"Reister_Form.html",d)
 

def Data_Student(request):
    SO=StudentForm()
    d={'SO':SO}
    if request.method=='POST':
        SL=StudentForm(request.POST)
        if SL.is_valid():
            TO=Student.objects.get_or_create(Sid=SL.cleaned_data["Sid"],Sname=SL.cleaned_data['Sname'],Sage=SL.cleaned_data['Sage'],Semail=SL.cleaned_data['Semail'],JDate=SL.cleaned_data['JDate'])[0]
            TO.save()
            return HttpResponse(str(SL.cleaned_data))
        

    return render(request,"Data_Student.html",d)

def Retrieve_Data(request):
    SS=Student.objects.all()
    d={'SS':SS}
    if request.method=='POST':
        SA=request.POST.getlist('id')
        NA=Student.objects.none()
        for x in SA:
            NA=NA|Student.objects.filter(Sid=x)
        d={"NA":NA}
        return render(request,"Display.html",d)

    return render(request,"Retrieve_Data.html",d)

def Data_table(request):
    d={"SS":Student.objects.all}
    return render(request,'Display_data.html',d)
 