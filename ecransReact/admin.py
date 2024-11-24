from django.contrib import admin
from django.utils.html import format_html
from .models import Contact, Faq, Faqcategorie, MentionLegale, Partenaire, Partenairecategorie

# Register your models here.
#Partenaire :
#   - nom
#   - description
#   - visuel
#   - categorie
@admin.register(Partenairecategorie)
class FaqcategorieAdmin(admin.ModelAdmin):
    list_display = ('categorie',)
    search_fields = ('categorie',)

@admin.register(Partenaire)
class PartenaireAdmin(admin.ModelAdmin):
    list_display = ('categorie', 'nom', 'description', 'image_preview')
    search_fields = ('nom',)
    
    def image_preview(self, obj):
        if obj.visuel:
            return format_html('<img src="{}" style="width: 80px; height:80px;" />'.format(obj.visuel.url))
        return ""
    image_preview.short_description = 'Visuel partenaire'


#Mentions Légales :
#   - titre
#   - mention
@admin.register(MentionLegale)
class MentionLegaleAdmin(admin.ModelAdmin):
    list_display = ('ordre','titre', 'mention')
    search_fields = ('titre',)


 #Contact :
#   - visuel
#   - nom
#   - adresse
#   - horaires ouverture
#   - @mail
#   - telephone       
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('nom', 'adresse', 'horaires', 'mail', 'telephone','image_preview')
    search_fields = ('nom',)
    
    def image_preview(self, obj):
        if obj.visuel:
            return format_html('<img src="{}" style="width: 80px; height:80px;" />'.format(obj.visuel.url))
        return ""
    image_preview.short_description = 'Visuel contact'


#FAQ :
#   - question
#   - réponse
#   - ordre
#   - faqcategorie
@admin.register(Faqcategorie)
class FaqcategorieAdmin(admin.ModelAdmin):
    list_display = ('categorie',)
    search_fields = ('categorie',)

@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('question', 'reponse','ordre','categorie')
    search_fields = ('question',)
