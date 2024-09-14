from django.contrib import admin
from .models import *
from django.utils import timezone


class PainterAdmin(admin.ModelAdmin):
    model = Painter

    def has_add_permission(self, request):
        return request.user.is_superuser


class ExhibitionAdmin(admin.ModelAdmin):
    model = Exhibition

    def has_add_permission(self, request):
        return request.user.is_superuser

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        if request.user.is_superuser:
            return qs.filter(date_end__gte=timezone.now().date())

        paintings = Painting.objects.filter(painter__user=request.user)

        exhibition_ids = paintings.values_list('exhibition_id', flat=True)
        return qs.filter(id__in=exhibition_ids)


class PaintingAdmin(admin.ModelAdmin):
    model = Painting

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(PaintingAdmin, self).save_model(request, obj, form, change)

    def has_add_permission(self, request):
        return request.user.is_authenticated and request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return obj and request.user == obj.painter.user


admin.site.register(Painting, PaintingAdmin)
admin.site.register(Exhibition, ExhibitionAdmin)
admin.site.register(Painter, PainterAdmin)
