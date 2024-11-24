from django.shortcuts import render
from .models import Partenaire

# Create your views here.
def faq(request):
    return render(request, "ecransReact/faq.html")

def contacts(request):
    return render(request, "ecransReact/contacts.html")

def partenaires(request):
    partenaires = Partenaire.objects.all()
    return render(request, "ecransReact/partenaires.html", context={"partenaires": partenaires})