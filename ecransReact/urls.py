from django.urls import path
from .views import faq, contacts, partenaires

urlpatterns = [
    path('faq/', faq, name="ecransReact-faq"),
    path('contacts/', contacts, name="ecransReact-contacts"),
    path('partenaires/', partenaires, name="ecransReact-partenaires"),
]