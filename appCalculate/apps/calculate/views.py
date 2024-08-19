from django.views.generic import FormView
from django.urls import reverse_lazy
from django.http import HttpRequest, HttpResponse
from django.template.loader import render_to_string
from .forms import ItemsForm

class CalculateListView(FormView):
    template_name = 'calculate/co2/co2_form.html'
    form_class = ItemsForm
    success_url = reverse_lazy('/')

    def dispatch(self, request, *args, **kwargs):
        # Resetear la lista de items cada vez que se carga la vista
        request.session['items'] = []
        request.session.modified = True
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = self.request.session.get('items', [])
        context['total_area'] = sum(item['area'] for item in context['items'])
        return context
    
