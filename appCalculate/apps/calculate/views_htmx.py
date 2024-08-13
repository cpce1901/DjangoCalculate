from django.shortcuts import render
from .forms import SelectMaterialsForm

def add_material_htmx(request):
    template_name = 'calculate/htmx_co2_calculate_add_material.html'
    if request.method == 'POST':
        pass
    context = {
        'form' : SelectMaterialsForm()
    }
    return render(request, template_name, context)