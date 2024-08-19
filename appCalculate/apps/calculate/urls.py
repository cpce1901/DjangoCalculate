from django.urls import path
from .views import CalculateListView
from .views_htmx import AddItemView, DeleteItemView


app_name = 'calculate'

urlpatterns = [
    path('factor-co2/', CalculateListView.as_view(), name='co2'),
    ]

htmx_url = [
    path('factor-co2/add/', AddItemView.as_view(), name='co2-add'),
    path('delete-item/', DeleteItemView.as_view(), name='delete_item'),
]

urlpatterns += htmx_url