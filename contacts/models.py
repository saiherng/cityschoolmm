from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField, StreamField

# import MultiFieldPanel:
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel

from base import blocks


class ContactsIndexPage(Page):
    
    header_title = models.CharField(max_length=100, null=True, blank=True)
    header_subtitle = models.CharField(max_length=100, null=True, blank=True)
    
    body = StreamField(

        [   
            ('base', blocks.BaseStreamBlock()),
            ('hero_feature', blocks.HeroFeaturesBlock()),
            ('hero_basic', blocks.HeroBasicBlock()),
            ('carousel', blocks.ImageCarouselBlock()),
            ('image_gallery', blocks.ImageGalleryBlock()),
            ('jumbotron', blocks.JumbotronBlock()),
            ("locations", blocks.LocationDetailsBlock())
         
        ],
        null=True,
        blank=True,)

    content_panels = Page.content_panels + [

        FieldPanel("header_title"),
        FieldPanel("header_subtitle"),
        FieldPanel("body")

    ]

    subpage_types = [ 'base.StandardPage' ,'base.FormPage'
    ]


