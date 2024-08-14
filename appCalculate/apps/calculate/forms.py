from django import forms
from .models import Items
from apps.materials.models import Materials

class ItemsForm(forms.ModelForm):

    
    class Meta:
        model = Items
        fields = ['material', 'area', 'thickness']
        widgets = {
            'material': forms.Select(
                attrs={
                    'class': 'block w-full px-4 py-2 text-gray-700 bg-white border border-gray-300 rounded-md focus:border-blue-500 focus:outline-none focus:ring'
                }
            ),
            'area': forms.NumberInput(
                attrs={
                    'class': 'block w-full px-4 py-2 text-gray-700 bg-white border border-gray-300 rounded-md focus:border-blue-500 focus:outline-none focus:ring',
                    'step': '0.01'
                }
            ),
            'thickness': forms.NumberInput(
                attrs={
                    'class': 'block w-full px-4 py-2 text-gray-700 bg-white border border-gray-300 rounded-md focus:border-blue-500 focus:outline-none focus:ring',
                    'step': '0.01'
                }
            ),
        }







   