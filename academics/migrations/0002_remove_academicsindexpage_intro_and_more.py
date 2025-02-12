# Generated by Django 5.0.6 on 2024-07-03 19:29

import django.db.models.deletion
import modelcluster.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0001_initial'),
        ('wagtailimages', '0026_delete_uploadedimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='academicsindexpage',
            name='intro',
        ),
        migrations.AddField(
            model_name='academicsindexpage',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='academicsindexpage',
            name='header_subtitle',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='academicsindexpage',
            name='header_title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='academicsindexpage',
            name='subject_section_subtitle',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='academicsindexpage',
            name='subject_section_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='AcademicsSubjectList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('subject_title', models.CharField(blank=True, max_length=255)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='academics.academicsindexpage')),
                ('subject_icon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
