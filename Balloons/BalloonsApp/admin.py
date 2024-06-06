from django.contrib import admin

from .models import *


class CompanyPilotInline(admin.TabularInline):
    model = CompanyPilot
    extra = 1


class CompanyAdmin(admin.ModelAdmin):
    inlines = [CompanyPilotInline]
    list_display = ('name',)


class FlightAdmin(admin.ModelAdmin):
    exclude = ('user',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        return obj and request.user == obj.user

    def has_delete_permission(self, request, obj=None):
        return False


class PilotAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname',)


admin.site.register(Company, CompanyAdmin)
admin.site.register(Pilot, PilotAdmin)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Balloon)
