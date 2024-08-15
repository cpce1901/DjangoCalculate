from django.http import HttpResponse
from django.views.generic import FormView, DeleteView, TemplateView
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.db.models import Sum
from apps.materials.models import Materials
from .forms import ItemsForm
from .models import Items, CalculateList


class CalculateListView(FormView):
    template_name = 'calculate/co2_calculate_add_material.html'
    form_class = ItemsForm
    success_url = reverse_lazy('calculate:co2')

    def form_valid(self, form):
        instance_item = form.cleaned_data["material"]
        area = form.cleaned_data["area"]
        thickness = form.cleaned_data["thickness"]

        new_item, created = Items.objects.get_or_create(
            material=instance_item,
            area=area,
            thickness=thickness
        )

        if not created:
            form.add_error('material', "El material ya ha sido ingresado.")
            return self.form_invalid(form)

        calculate_list, _ = CalculateList.objects.get_or_create(id=1)
        calculate_list.materials.add(new_item)

        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "El material ya ha sido seleccionado...")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calculate_list = CalculateList.objects.first()
        if calculate_list:
            context['items'] = calculate_list.materials.all()
        else:
            context['items'] = []
        return context
    

def delete_item(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(Items, id=item_id)
        calculate_list = CalculateList.objects.first()
        
        # Eliminar el item de la lista de cálculo
        if calculate_list:
            calculate_list.materials.remove(item)
        
        # Eliminar el item completamente
        item.delete()
        
        messages.success(request, "Item eliminado exitosamente.")
    else:
        messages.error(request, "Método no permitido.")
    
    return redirect(reverse('calculate:co2'))
    

def calculate_result(request):
    if request.method == 'POST':
        calculate_list = CalculateList.objects.first()
        if calculate_list:
        
            total_area = calculate_list.materials.aggregate(Sum('area'))['area__sum'] or 0            
            
            Items.objects.filter(calculate_lists=calculate_list).delete()
            
            calculate_list.materials.clear()
            
            messages.success(request, f"Cálculo completado. Área total: {total_area}")
        else:
            messages.error(request, "No hay lista de cálculo para procesar.")
        
        return redirect(reverse('calculate:co2'))
    else:
        messages.error(request, "Método no permitido.")
        return redirect(reverse('calculate:co2'))
    
    
def calculate_back(request):
    if request.method == 'POST':
        calculate_list = CalculateList.objects.first()
        if calculate_list:
            Items.objects.filter(calculate_lists=calculate_list).delete()
            calculate_list.materials.clear()
                
        return redirect(reverse('core:index'))
    else:
        return redirect(reverse('core:index'))
    
    

def tarea(request):

    # LLAmar a los mayteriales minomo 2

    # Obtener los datos de interes

    # Realizar calculos

    # devolver al html
    
    return redirect(reverse('core:index'))
    
    
