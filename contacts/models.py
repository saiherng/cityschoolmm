from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField

# import MultiFieldPanel:
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel

class ContactsIndexPage(Page):
    
    phone_number = models.CharField(max_length=250)
    address = models.TextField(help_text="Address Field", blank=True)
    email = models.EmailField(max_length= 250)
    page_url = models.URLField(help_text="Social Media Page URL")

    
    content_panels = Page.content_panels + [
        MultiFieldPanel
            [
                FieldPanel("phone_number"),
                FieldPanel("email"),
                FieldPanel("address"),
                FieldPanel("page_url")

            ],
    ]



