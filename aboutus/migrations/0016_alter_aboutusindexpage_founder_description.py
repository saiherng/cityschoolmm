# Generated by Django 5.0.6 on 2024-06-30 08:04

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus', '0015_alter_aboutusindexpage_founder_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutusindexpage',
            name='founder_description',
            field=wagtail.fields.RichTextField(blank=True),
        ),
    ]
