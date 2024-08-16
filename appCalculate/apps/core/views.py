from django.views.generic import TemplateView
from .models import Logo

class IndexTemplateView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo'] = Logo.objects.first()
        return context
    
