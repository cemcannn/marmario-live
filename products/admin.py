from django.contrib import admin
from . models import Product

@admin.register(Product)
class PoductAdmin(admin.ModelAdmin):
    list_display = ('name', 'available')
    list_filter = ('available',)
    search_fields = ('name', 'description')
# Register your models here.
