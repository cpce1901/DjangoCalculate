from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    print("Esto es una vista")
    return HttpResponse("hello")