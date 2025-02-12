# Generated by Django 5.0.6 on 2024-06-19 07:52

import django.db.models.deletion
import modelcluster.fields
import wagtail.blocks
import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_homepagefaqs'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepagefaqs',
            name='page',
            field=modelcluster.fields.ParentalKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='faqs', to='home.homepage'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='homepagefaqs',
            name='faqs',
            field=wagtail.fields.StreamField([('faqs', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='FAQ Section Title', required=True)), ('subtitle', wagtail.blocks.TextBlock(help_text='FAQ Section Subtitle', required=False)), ('faqs', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('question', wagtail.blocks.TextBlock(help_text='Input Question', required=True)), ('answer', wagtail.blocks.TextBlock(help_text='Input Question', required=True))])))], help_text='Input Frequently Asked Questions'))], blank=True, null=True),
        ),
    ]
