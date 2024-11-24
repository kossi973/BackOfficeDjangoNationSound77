from django.db import models

# Create your models here.

#Partenaire :
#   - nom
#   - description
#   - visuel
#   - categorie
class Partenairecategorie(models.Model):
    categorie = models.CharField(max_length=50)

    def __str__(self):
        return self.categorie  
    class Meta:
        ordering = ['categorie']

class Partenaire(models.Model):
    nom = models.CharField(max_length=30)
    description = models.TextField(max_length=100, blank=True)
    visuel = models.ImageField(upload_to='partenaires_images/')
    categorie = models.ForeignKey(Partenairecategorie, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom  
    class Meta:
        ordering = ['categorie','nom']


#Mentions Légales :
#   - titre
#   - mention
#   - ordre
class MentionLegale(models.Model):
    titre = models.CharField(max_length=30)
    mention = models.TextField(max_length=1000)
    ordre = models.IntegerField(default=1)

    def __str__(self):
        return self.titre  
    class Meta:
        verbose_name_plural = "Mentions Légales"
        ordering = ['ordre','titre']


#Contact :
#   - visuel
#   - nom
#   - adresse
#   - horaires ouverture
#   - @mail
#   - telephone
class Contact(models.Model):
    visuel = models.ImageField(upload_to='contacts_images/', blank=True, null=True)
    nom = models.CharField(max_length=30)
    adresse = models.CharField(max_length=100)
    horaires = models.CharField(max_length=100)
    mail = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50)

    def __str__(self):
        return self.nom  
    class Meta:
        ordering = ['nom']


#FAQ :
#   - question
#   - réponse
#   - ordre
#   - categorie
class Faqcategorie(models.Model):
    categorie = models.CharField(max_length=50)

    def __str__(self):
        return self.categorie  
    class Meta:
        ordering = ['categorie']

class Faq(models.Model):
    question = models.CharField(max_length=50)
    reponse = models.TextField(max_length=1000)
    ordre = models.IntegerField(default=1)
    categorie = models.ForeignKey(Faqcategorie, on_delete=models.CASCADE)

    def __str__(self):
        return self.question  
    class Meta:
        ordering = ['ordre',]        