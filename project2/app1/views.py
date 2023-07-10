from django.shortcuts import render

# Create your views here.
def sab(request):
    return render(request,'first.html')

def sabi(request):
    return render(request,'second.html')