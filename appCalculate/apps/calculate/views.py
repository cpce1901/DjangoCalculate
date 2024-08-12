from django.views.generic import TemplateView


class CalculateEmitCO2TemplateView(TemplateView):
    template_name = 'calculate/co2_calculate_select_materials.html'