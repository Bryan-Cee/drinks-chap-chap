from django.contrib import admin
from .models import Drinks


class DrinksAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Drinks._meta.fields]


admin.site.register(Drinks, DrinksAdmin)
