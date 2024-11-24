from django.contrib import admin
from django.utils.html import format_html
from .models import Partenaire

# Register your models here.
@admin.register(Partenaire)
class PartenaireAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description', 'image_preview')
    search_fields = ('nom',)
    
    def image_preview(self, obj):
        if obj.visuel:
            return format_html('<img src="{}" style="width: 80px; height:80px;" />'.format(obj.visuel.url))
        return ""
    image_preview.short_description = 'Visuel partenaire'