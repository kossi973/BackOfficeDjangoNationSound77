# Generated by Django 5.1.3 on 2024-11-12 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backofficeNationSound77', '0008_categoriepoi_listepoi_alter_artiste_description'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ListePOI',
            new_name='NomPoi',
        ),
        migrations.RemoveField(
            model_name='categoriepoi',
            name='imagePoi',
        ),
    ]
