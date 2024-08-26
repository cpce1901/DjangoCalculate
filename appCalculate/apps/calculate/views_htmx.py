"""
Django 5.1

De que se trata

Version

Creador

"""

from django.views.generic import View
from django.http import HttpResponse
from django.template.loader import render_to_string
from .forms import ItemsForm
from apps.materials.models import Materials


class AddItemCO2View(View):
    def post(self, request, *args, **kwargs):
        form = ItemsForm(request.POST)
        session_id = request.session.get('session_id', None)
        items = request.session.get(f'items_{session_id}', [])

        # Verificar si ya hay 5 elementos
        if len(items) >= 5:
            context = {
                'items': items,  # Mostrar los elementos existentes
                'message': 'Haz superado el limite de items...'  # Mensaje de advertencia
            }
            html = render_to_string('calculate/co2/htmx/htmx_item_list.html', context)
            return HttpResponse(html)

        if form.is_valid():
            material = form.cleaned_data['materials']
            area = form.cleaned_data['area']
            thickness = form.cleaned_data['thickness']

            new_item = {
                'material_id': material.id,
                'material_name': material.name,
                'area': area,
                'thickness': thickness,
            }

            # Actualizar si existe, sino agregar nuevo
            updated = False
            for item in items:
                if item['material_name'] == new_item['material_name']:
                    item['area'] = new_item['area']
                    item['thickness'] = new_item['thickness']
                    updated = True
                    break

            if not updated:
                items.append(new_item)

            request.session[f'items_{session_id}'] = items
            request.session.modified = True

            context = {
                'items': items,
            }
            html = render_to_string('calculate/co2/htmx/htmx_item_list.html', context)
            return HttpResponse(html)
        else:
            errors = {
                field: [{'message': error} for error in error_list]
                for field, error_list in form.errors.items()
            }
            context = {
                'errors': errors,
            }
            error_html = render_to_string('calculate/co2/htmx/htmx_messages.html', context)
            return HttpResponse(error_html, status=400)


class DeleteItemCO2View(View):
    def get(self, request, *args, **kwargs):
        index = int(request.GET.get('index', -1))
        session_id = request.session['session_id']
        items = request.session.get(f'items_{session_id}', [])

        if 0 <= index < len(items):
            del items[index]
            request.session[f'items_{session_id}'] = items
            request.session.modified = True

        context = {
            'items': items,
            'total_area': sum(item['area'] for item in items),
        }
        html = render_to_string('calculate/co2/htmx/htmx_item_list.html', context)
        return HttpResponse(html)


class ResultCO2View(View):

    def co2_calculate(self, items):
        total_emision_m2 = 0
        for item in items:
            material_id = item['material_id']
            material_name = item['material_name']
            espesor = item['thickness']
            area = item['area']
            
            # Obtener el material desde la base de datos
            try:
                material = Materials.objects.get(id=material_id)
            except Materials.DoesNotExist:
                print(f"No hay información para el material: {material_name}")
                continue

            densidad_kg_m3 = material.density
            fe_kg_co2 = material.co2_factor

            volumen_m3 = espesor * area
            densidad_ton_m3 = densidad_kg_m3 / 1000
            ton = densidad_ton_m3 * volumen_m3
            emision_capa_kg_co2_ton = fe_kg_co2 * ton
            emision_capa_kg_co2_m3 = emision_capa_kg_co2_ton * densidad_ton_m3
            emision_capa_kg_co2_m2 = emision_capa_kg_co2_m3 * area

            total_emision_m2 += emision_capa_kg_co2_m2

        return total_emision_m2
    
    def get(self, request, *args, **kwargs):
        session_id = request.session.get('session_id', None)
        items = request.session.get(f'items_{session_id}', [])       

       
        if items:
            result_co2 = self.co2_calculate(items)
            context = {
                'result': result_co2,
                'status': 'success',
                'message': None,
            }
        else:
            context = {
                'result': 0,
                'status': 'error',
                'message': 'Debes ingresar almenos un elemento...',
            }

        html = render_to_string('calculate/co2/htmx/htmx_result.html', context)
        return HttpResponse(html)


class AddItemTRANSView(View):
    def post(self, request, *args, **kwargs):
        form = ItemsForm(request.POST)
        session_id = request.session.get('session_id', None)
        items = request.session.get(f'items_{session_id}', [])

        # Verificar si ya hay 5 elementos
        if len(items) >= 5:
            context = {
                'items': items,  # Mostrar los elementos existentes
                'message': 'Haz superado el limite de items...'  # Mensaje de advertencia
            }
            html = render_to_string('calculate/trans/htmx/htmx_item_list.html', context)
            return HttpResponse(html)

        if form.is_valid():
            material = form.cleaned_data['materials']
            area = form.cleaned_data['area']
            thickness = form.cleaned_data['thickness']

            new_item = {
                'material_id': material.id,
                'material_name': material.name,
                'area': area,
                'thickness': thickness,
            }

            # Actualizar si existe, sino agregar nuevo
            updated = False
            for item in items:
                if item['material_name'] == new_item['material_name']:
                    item['area'] = new_item['area']
                    item['thickness'] = new_item['thickness']
                    updated = True
                    break

            if not updated:
                items.append(new_item)

            request.session[f'items_{session_id}'] = items
            request.session.modified = True

            context = {
                'items': items,
            }
            html = render_to_string('calculate/trans/htmx/htmx_item_list.html', context)
            return HttpResponse(html)
        else:
            errors = {
                field: [{'message': error} for error in error_list]
                for field, error_list in form.errors.items()
            }
            context = {
                'errors': errors,
            }
            error_html = render_to_string('calculate/trans/htmx/htmx_messages.html', context)
            return HttpResponse(error_html, status=400)


class DeleteItemTRANSView(View):
    """
    De que se trata cada clase
    """

    def get(self, request, *args, **kwargs):
        # Funcion para obtener items
        index = int(request.GET.get('index', -1))
        session_id = request.session['session_id']
        items = request.session.get(f'items_{session_id}', [])

        if 0 <= index < len(items):
            del items[index]
            request.session[f'items_{session_id}'] = items
            request.session.modified = True

        context = {
            'items': items,
            'total_area': sum(item['area'] for item in items),
        }
        html = render_to_string('calculate/trans/htmx/htmx_item_list.html', context)
        return HttpResponse(html)


# Vista HTMX para obtener resultados 
class ResultTRANSView(View):

    def result_trans(self, items):
        constante_uno = 1
        resistencia_superficial = 0.17  
        total_resistencia = 0
        transmitancia = 0

        for item in items:
            material_id = item['material_id']
            material_name = item['material_name']
            espesor = item['thickness']

            # Obtener el material desde la base de datos
            try:
                material = Materials.objects.get(id=material_id)
            except Materials.DoesNotExist:
                print(f"No hay información para el material: {material_name}")
                continue

            conductividad = material.thermic_trans

            resistencia = espesor / conductividad
            total_resistencia += resistencia


        transmitancia = constante_uno / (total_resistencia + resistencia_superficial) if total_resistencia > 0 else 0

        return transmitancia
    

    def get(self, request, *args, **kwargs):
        session_id = request.session.get('session_id', None)
        items = request.session.get(f'items_{session_id}', [])

        if items:
            result_trans = self.result_trans(items)
            context = {
                'result': result_trans,
                'status': 'success',
                'message': None,
            }
        else:
            context = {
                'result': 0,
                'status': 'error',
                'message': 'Debes ingresar almenos un elemento...',
            }

        html = render_to_string('calculate/trans/htmx/htmx_result.html', context)
        return HttpResponse(html)
