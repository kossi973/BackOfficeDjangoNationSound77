# Generated by Django 5.1.3 on 2024-11-11 11:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backofficeNationSound77', '0004_alter_artiste_nom_alter_calendrier_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='artiste',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='backofficeNationSound77.artiste'),
        ),
    ]