from django.contrib import admin

from .models import *


class RoomCleanerInline(admin.TabularInline):
    model = RoomCleaner
    extra = 1


class EmployeeAdmin(admin.ModelAdmin):
    inlines = [RoomCleanerInline]


class HotelReservationAdmin(admin.ModelAdmin):
    list_display = ['id', 'room',]
    exclude = ['user', ]
    def save_model(self, request, obj, form, change):
        if not obj.room.is_cleaned:
            return False
        obj.user = request.user
        return super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        return obj and obj.user == request.user


class RoomAdmin(admin.ModelAdmin):
    list_display = ['number', 'is_cleaned']
    def has_add_permission(self, request):
        return request.user.is_superuser


admin.site.register(Room, RoomAdmin)
admin.site.register(HotelReservation, HotelReservationAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(RoomCleaner)
