# Generated by Django 5.1.3 on 2024-11-24 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecransReact', '0010_alter_mentionlegale_ordre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentionlegale',
            name='ordre',
            field=models.IntegerField(default=1),
        ),
    ]
