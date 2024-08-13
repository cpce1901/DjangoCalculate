from django.views.generic import FormView, TemplateView, View
from .forms import SelectMaterialsForm, LoginForm
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from apps.materials.models import Materials


class SelectMaterialsFormView(FormView):
    template_name = 'calculate/co2_calculate_add_material.html'
    form_class = SelectMaterialsForm
    success_url = '/'


@method_decorator(csrf_exempt, name='dispatch')
class CalculateTemplateView(TemplateView):
    template_name = 'co2_result_page.html'



    
    


