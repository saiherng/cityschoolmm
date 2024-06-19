from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField, StreamField

# import MultiFieldPanel:
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.fields import StreamField


from base import blocks

class ContactsIndexPage(Page):
    
    header_title = models.CharField(max_length=100, null=True, blank=True)
    subtitle = models.CharField(max_length=100, null=True, blank=True)

    school_locations = StreamField(

        [   
            ("locations", blocks.LocationDetailsBlock())
         
        ],
        null=True,
        blank=True,)

    content_panels = Page.content_panels + [

        FieldPanel("header_title"),
        FieldPanel("subtitle"),
        FieldPanel("school_locations")

    ]



