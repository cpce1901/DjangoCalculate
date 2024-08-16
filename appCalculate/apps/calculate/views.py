from django.views.generic import FormView, DeleteView, View
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.shortcuts import redirect
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from .forms import ItemsForm
from .models import Items, CalculateList

class CalculateListView(FormView):
    template_name = 'calculate/co2_calculate_add_material.html'
    form_class = ItemsForm
    success_url = reverse_lazy('calculate:co2')

    def get_calculate_list(self):
        session_key = self.request.session.session_key
        if not session_key:
            self.request.session.create()
            session_key = self.request.session.session_key
        
        calculate_list, created = CalculateList.objects.get_or_create(session_key=session_key)
        return calculate_list

    def form_valid(self, form):
        instance_item = form.cleaned_data["material"]
        area = form.cleaned_data["area"]
        thickness = form.cleaned_data["thickness"]
        
        calculate_list = self.get_calculate_list()
        
        # Verificar si ya existe un ítem con el mismo material en la lista de cálculo
        if calculate_list.materials.filter(material=instance_item).exists():
            form.add_error('material', "Este material ya ha sido agregado a la lista.")
            return self.form_invalid(form)
        
        new_item = Items.objects.create(
            material=instance_item,
            area=area,
            thickness=thickness
        )
        
        calculate_list.materials.add(new_item)
        messages.success(self.request, "Material agregado exitosamente.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Error al agregar el material. Por favor, verifique los datos ingresados.")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calculate_list = self.get_calculate_list()
        context['items'] = calculate_list.materials.all()
        return context
    

class DeleteItemView(DeleteView):
    model = Items
    success_url = reverse_lazy('calculate:co2')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        calculate_list = CalculateList.objects.filter(session_key=request.session.session_key).first()
        
        if calculate_list:
            calculate_list.materials.remove(self.object)
        
        success_url = self.get_success_url()
        self.object.delete()
        messages.success(request, "Item eliminado exitosamente.")
        return HttpResponseRedirect(success_url)


class CalculateResultView(View):
    def post(self, request):
        calculate_list = CalculateList.objects.filter(session_key=request.session.session_key).first()
        if calculate_list:
            total_area = calculate_list.materials.aggregate(Sum('area'))['area__sum'] or 0
            
            # Eliminar los Items asociados a esta lista de cálculo
            Items.objects.filter(calculate_lists=calculate_list).delete()
            
            # Eliminar la lista de cálculo
            calculate_list.delete()
            
            messages.success(request, f"Cálculo completado. Área total: {total_area}")
        else:
            messages.error(request, "No hay lista de cálculo para procesar.")
        
        return redirect(reverse('calculate:co2'))


class CalculateBackView(View):
    def post(self, request):
        calculate_list = CalculateList.objects.filter(session_key=request.session.session_key).first()
        if calculate_list:
            # Eliminar los Items asociados a esta lista de cálculo
            Items.objects.filter(calculate_lists=calculate_list).delete()
            # Eliminar la lista de cálculo
            calculate_list.delete()
        
        return redirect(reverse('core:index'))
    
    
class ClearCalculateListView(View):
    def post(self, request, *args, **kwargs):
        session_key = request.session.session_key
        if session_key:
            calculate_list = CalculateList.objects.filter(session_key=session_key).first()
            if calculate_list:
                Items.objects.filter(calculate_lists=calculate_list).delete()
                calculate_list.delete()
        return JsonResponse({"status": "success"})