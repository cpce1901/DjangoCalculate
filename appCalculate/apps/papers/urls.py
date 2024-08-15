from django.urls import path
from .views import PaperTemplateView, PaperDetailView

app_name = 'papers'

urlpatterns = [
    path('papers/', PaperTemplateView.as_view(), name='papers-list'),
    path('papers/<int:pk>/', PaperDetailView.as_view(), name='paper-detail')
    
]