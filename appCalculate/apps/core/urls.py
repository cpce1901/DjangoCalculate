from django.urls import path
from .views import IndexTemplateView

app_name = 'core'

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    
]

