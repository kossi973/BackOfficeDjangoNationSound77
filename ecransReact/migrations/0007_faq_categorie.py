# Generated by Django 5.1.3 on 2024-11-24 18:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecransReact', '0006_faqcategorie_alter_faq_options_faq_ordre'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='categorie',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ecransReact.faqcategorie'),
            preserve_default=False,
        ),
    ]
