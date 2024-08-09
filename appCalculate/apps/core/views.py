from django.views.generic import TemplateView
from apps.materials.models import Materials

class IndexTemplateView(TemplateView):
    template_name = 'core/index.html'
