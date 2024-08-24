from django.views.generic import TemplateView, DetailView, ListView
from .models import Papers

# Create your views here.
class PaperTemplateView(ListView):
    template_name = 'papers/papers_list.html'
    context_object_name = 'papers'
    paginate_by = 2
    model = Papers

  


class PaperDetailView(TemplateView):
    template_name = 'papers/papers_detail.html'
    model = Papers

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs["id"]
        context['paper'] = Papers.objects.get(id=id)
        return context