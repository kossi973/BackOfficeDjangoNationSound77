from rest_framework import serializers
from .models import Style, Artiste, Calendrier, Scene, Programme, Event
from .models import CategoriePoi, Poi
from .models import MessageUrgent

class CalendrierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendrier
        fields = ['id', 'jour_festival', 'date_festival']

class StyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Style
        fields = ['id', 'style']

class ArtisteSerializer(serializers.ModelSerializer):
    style = serializers.CharField(source='style.style')

    class Meta:
        model = Artiste
        fields = ['id', 'nom', 'style', 'description', 'visuel']
    
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'event']

class SceneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scene
        fields = ['id', 'scene']

class ProgrammeSerializer(serializers.ModelSerializer):
    jour_festival = serializers.IntegerField(source='calendrier.jour_festival')
    date_festival = serializers.DateField(source='calendrier.date_festival')
    event = serializers.CharField(source='event.event')
    artiste = ArtisteSerializer()
    scene = serializers.IntegerField(source='scene.scene')

    class Meta:
        model = Programme
        fields = ['id', 'jour_festival', 'date_festival', 'event', 'artiste', 'scene', 'horaire']


class CategoriePoiSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriePoi
        fields = ['id', 'categoriePoi', 'urlPoi']

class PoiSerializer(serializers.ModelSerializer):
    categoriePoi = serializers.CharField(source='categoriePoi.categoriePoi')
    urlPoi = serializers.URLField(source='categoriePoi.urlPoi')

    class Meta:
        model = Poi
        fields = ['id', 'nomPoi', 'categoriePoi', 'urlPoi', 'descriptionPoi', 'latitudePoi', 'longitudePoi']


class MessageUrgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageUrgent
        fields = ['id', 'msgUrgent', 'prioriteMsg']