# Generated by Django 5.1.3 on 2024-11-11 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backofficeNationSound77', '0006_alter_artiste_options_alter_calendrier_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artiste',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]