# Generated by Django 5.1.3 on 2024-11-24 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecransReact', '0003_contact_alter_mentionlegale_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='tel',
            new_name='telephone',
        ),
    ]
