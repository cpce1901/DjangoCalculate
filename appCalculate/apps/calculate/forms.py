from django import forms
from apps.materials.models import Materials

class SelectMaterialsForm(forms.Form):

    materials = forms.ModelChoiceField(
        queryset=Materials.objects.all(),
        label="Material",
        empty_label="Seleccione un material",
        widget=forms.Select(
            attrs={
                "id": "materials",
                "class": "block text-gray-700 text-sm font-medium mb-2",
            }
        ),
    )

    area = forms.FloatField(  # Cambiado a EmailField para validar correos electrónicos
        label="Area m2",
        widget=forms.NumberInput(  # Cambiado a EmailInput
            attrs={
                "id": "area",
                "placeholder": "m2",
                "class": "block text-gray-700 text-sm font-medium mb-2",
            }
        ),
    )

    thickness = forms.FloatField(
        label="Espesor mm",
        widget=forms.NumberInput(
            attrs={
                "id": "thickness",
                "placeholder": "mm",
                "class": "block text-gray-700 text-sm font-medium mb-2-1",
            }
        ),
    )



class LoginForm(forms.Form):

    user = forms.CharField(
        #label="Usuario"
    )

    password = forms.CharField(
        label="Password",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "id": "Password-2",
                "class": "",
            }
        ),
    )

   