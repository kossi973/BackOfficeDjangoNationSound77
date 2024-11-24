from django.urls import path
from .views import faq, contacts, partenaires, mentionslegales

urlpatterns = [
    path('faq/', faq, name="ecranReact-faq"),
    path('contacts/', contacts, name="ecranReact-contacts"),
    path('partenaires/', partenaires, name="ecranReact-partenaires"),
    path('mentionslegales/', mentionslegales, name="ecranReact-mentionslegales"),
    path('contacts/', contacts, name="ecransReact-contacts"),
]