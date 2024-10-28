from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group
from unfold.admin import ModelAdmin
from unfold.forms import UserChangeForm, UserCreationForm, AdminPasswordChangeForm

from .models import Currency, Product, Category, Supplier, ProductSupplier, ProductImage, Warehouse, Stock


admin.site.unregister(User)
admin.site.unregister(Group)

@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm

@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass


# class UserTokenAdmin(admin.ModelAdmin):
#     list_display = ('user','token','expiration_date', 'used', 'expired')
#     list_filter = ("used", "expired", "expiration_date")
#     search_fields = ['user']
    
admin.site.register(Currency, ModelAdmin)
admin.site.register(Product, ModelAdmin)
admin.site.register(Category, ModelAdmin)
admin.site.register(Supplier, ModelAdmin)
admin.site.register(ProductSupplier, ModelAdmin)
admin.site.register(ProductImage, ModelAdmin)
admin.site.register(Warehouse, ModelAdmin)
admin.site.register(Stock, ModelAdmin)