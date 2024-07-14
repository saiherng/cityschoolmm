from django.db import models


from wagtail.models import Page, Orderable
from modelcluster.fields import ParentalKey
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel, PageChooserPanel

from base import blocks
from base.blocks import BaseStreamBlock, RichTextBlock


class AboutUsIndexPage(Page):


    header_title = models.CharField(max_length=100, null=True, blank=True)
    header_subtitle = models.CharField(max_length=100, null=True, blank=True)
    header_image = models.ImageField(null=True,blank=True)

    mission_statement = StreamField(
        BaseStreamBlock(), verbose_name="Page body", blank=True, use_json_field=True
    )


    founder_section_title = models.CharField(
        blank=True,
        max_length=255, help_text="Enter Founder's Name"
    )

    founder_name = models.CharField(
        blank=True,
        max_length=255, help_text="Enter Founder's Name"
    )
    founder_title = models.CharField(
        blank=True,
        max_length=255,
        help_text="Enter founder's title",
    )
    founder_description = models.TextField(
        blank=True,
        max_length=522,
        help_text="Enter founder's title",
    )

    founder_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Founder's image",
    )

    
    staff_cards = StreamField(
        [   
            ("cards", blocks.CardsBlock())           
        ],
        null=True,
        blank=True,)
    

    gallery_heading = models.CharField(max_length=255, blank=True)
    gallery_subheading = models.CharField(blank=True, max_length=255)

    content_panels = Page.content_panels + [
        
        MultiFieldPanel([
            FieldPanel("header_title"),
            FieldPanel("header_subtitle"),
            FieldPanel("header_image"),

        ], heading="Header Details"),
        FieldPanel("mission_statement"),

        MultiFieldPanel([
            FieldPanel("founder_section_title"),
            FieldPanel("founder_name"),
            FieldPanel("founder_title"),
            FieldPanel("founder_image"),
            FieldPanel("founder_description"),
        ], heading="Founder Details"),
        FieldPanel("staff_cards"),

        MultiFieldPanel([
            FieldPanel("gallery_heading"),
            FieldPanel("gallery_subheading"),
            InlinePanel('gallery_images', label="Gallery images")
        ], heading="About Us Gallery")

    ]


class AboutUsGalleryImage(Orderable):

    page = ParentalKey(AboutUsIndexPage, on_delete=models.CASCADE, related_name='gallery_images')

    

    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=255)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption')
    ]

