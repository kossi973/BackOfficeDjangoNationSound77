# Generated by Django 5.1.3 on 2024-11-12 08:34

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backofficeNationSound77', '0009_rename_listepoi_nompoi_remove_categoriepoi_imagepoi'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoriepoi',
            name='urlPoi',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
    ]
