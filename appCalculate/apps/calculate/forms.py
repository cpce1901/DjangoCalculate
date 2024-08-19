from django import forms
from apps.materials.models import Materials


class ItemsForm(forms.Form):

    materials = forms.ModelChoiceField(
        queryset=Materials.objects.all(),
        label="Material",
        empty_label="MATERIALES",
        widget=forms.Select(
            attrs={
                "id": "materials",
                "class": "w-52 p-2 outline outline-1 outline-gray-300 rounded-lg text-black focus:outline-none appearance-none bg-white text-gray-600",
            }
        ),
    )

    area = forms.FloatField(  # Cambiado a EmailField para validar correos electrónicos
        label="Area m2",
        required=True,
        widget=forms.NumberInput(  # Cambiado a EmailInput
            attrs={
                "id": "area",
                "placeholder": "Ingrese m2",
                "class": "p-2 outline outline-1 outline-gray-300 bg-white rounded-lg text-gray-600",
            }
        ),
    )

    thickness = forms.FloatField(
        label="Espesor mm",
        required=True,
        widget=forms.NumberInput(
            attrs={
                "id": "thickness",
                "placeholder": "Ingrese mm",
                "class": "p-2 outline outline-1 outline-gray-300 bg-white rounded-lg text-gray-600",
            }
        ),
    )

    








   