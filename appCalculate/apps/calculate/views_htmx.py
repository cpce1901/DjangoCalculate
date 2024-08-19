from django.views.generic import View
from django.http import HttpResponse
from django.template.loader import render_to_string
from .forms import ItemsForm

class AddItemView(View):
    def post(self, request, *args, **kwargs):
        form = ItemsForm(request.POST)
        if form.is_valid():
            material = form.cleaned_data['materials']
            area = form.cleaned_data['area']
            thickness = form.cleaned_data['thickness']

            new_item = {
                'material_name': material.name,
                'area': area,
                'thickness': thickness,
            }

            items = request.session.get('items', [])
            
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

            request.session['items'] = items
            request.session.modified = True

            context = {
                'items': items,
                'total_area': sum(item['area'] for item in items),
            }
            html = render_to_string('calculate/co2/htmx/htmx_item_list.html', context)
            
            return HttpResponse(html)
        else:
            return HttpResponse(form.errors.as_json(), status=400)
        

class DeleteItemView(View):
    def get(self, request, *args, **kwargs):
        index = int(request.GET.get('index', -1))
        items = request.session.get('items', [])
        
        if 0 <= index < len(items):
            del items[index]
            request.session['items'] = items
            request.session.modified = True

        context = {
            'items': items,
            'total_area': sum(item['area'] for item in items),
        }
        html = render_to_string('calculate/co2/htmx/htmx_item_list.html', context)
        return HttpResponse(html)