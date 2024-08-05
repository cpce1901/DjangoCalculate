from django.urls import path
from .views import calculo_emision_co2

urlpatterns = [
    path('factor-co2/', calculo_emision_co2, name='co2'),
    
]

