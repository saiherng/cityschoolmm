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
    header_image = models.ImageField(null=True, blank=True)

    school_locations = StreamField(

        [   
            ("locations", blocks.LocationDetailsBlock())
         
        ],
        null=True,
        blank=True,)

    content_panels = Page.content_panels + [

        FieldPanel("header_title"),
        FieldPanel("header_subtitle"),
        FieldPanel("header_image"),
        FieldPanel("school_locations")

    ]

    subpage_types = [ 'base.StandardPage' ,'base.FormPage'
    ]


