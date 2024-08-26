from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import ItemsFormCO2, ItemsFormTrans
import uuid


class CalculateListCO2View(FormView):
    template_name = 'calculate/co2/co2_form.html'
    form_class = ItemsFormCO2
    success_url = reverse_lazy('core:index')

    def dispatch(self, request, *args, **kwargs):
        if 'session_id' in request.session:
            del request.session['session_id']
        if 'items' in request.session:
            del request.session['items']

        # Generar un nuevo identificador único para la sesión
        request.session['session_id'] = str(uuid.uuid4())
        request.session['items'] = []
        request.session.modified = True

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = self.request.session.get('items', [])
        return context


class CalculateListTRANSView(FormView):
    template_name = 'calculate/trans/trans_form.html'
    form_class = ItemsFormTrans
    success_url = reverse_lazy('core:index')

    def dispatch(self, request, *args, **kwargs):
        if 'session_id' in request.session:
            del request.session['session_id']
        if 'items' in request.session:
            del request.session['items']

        # Generar un nuevo identificador único para la sesión
        request.session['session_id'] = str(uuid.uuid4())
        request.session['items'] = []
        request.session.modified = True

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = self.request.session.get('items', [])
        return context