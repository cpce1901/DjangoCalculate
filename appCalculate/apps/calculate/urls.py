from django.urls import path
from .views import CalculateEmitCO2TemplateView

app_name = 'calculate'

urlpatterns = [
    path('factor-co2/', CalculateEmitCO2TemplateView.as_view(), name='co2'),
    
]

