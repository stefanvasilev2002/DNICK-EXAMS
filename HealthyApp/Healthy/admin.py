from django.contrib import admin
from .models import *


class ProductCategoryInline(admin.TabularInline):
    model = Product
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    inlines = [ProductCategoryInline]
    list_display = ('name',)

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname',)


class ProductAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        return obj and obj.user == request.user


admin.site.register(Client, ClientAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
