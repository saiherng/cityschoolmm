from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField

# import MultiFieldPanel:
from wagtail.admin.panels import FieldPanel, MultiFieldPanel


class HomePage(Page):
    # add the Hero section of HomePage:
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Homepage image",
    )
    hero_heading = models.CharField(
        blank=True,
        max_length=255, help_text="Write an introduction for the site"
    )

    hero_subheading = models.CharField(
        blank=True,
        max_length=255, help_text="Write sub heading for the site"
    )
    hero_cta1 = models.CharField(
        blank=True,
        verbose_name="Hero CTA 1",
        max_length=255,
        help_text="Text to display on Call to Action",
    )
    hero_cta1_link = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Hero CTA link 1",
        help_text="Choose a page to link to for the Call to Action",
    )
    hero_cta2 = models.CharField(
        blank=True,
        verbose_name="Hero CTA 2",
        max_length=255,
        help_text="Text to display on Call to Action",
    )

    hero_cta2_link = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Hero CTA link 2",
        help_text="Choose a page to link to for the Call to Action",
    )


    # modify your content_panels:
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("image"),
                FieldPanel("hero_heading"),
                FieldPanel("hero_subheading"),
                FieldPanel("hero_cta1"),
                FieldPanel("hero_cta1_link"),
                FieldPanel("hero_cta2"),
                FieldPanel("hero_cta2_link"),
            ],
            heading="Hero section",
        )
    ]