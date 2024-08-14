from django.urls import path
from .views import CalculateListView, delete_item, calculate_result


app_name = 'calculate'

urlpatterns = [
    path('factor-co2/', CalculateListView.as_view(), name='co2'),
    path('delete/<int:item_id>/', delete_item, name='delete_item'),
    path('calculate-result/', calculate_result, name='calculate_result'),
    ]

