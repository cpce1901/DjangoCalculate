from django.contrib import admin
from .models import Papers

# Register your models here.
# Register your models here.
@admin.register(Papers)
class PapersAdmin(admin.ModelAdmin):
    pass