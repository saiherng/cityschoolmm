from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField

# import MultiFieldPanel:
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel

from wagtail.fields import StreamField

from base import blocks
from base.blocks import BaseStreamBlock, RichTextBlock


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

    program_section_heading = models.CharField(
        blank=True,
        max_length=255, help_text="Feature Section Title"
    )

    program_section_subheading = models.CharField(
        blank=True,
        max_length=255, help_text="Feature Section Subheading"
    )

    program_section_description = models.CharField(
        blank=True,
        max_length=255, help_text="Feature Section Subheading"
    )

    body = StreamField([

        ('base', BaseStreamBlock()),
        ('hero_feature', blocks.HeroFeaturesBlock()),
        ('hero_basic', blocks.HeroBasicBlock()),
        ('carousel', blocks.ImageCarouselBlock()),
        ('image_gallery', blocks.ImageGalleryBlock()),
        ('jumbotron', blocks.JumbotronBlock()),
    ],  null=True,
        blank=True)


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
        InlinePanel('locations', label="School Branch Locations"),


        InlinePanel('gallery_images', label="Logo Gallery of University and Agencies"),
        MultiFieldPanel(
            [
                FieldPanel("feature_section_heading"),
                FieldPanel("feature_section_subheading"),
                InlinePanel('features', label="Add school features",max_num=4)
            ],
            heading="Features Section- ex. Reasons to Choose Us ", 
        ),
        MultiFieldPanel(
            [
                FieldPanel("program_section_heading"),
                FieldPanel("program_section_subheading"),
                FieldPanel("program_section_description"),
                InlinePanel('programs', label="Add school programs")
            ],
            heading="Add Programs for all ages ", 
        ),
        FieldPanel('body'),
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

class HomePagePrograms(Orderable):

    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='programs')
    
    program_image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    program_title = models.CharField(blank=True, max_length=255)
    program_age = models.CharField(blank=True, max_length=255)
    program_description = models.TextField(blank=True, max_length=255)

    panels = [
        FieldPanel('program_image'),
        FieldPanel('program_title'),
        FieldPanel('program_age'),
        FieldPanel('program_description'),
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

class HomePageLocation(Orderable):

    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='locations')
    background = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    school_logo = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )

    school_name = models.CharField(blank=True, max_length=255)
    heading = models.CharField(blank=True, max_length=255)
    subheading = models.CharField(blank=True, max_length=255)
    address = models.CharField(blank=True, max_length=255)
    phone = StreamField(
        [
        ('phone', blocks.CharBlock())
    ], null=True, blank=True, block_counts={'phone' : {'max_num': 2},})
    email = models.EmailField(blank=True, max_length=255)

    panels = [
        FieldPanel('background'),
        FieldPanel('school_name'),
        FieldPanel('school_logo'),
        FieldPanel('heading'),
        FieldPanel('subheading'),
        FieldPanel('address'),
        FieldPanel('phone'),
        FieldPanel('email'),
    ]

    
   


