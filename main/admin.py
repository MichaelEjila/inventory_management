from django.contrib import admin
from .models import Supplier, Product, Inventory

# Register your models here.
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)
    ordering = ('name',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'supplier', 'created_at', 'updated_at')
    search_fields = ('name', 'supplier__name')
    list_filter = ('supplier',)
    ordering = ('name',)

class InventoryAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'created_at', 'updated_at')
    search_fields = ('product__name',)
    list_filter = ('product',)
    ordering = ('product',)

# Register the models with the custom admin classes
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Inventory, InventoryAdmin)
