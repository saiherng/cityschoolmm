# Generated by Django 5.0.6 on 2024-07-14 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus', '0020_aboutusindexpage_mission_statement'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutusindexpage',
            name='mission_header',
            field=models.CharField(default='Our Mission', max_length=100),
        ),
    ]
