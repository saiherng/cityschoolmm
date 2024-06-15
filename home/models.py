from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField

# import MultiFieldPanel:
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel


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
        ),
        InlinePanel('gallery_images', label="Gallery University and Agencies Logo")
        
    ]

class HomePageLogoGallery(Orderable):

    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='gallery_images')

    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]
