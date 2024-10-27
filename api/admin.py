from django.contrib import admin
from .models import Currency, Product, Category, Supplier, ProductSupplier, ProductImage, Warehouse, Stock


# class UserTokenAdmin(admin.ModelAdmin):
#     list_display = ('user','token','expiration_date', 'used', 'expired')
#     list_filter = ("used", "expired", "expiration_date")
#     search_fields = ['user']
    
admin.site.register(Currency)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Supplier)
admin.site.register(ProductSupplier)
admin.site.register(ProductImage)
admin.site.register(Warehouse)
admin.site.register(Stock)