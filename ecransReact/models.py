from django.db import models

# Create your models here.

#Partenaire :
#   - nom
#   - description
#   - visuel

class Partenaire(models.Model):
    nom = models.CharField(max_length=30)
    description = models.TextField(max_length=100, blank=True)
    visuel = models.ImageField(upload_to='partenaires_images/')

    def __str__(self):
        return self.nom  
    class Meta:
        ordering = ['nom']
