from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group
from unfold.admin import ModelAdmin
from unfold.forms import UserChangeForm, UserCreationForm, AdminPasswordChangeForm
from import_export.admin import ImportExportModelAdmin
from unfold.contrib.import_export.forms import ExportForm, ImportForm, SelectableFieldsExportForm
from unfold.contrib.filters.admin import FieldTextFilter, ChoicesDropdownFilter, RangeDateFilter

from .models import Currency, Product, Category, Supplier, ProductSupplier, ProductImage, Warehouse, Stock, Organization


admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.site_url = None


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass


class CurrencyAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = ('code','symbol')
    list_filter = ('code',)
    search_fields = ['code']

    import_form_class = ImportForm
    export_form_class = ExportForm
    export_form_class = SelectableFieldsExportForm


class ProductAdmin(ModelAdmin, ImportExportModelAdmin):
    list_filter_submit = True
    list_display = ('sku', 'name', 'price', 'currency', 'stock_quantity', 'is_active', 'created_at', 'updated_at')
    list_filter = (('name', ChoicesDropdownFilter), ('sku', FieldTextFilter), 'is_active', ('categories', ChoicesDropdownFilter), ('created_at', RangeDateFilter))
    search_fields = ['name', 'sku', 'categories']

    import_form_class = ImportForm
    export_form_class = ExportForm
    export_form_class = SelectableFieldsExportForm


class CategoryAdmin(ModelAdmin, ImportExportModelAdmin):
    list_filter_submit = True
    list_display = ('name', 'slug')
    list_filter = (('name', ChoicesDropdownFilter), ('slug',ChoicesDropdownFilter))
    search_fields = ['name']

    import_form_class = ImportForm
    export_form_class = ExportForm
    export_form_class = SelectableFieldsExportForm


class SupplierAdmin(ModelAdmin, ImportExportModelAdmin):
    list_filter_submit = True
    list_display = ('name','email', 'phone')
    list_filter = (('name', ChoicesDropdownFilter),)
    search_fields = ['name', 'email']

    import_form_class = ImportForm
    export_form_class = ExportForm
    export_form_class = SelectableFieldsExportForm


class ProductSupplierAdmin(ModelAdmin, ImportExportModelAdmin):
    list_filter_submit = True
    list_display = ('product','supplier', 'cost_price', 'lead_time')
    list_filter = (('product', ChoicesDropdownFilter), ('supplier', ChoicesDropdownFilter))
    search_fields = ['product', 'supplier']

    import_form_class = ImportForm
    export_form_class = ExportForm
    export_form_class = SelectableFieldsExportForm


class ProductImageAdmin(ModelAdmin, ImportExportModelAdmin):
    list_filter_submit = True
    list_display = ('product','image')
    list_filter = (('product', ChoicesDropdownFilter),)
    search_fields = ['product']

    import_form_class = ImportForm
    export_form_class = ExportForm
    export_form_class = SelectableFieldsExportForm


class WarehouseAdmin(ModelAdmin, ImportExportModelAdmin):
    list_filter_submit = True
    list_display = ('name',)
    list_filter = (('name', ChoicesDropdownFilter),)
    search_fields = ['name']

    import_form_class = ImportForm
    export_form_class = ExportForm
    export_form_class = SelectableFieldsExportForm


class StockAdmin(ModelAdmin, ImportExportModelAdmin):
    list_filter_submit = True
    list_display = ('product','quantity', 'warehouse')
    list_filter = (('product', ChoicesDropdownFilter),)
    search_fields = ['product']

    import_form_class = ImportForm
    export_form_class = ExportForm
    export_form_class = SelectableFieldsExportForm


admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(ProductSupplier, ProductSupplierAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(Warehouse, WarehouseAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(Organization, ModelAdmin)
