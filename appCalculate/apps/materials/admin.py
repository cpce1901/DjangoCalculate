from django.contrib import admin
from .models import Materials

# Register your models here.
@admin.register(Materials)
class MaterialsAdmin(admin.ModelAdmin):
    pass

