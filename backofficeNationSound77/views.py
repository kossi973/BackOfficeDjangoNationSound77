from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Style, Artiste, Calendrier, Scene, Programme, Event
from .models import CategoriePoi, Poi
from .models import MessageUrgent
from .serializers import StyleSerializer, ArtisteSerializer, CalendrierSerializer, SceneSerializer, ProgrammeSerializer, EventSerializer
from .serializers import CategoriePoiSerializer, PoiSerializer
from .serializers import MessageUrgentSerializer


class StyleViewSet(viewsets.ModelViewSet):
    queryset = Style.objects.all()
    serializer_class = StyleSerializer

class ArtisteViewSet(viewsets.ModelViewSet):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer

class CalendrierViewSet(viewsets.ModelViewSet):
    queryset = Calendrier.objects.all()
    serializer_class = CalendrierSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class SceneViewSet(viewsets.ModelViewSet):
    queryset = Scene.objects.all()
    serializer_class = SceneSerializer

class ProgrammeViewSet(viewsets.ModelViewSet):
    queryset = Programme.objects.all()
    serializer_class = ProgrammeSerializer


class CategoriePoiViewSet(viewsets.ModelViewSet):
    queryset = CategoriePoi.objects.all()
    serializer_class = CategoriePoiSerializer

class PoiViewSet(viewsets.ModelViewSet):
    queryset = Poi.objects.all()
    serializer_class = PoiSerializer

class MessageUrgentViewSet(viewsets.ModelViewSet):
    queryset = MessageUrgent.objects.all()
    serializer_class = MessageUrgentSerializer