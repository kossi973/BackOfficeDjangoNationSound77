from django.db import models

# Create your models here.
class Calendrier(models.Model):
    jour_festival = models.IntegerField(unique=True)
    date_festival = models.DateField(unique=True)

    def __str__(self):
        return f"Jour {self.jour_festival} - {self.date_festival.strftime('%d/%m/%Y')}"
    class Meta:
        ordering = ['jour_festival']


class Style(models.Model):
    style = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.style        
    class Meta:
        ordering = ['style']


class Artiste(models.Model):
    nom = models.CharField(max_length=50, unique=True)
    style = models.ForeignKey(Style, on_delete=models.PROTECT)
    description = models.CharField(max_length=300, null=True, blank=True)
    visuel = models.ImageField(upload_to='artiste_images/', null=True, blank=True)

    def __str__(self):
        return f"{self.nom} / {self.style}"    
    class Meta:
        ordering = ['nom']
    

class Event(models.Model):
    event = models.CharField(max_length=50)

    def __str__(self):
        return self.event
    class Meta:
        ordering = ['event']


class Scene(models.Model):
    scene = models.IntegerField(unique=True)

    def __str__(self):
        return f"{self.scene}"  
    class Meta:
        verbose_name = "Scène"
        verbose_name_plural = "Scènes"
        ordering = ['scene']


class Programme(models.Model):
    calendrier = models.ForeignKey(Calendrier, on_delete=models.CASCADE)
    horaire = models.TimeField()
    artiste = models.ForeignKey(Artiste, blank=True, null=True, on_delete=models.SET_NULL)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    scene = models.ForeignKey(Scene, on_delete=models.CASCADE)

    def __str__(self):
        return self.event.event
    
    class Meta:
        ordering = ['calendrier', 'horaire']


#Model du POI
class CategoriePoi(models.Model):
    categoriePoi = models.CharField(max_length=20)
    urlPoi = models.URLField()

    def __str__(self):
        return self.categoriePoi
    class Meta:
        ordering = ['categoriePoi']


class Poi(models.Model):
    nomPoi = models.CharField(max_length=50)
    categoriePoi = models.ForeignKey(CategoriePoi, on_delete=models.CASCADE)
    descriptionPoi = models.CharField(max_length=150, blank=True, null=True)
    latitudePoi = models.DecimalField(max_digits=20, decimal_places=18)
    longitudePoi = models.DecimalField(max_digits=20, decimal_places=18)

    def __str__(self):
        return self.nomPoi
    class Meta:
        ordering = ['nomPoi']

#Model du Message urgent
class MessageUrgent(models.Model):
    msgUrgent = models.CharField(max_length=100)
    prioriteMsg = models.IntegerField(default=1)

    def __str__(self):
        return self.msgUrgent
    class Meta:
        verbose_name_plural = "Messages urgents"
        ordering = ['prioriteMsg','msgUrgent']

#Model de Information
class Information(models.Model):
    information = models.CharField(max_length=100)
    prioriteInfo = models.IntegerField(default=1)

    def __str__(self):
        return self.information
    class Meta:
        ordering = ['prioriteInfo','information']


class ImageCarrousel(models.Model):
    image = models.ImageField(upload_to='carrousel_images/')
    prioriteImage = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.prioriteImage}"   
    class Meta:
        verbose_name_plural = "Images Carrousel"
        ordering = ['prioriteImage']