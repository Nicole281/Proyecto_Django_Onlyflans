# Generated by Django 5.1 on 2024-08-24 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miweb', '0002_alter_flan_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flan',
            name='slug',
            field=models.SlugField(),
        ),
    ]
