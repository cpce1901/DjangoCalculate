from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def calculo_emision_co2(request):
    return HttpResponse("CO2")