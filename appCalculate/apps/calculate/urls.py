from django.urls import path
from .views import SelectMaterialsFormView, CalculateTemplateView
from .views_htmx import add_material_htmx

app_name = 'calculate'

urlpatterns = [
    path('factor-co2/', SelectMaterialsFormView.as_view(), name='co2'),
    path('factor-co2/result/', CalculateTemplateView.as_view(), name='co2-result'),
    ]


url_htmx = [
    path('factor-co2/add/', add_material_htmx, name='co2-add'),
]

urlpatterns += url_htmx