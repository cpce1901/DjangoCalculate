from django.urls import path
from .views import CalculateListView, DeleteItemView, CalculateResultView, CalculateBackView, ClearCalculateListView


app_name = 'calculate'

urlpatterns = [
    path('factor-co2/', CalculateListView.as_view(), name='co2'),
    path('delete/<pk>/', DeleteItemView.as_view(), name='delete_item'),
    path('calculate-result/back/', CalculateBackView.as_view(), name='calculate_back'),
    path('calculate-result/', CalculateResultView.as_view(), name='calculate_result'),

    path('clear-list/', ClearCalculateListView.as_view(), name='clear_list'),
    ]

