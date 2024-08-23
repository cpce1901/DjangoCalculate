from django.views.generic import TemplateView, DetailView
from .models import Papers

# Create your views here.
class PaperTemplateView(TemplateView):
    template_name = 'papers/papers_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['papers'] = Papers.objects.all()
        return context


class PaperDetailView(TemplateView):
    template_name = 'papers/papers_detail.html'
    model = Papers

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs["id"]
        context['paper'] = Papers.objects.get(id=id)
        return context