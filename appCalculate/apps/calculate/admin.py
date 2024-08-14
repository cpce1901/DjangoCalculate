from django.contrib import admin
from .models import CalculateList, Items


@admin.register(Items)
class ItemsAdmin(admin.ModelAdmin):
    pass

@admin.register(CalculateList)
class CalculateListAdmin(admin.ModelAdmin):
    pass