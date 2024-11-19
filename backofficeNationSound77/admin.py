from django.contrib import admin
from django.utils.html import format_html
from .models import Style, Artiste, Calendrier, Scene, Programme, Event
from .models import CategoriePoi, Poi
from .models import MessageUrgent

# Register your models here.

@admin.register(Calendrier)
class CalendrierAdmin(admin.ModelAdmin):
    list_display = ('jour_festival', 'date_festival')
    list_filter = ('date_festival',)
    search_fields = ('jour_festival',)
    ordering = ('date_festival',)

@admin.register(Style)
class StyleAdmin(admin.ModelAdmin):
    list_display = ('style',)
    search_fields = ('style',)

@admin.register(Artiste)
class ArtisteAdmin(admin.ModelAdmin):
    list_display = ('nom', 'style', 'description', 'image_preview')
    list_filter = ('style',)
    search_fields = ('nom',)
    
    def image_preview(self, obj):
        if obj.visuel:
            return format_html('<img src="{}" style="width: 80px; height:80px;" />'.format(obj.visuel.url))
        return ""
    image_preview.short_description = 'Visuel artiste'

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('event',)
    search_fields = ('event',)

@admin.register(Scene)
class SceneAdmin(admin.ModelAdmin):
    list_display = ('scene',)
    search_fields = ('scene',)

@admin.register(Programme)
class ProgrammeAdmin(admin.ModelAdmin):
    list_display = ('calendrier', 'horaire', 'artiste__nom', 'artiste__style', 'event', 'scene', 'artiste_image')
    list_filter = ('calendrier', 'scene', 'event', 'artiste__style')
    search_fields = ('artiste__nom', 'artiste__style__style')
    ordering = ('calendrier', 'horaire')
    
    def artiste_image(self, obj):
        # Vérifie si obj.artiste existe et si obj.artiste.image existe
        if obj.artiste and obj.artiste.visuel:
            return format_html('<img src="{}" width="50" height="50" />', obj.artiste.visuel.url)
        return "-"
    artiste_image.short_description = "Artiste Visuel"

    # Ajoute des champs de filtrage par date et heure
    date_hierarchy = 'calendrier__date_festival'


#Model du Point d'intérêt
@admin.register(CategoriePoi)
class CategoriePoiAdmin(admin.ModelAdmin):
    list_display = ('categoriePoi',)
    search_fields = ('categoriePoi',)

@admin.register(Poi)
class PoiAdmin(admin.ModelAdmin):
    list_display = ('nomPoi', 'categoriePoi', 'descriptionPoi', 'latitudePoi', 'longitudePoi')
    search_fields = ('nomPoi',)

#Model du Message urgent    
@admin.register(MessageUrgent)
class MessageUrgentAdmin(admin.ModelAdmin):
    list_display = ('msgUrgent','prioriteMsg' )
    search_fields = ('prioriteMsg',)