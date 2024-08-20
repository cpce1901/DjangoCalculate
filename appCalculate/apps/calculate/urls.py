from django.urls import path
from .views import CalculateListCO2View, CalculateListTRANSView
from .views_htmx import AddItemCO2View, DeleteItemCO2View, ResultCO2View, AddItemTRANSView, DeleteItemTRANSView, ResultTRANSView


app_name = 'calculate'

urlpatterns = [
    path('co2/', CalculateListCO2View.as_view(), name='co2'),
    path('trans/', CalculateListTRANSView.as_view(), name='trans'),
    ]

htmx_url = [
    path('co2/add/', AddItemCO2View.as_view(), name='co2-add'),
    path('co2/del/', DeleteItemCO2View.as_view(), name='co2-del'),
    path('co2/result/', ResultCO2View.as_view(), name='co2-result'),

    path('trans/add/', AddItemTRANSView.as_view(), name='trans-add'),
    path('trans/del/', DeleteItemTRANSView.as_view(), name='trans-del'),
    path('trans/result/',ResultTRANSView.as_view(), name='trans-result'),
]

urlpatterns += htmx_url