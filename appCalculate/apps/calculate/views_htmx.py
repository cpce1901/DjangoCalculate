from django.views.generic import View
from django.http import HttpResponse
from django.template.loader import render_to_string
from .forms import ItemsForm

class AddItemView(View):
    def post(self, request, *args, **kwargs):
        form = ItemsForm(request.POST)
        session_id = request.session.get('session_id', None)
        items = request.session.get(f'items_{session_id}', [])

        if form.is_valid():
            material = form.cleaned_data['materials']
            area = form.cleaned_data['area']
            thickness = form.cleaned_data['thickness']

            new_item = {
                'material.id': material.id,
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
            return HttpResponse(error_html)
        

class DeleteItemView(View):
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


class ResultView(View):
    def get(self, request, *args, **kwargs):
        session_id = request.session.get('session_id', None)
        items = request.session.get(f'items_{session_id}', [])

        total_area = sum(item['area'] for item in items) if items else 0
        context = {
            'result': total_area,
        }
        html = render_to_string('calculate/co2/htmx/htmx_result.html', context)
        return HttpResponse(html)
