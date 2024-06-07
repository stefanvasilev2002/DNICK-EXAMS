from django.contrib import admin
from .models import *


class EventBandInline(admin.TabularInline):
    model = EventBand
    extra = 1


class EventAdmin(admin.ModelAdmin):
    inlines = [EventBandInline]
    list_display = ('name', 'date_time', )
    exclude = ('bands', 'num_participants')

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(EventAdmin, self).save_model(request, obj, form, change)

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return obj and obj.user == request.user

    def has_change_permission(self, request, obj=None):
        return obj and obj.user == request.user


class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'country',)


admin.site.register(Event, EventAdmin)
admin.site.register(Band, BandAdmin)
admin.site.register(EventBand)
