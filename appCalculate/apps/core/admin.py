from django.contrib import admin
from .models import Logo

@admin.register(Logo)
class logoAdmin(admin.ModelAdmin):
    pass

