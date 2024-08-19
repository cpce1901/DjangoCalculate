from django.urls import path
from .views import CalculateListView
from .views_htmx import AddItemView, DeleteItemView, ResultView


app_name = 'calculate'

urlpatterns = [
    path('factor-co2/', CalculateListView.as_view(), name='co2'),
    ]

htmx_url = [
    path('factor-co2/add/', AddItemView.as_view(), name='co2-add'),
    path('delete-item/', DeleteItemView.as_view(), name='delete_item'),
    path('result/', ResultView.as_view(), name='result'),
]

urlpatterns += htmx_url