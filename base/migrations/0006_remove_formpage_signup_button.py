# Generated by Django 5.0.6 on 2024-06-21 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_formpage_signup_button'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formpage',
            name='signup_button',
        ),
    ]
