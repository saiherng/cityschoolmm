from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField

# import MultiFieldPanel:
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel

from wagtail.fields import StreamField
from base import blocks


from blog.models import BlogPage


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


    feature_section_heading = models.CharField(
        blank=True,
        max_length=255, help_text="Feature Section Title"
    )

    feature_section_subheading = models.CharField(
        blank=True,
        max_length=255, help_text="Feature Section Subheading"
    )

    faqs = StreamField(
        [
            ("faqs", blocks.FaqsBlock(help_text="Input Frequently Asked Questions"))
         ],
        null=True,
        blank=True
    )

    def get_context(self, request):
        # Update context to include only published blog pages, ordered by reverse-chron
        context = super().get_context(request)
        context['blog_pages'] = BlogPage.objects.live().order_by('-date')[:3]
        return context
    
    
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
            heading="Main Header Section",
        ),
        InlinePanel('gallery_images', label="Logo Gallery of University and Agencies"),
        MultiFieldPanel(
            [
                FieldPanel("feature_section_heading"),
                FieldPanel("feature_section_subheading"),
                InlinePanel('features', label="Add school features",max_num=4)
            ],
            heading="Features Section- ex. Reasons to Choose Us ", 
        ),

        FieldPanel('faqs')
    ]

class HomePageFeatures(Orderable):

    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='features')
    feature_image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    feature_title = models.CharField(blank=True, max_length=255)
    feature_description = models.TextField(blank=True, max_length=255)

    panels = [
        FieldPanel('feature_image'),
        FieldPanel('feature_title'),
        FieldPanel('feature_description'),
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

