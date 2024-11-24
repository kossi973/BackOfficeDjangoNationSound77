# Generated by Django 5.1.3 on 2024-11-24 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecransReact', '0005_faq'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faqcategorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorie', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['categorie'],
            },
        ),
        migrations.AlterModelOptions(
            name='faq',
            options={'ordering': ['ordre']},
        ),
        migrations.AddField(
            model_name='faq',
            name='ordre',
            field=models.IntegerField(default=1),
        ),
    ]