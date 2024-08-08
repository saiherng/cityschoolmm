from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel


from base import blocks
from base.blocks import BaseStreamBlock, RichTextBlock

from wagtail.images.blocks import ImageChooserBlock

class AcademicsIndexPage(Page):

    header_title = models.CharField(max_length=255, null=True, blank=True)
    header_subtitle = models.CharField(max_length=255, null=True, blank=True)
    header_image = models.ImageField(null=True,blank=True)

    subject_section_title = models.CharField(max_length=100, null=True, blank=True)
    subject_section_subtitle = models.CharField(max_length=255, null=True, blank=True)

    programs_section_title = models.CharField(blank=True, max_length=255)
    programs_section_subtitle = models.CharField(blank=True, max_length=255)
    programs_section_image = models.ForeignKey(
        'wagtailimages.Image', blank=True, null=True, on_delete=models.SET_NULL, related_name='+'
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

    content_panels = Page.content_panels + [

        MultiFieldPanel(
            [
                FieldPanel("header_title"),
                FieldPanel("header_subtitle"),
                FieldPanel("header_image"),
            ],
            heading="Main Header Section",
        ),
         MultiFieldPanel(
            [
                FieldPanel("programs_section_title"),
                FieldPanel("programs_section_subtitle"),
                FieldPanel("programs_section_image"),
                InlinePanel('programs', label="Add School Programs")
            ],
            heading="Programs List ", 
        ),
        FieldPanel('body'),

        MultiFieldPanel(
            [
                FieldPanel("subject_section_title"),
                FieldPanel("subject_section_subtitle"),
                InlinePanel('subjects', label="Add School Subjects")
            ],
            heading="Subjects List ", 
        ),

    ]

    subpage_types = [ 'base.StandardPage','base.FormPage'
    ]

class AcademicsPrograms(Orderable):

    page = ParentalKey(AcademicsIndexPage, on_delete=models.CASCADE, related_name='programs')
    
    program_title = models.CharField(blank=True, max_length=255)
    program_description = models.TextField(blank=True, max_length=255)
    
    panels = [
        FieldPanel('program_title'),
        FieldPanel('program_description'),
    ]


class AcademicsSubjectList(Orderable):

    page = ParentalKey(AcademicsIndexPage, on_delete=models.CASCADE, related_name='subjects')
    subject_icon = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )

    subject_title = models.CharField(blank=True, max_length=255)

