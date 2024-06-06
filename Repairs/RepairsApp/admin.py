from django.contrib import admin

from .models import *


class ManufacturerInline(admin.StackedInline):
    model = WorkshopManufacturer
    extra = 1


class RepairAdmin(admin.ModelAdmin):
    exclude = ('user',)
    list_display = ('user',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


class WorkshopAdmin(admin.ModelAdmin):
    inlines = [ManufacturerInline]

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name',)

    def has_add_permission(self, request, obj=None):
        return request.user.is_superuser


class CarAdmin(admin.ModelAdmin):
    list_display = ('type', 'max_speed',)


admin.site.register(Car, CarAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Workshop, WorkshopAdmin)
admin.site.register(Repair, RepairAdmin)
