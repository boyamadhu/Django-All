from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def m(request):
    return input('enter movie name')
def k(request):
    return input('enter rating')