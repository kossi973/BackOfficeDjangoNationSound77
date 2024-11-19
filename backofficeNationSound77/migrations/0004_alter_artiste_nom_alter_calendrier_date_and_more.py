# Generated by Django 5.1.3 on 2024-11-11 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backofficeNationSound77', '0003_remove_event_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artiste',
            name='nom',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='calendrier',
            name='date',
            field=models.DateField(unique=True),
        ),
        migrations.AlterField(
            model_name='calendrier',
            name='no_jour',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='scene',
            name='scene',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='style',
            name='style',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]