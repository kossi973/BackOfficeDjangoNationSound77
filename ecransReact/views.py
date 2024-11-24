from django.shortcuts import render
from .models import Contact, Faq, MentionLegale, Partenaire

# Create your views here.
def faq(request):
    return render(request, "ecransReact/faq.html")

def contacts(request):
    return render(request, "ecransReact/contacts.html")

def partenaires(request):
    partenaires = Partenaire.objects.all()
    return render(request, "ecransReact/partenaires.html", context={"partenaires": partenaires})

def mentionslegales(request):
    mentionslegales = MentionLegale.objects.all()
    return render(request, "ecransReact/mentionslegales.html", context={"mentionslegales": mentionslegales})

def contacts(request):
    contacts = Contact.objects.all()
    return render(request, "ecransReact/contacts.html", context={"contacts": contacts})

def faq(request):
    faq = Faq.objects.all()
    return render(request, "ecransReact/faq.html", context={"faq": faq})