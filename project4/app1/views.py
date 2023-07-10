from django.shortcuts import render

# Create your views here.
def sab(request):
    return render(request,'first.html')

def madhu(request):
    return render(request,'second.html')