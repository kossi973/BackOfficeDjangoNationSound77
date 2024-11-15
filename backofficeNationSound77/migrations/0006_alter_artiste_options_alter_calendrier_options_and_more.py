# Generated by Django 5.1.3 on 2024-11-11 16:52

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backofficeNationSound77', '0005_alter_event_artiste'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artiste',
            options={'ordering': ['nom']},
        ),
        migrations.AlterModelOptions(
            name='calendrier',
            options={'ordering': ['no_jour']},
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['event']},
        ),
        migrations.AlterModelOptions(
            name='scene',
            options={'ordering': ['scene'], 'verbose_name': 'Scène', 'verbose_name_plural': 'Scènes'},
        ),
        migrations.AlterModelOptions(
            name='style',
            options={'ordering': ['style']},
        ),
        migrations.RemoveField(
            model_name='event',
            name='artiste',
        ),
        migrations.AddField(
            model_name='artiste',
            name='description',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='programme',
            name='artiste',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='backofficeNationSound77.artiste'),
        ),
    ]
