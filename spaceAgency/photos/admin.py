from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Photo
from adminsortable2.admin import SortableAdminMixin


class PhotoAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'image_preview')

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="250px" height="250px" style="object-fit: cover;" />')
        return '-'
    image_preview.allow_tags = True  # Разрешаем вывод HTML

admin.site.register(Photo, PhotoAdmin)