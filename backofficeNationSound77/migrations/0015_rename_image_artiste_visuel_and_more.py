# Generated by Django 5.1.3 on 2024-11-12 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backofficeNationSound77', '0014_alter_poi_descriptionpoi'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artiste',
            old_name='image',
            new_name='visuel',
        ),
        migrations.AlterField(
            model_name='categoriepoi',
            name='urlPoi',
            field=models.URLField(),
        ),
    ]