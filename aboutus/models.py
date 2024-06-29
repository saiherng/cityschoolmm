from django.db import models


from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel

from base import blocks

class AboutUsIndexPage(Page):
    intro = RichTextField(blank=True)

    
    staff_cards = StreamField(

        [   
            ("cards", blocks.CardsBlock())
         
        ],
        null=True,
        blank=True,)

    content_panels = Page.content_panels + [

        FieldPanel("intro"),
        FieldPanel("staff_cards")

    ]

