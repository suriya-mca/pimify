from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group
from unfold.admin import ModelAdmin
from unfold.forms import UserChangeForm, UserCreationForm, AdminPasswordChangeForm
from import_export.admin import ImportExportModelAdmin
from unfold.contrib.import_export.forms import ExportForm, ImportForm, SelectableFieldsExportForm
from unfold.contrib.filters.admin import FieldTextFilter, ChoicesDropdownFilter, RangeDateFilter
from django.db import models
from unfold.contrib.forms.widgets import WysiwygWidget
from image_uploader_widget.widgets import ImageUploaderWidget
from login_history.models import LoginHistory

from .models import Currency, Product, Category, Supplier, ProductSupplier, ProductImage, Warehouse, Stock, Organization, APIKey


admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(LoginHistory)
admin.site.site_url = None


@admin.register(LoginHistory)
class LoginHistoryAdmin(ModelAdmin, ImportExportModelAdmin):

    list_display = ('user','date_time', 'ip', 'user_agent', 'is_logged_in')
    import_form_class = ImportForm
    export_form_class = ExportForm
    export_form_class = SelectableFieldsExportForm

@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    compressed_fields = True
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm

    def has_module_permission(self, request):
        return False


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    compressed_fields = True

    def has_module_permission(self, request):
        return False


@admin.register(Currency)
class CurrencyAdmin(ModelAdmin, ImportExportModelAdmin):
    compressed_fields = True
    warn_unsaved_form = True
    list_display = ('code','symbol')
    list_filter = ('code',)
    search_fields = ['code']

    import_form_class = ImportForm
    export_form_class = ExportForm
    export_form_class = SelectableFieldsExportForm

    def has_module_permission(self, request):
        return False


@admin.register(Product)
class ProductAdmin(ModelAdmin, ImportExportModelAdmin):
    compressed_fields = True
    warn_unsaved_form = True
    list_filter_submit = True
    list_display = ('sku', 'name', 'price', 'currency', 'stock_quantity', 'is_active', 'created_at', 'updated_at')
    list_filter = (('name', ChoicesDropdownFilter), ('sku', FieldTextFilter), 'is_active', ('categories', ChoicesDropdownFilter), ('created_at', RangeDateFilter))
    search_fields = ['name', 'sku', 'categories']

    import_form_class = ImportForm
    export_form_class = ExportForm
    export_form_class = SelectableFieldsExportForm

    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        }
    }

    def has_module_permission(self, request):
        return False


@admin.register(Category)
class CategoryAdmin(ModelAdmin, ImportExportModelAdmin):
    compressed_fields = True
    warn_unsaved_form = True
    list_filter_submit = True
    list_display = ('name', 'slug')
    list_filter = (('name', ChoicesDropdownFilter), ('slug',ChoicesDropdownFilter))
    search_fields = ['name']

    import_form_class = ImportForm
    export_form_class = ExportForm
    export_form_class = SelectableFieldsExportForm

    def has_module_permission(self, request):
        return False


@admin.register(Supplier)
class SupplierAdmin(ModelAdmin, ImportExportModelAdmin):
    compressed_fields = True
    warn_unsaved_form = True
    list_filter_submit = True
    list_display = ('name','email', 'phone')
    list_filter = (('name', ChoicesDropdownFilter),)
    search_fields = ['name', 'email']

    import_form_class = ImportForm
    export_form_class = ExportForm
    export_form_class = SelectableFieldsExportForm

    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        }
    }

    def has_module_permission(self, request):
        return False


@admin.register(ProductSupplier)
class ProductSupplierAdmin(ModelAdmin, ImportExportModelAdmin):
    compressed_fields = True
    warn_unsaved_form = True
    list_filter_submit = True
    list_display = ('product','supplier', 'cost_price', 'lead_time')
    list_filter = (('product', ChoicesDropdownFilter), ('supplier', ChoicesDropdownFilter))
    search_fields = ['product', 'supplier']

    import_form_class = ImportForm
    export_form_class = ExportForm
    export_form_class = SelectableFieldsExportForm

    def has_module_permission(self, request):
        return False


@admin.register(ProductImage)
class ProductImageAdmin(ModelAdmin, ImportExportModelAdmin):
    compressed_fields = True
    warn_unsaved_form = True
    list_filter_submit = True
    list_display = ('product','image')
    list_filter = (('product', ChoicesDropdownFilter),)
    search_fields = ['product']

    import_form_class = ImportForm
    export_form_class = ExportForm
    export_form_class = SelectableFieldsExportForm

    formfield_overrides = {
        models.ImageField: {'widget': ImageUploaderWidget},
    }

    def has_module_permission(self, request):
        return False


@admin.register(Warehouse)
class WarehouseAdmin(ModelAdmin, ImportExportModelAdmin):
    compressed_fields = True
    warn_unsaved_form = True
    list_filter_submit = True
    list_display = ('name',)
    list_filter = (('name', ChoicesDropdownFilter),)
    search_fields = ['name']

    import_form_class = ImportForm
    export_form_class = ExportForm
    export_form_class = SelectableFieldsExportForm

    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        }
    }

    def has_module_permission(self, request):
        return False


@admin.register(Stock)
class StockAdmin(ModelAdmin, ImportExportModelAdmin):
    compressed_fields = True
    warn_unsaved_form = True
    list_filter_submit = True
    list_display = ('product','quantity', 'warehouse')
    list_filter = (('product', ChoicesDropdownFilter),)
    search_fields = ['product']

    import_form_class = ImportForm
    export_form_class = ExportForm
    export_form_class = SelectableFieldsExportForm

    def has_module_permission(self, request):
        return False


@admin.register(APIKey)
class APIKeyAdmin(ModelAdmin):
    compressed_fields = True
    warn_unsaved_form = True
    list_display = ('name', 'api_key', 'is_active', 'created_at', 'updated_at')
    list_filter = (('name'), ('is_active'))
    search_fields = ['name']


@admin.register(Organization)
class OrganizationAdmin(ModelAdmin):
    compressed_fields = True
    warn_unsaved_form = True
    list_display = ('name', 'email', 'website', 'api_keys', 'created_at', 'updated_at')
    list_filter = (('name'),)
    search_fields = ['name']

    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        }
    }
