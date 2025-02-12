# Generated by Django 5.0.6 on 2024-07-19 21:14

import django.db.models.deletion
import modelcluster.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0002_remove_academicsindexpage_intro_and_more'),
        ('wagtailimages', '0026_delete_uploadedimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='academicsindexpage',
            name='programs_section_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='academicsindexpage',
            name='programs_section_subtitle',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='academicsindexpage',
            name='programs_section_title',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.CreateModel(
            name='AcademicsPrograms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('program_title', models.CharField(blank=True, max_length=255)),
                ('program_description', models.TextField(blank=True, max_length=255)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='programs', to='academics.academicsindexpage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
