# Generated by Django 5.0.6 on 2024-07-27 19:51

import wagtail.blocks
import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_homepagelocation_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='faqs',
            field=wagtail.fields.StreamField([('faqs', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='FAQ Section Title', required=True)), ('subtitle', wagtail.blocks.TextBlock(help_text='FAQ Section Subtitle', required=False)), ('faqs', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('question', wagtail.blocks.TextBlock(help_text='Input Question', required=True)), ('answer', wagtail.blocks.RichTextBlock(help_text='Input Question', required=True))])))], help_text='Input Frequently Asked Questions'))], blank=True, null=True),
        ),
    ]
