from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField

# import MultiFieldPanel:
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel

from wagtail.fields import StreamField
from base import blocks

# import RichTextField:
from wagtail.fields import RichTextField, StreamField

# import DraftStateMixin, PreviewableMixin, RevisionMixin, TranslatableMixin:
from wagtail.models import (
    DraftStateMixin,
    PreviewableMixin,
    RevisionMixin,
    TranslatableMixin,
)
from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    register_setting,
)
from modelcluster.fields import ParentalKey


# import register_snippet:
from wagtail.snippets.models import register_snippet


from wagtail.admin.panels import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    PublishingPanel,
)
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField

from .blocks import BaseStreamBlock

from django_recaptcha.fields import ReCaptchaField
from django_recaptcha import widgets


from wagtailcaptcha.models import WagtailCaptchaEmailForm

@register_setting
class NavigationSettings(BaseGenericSetting):
    twitter_url = models.URLField(verbose_name="Twitter URL", blank=True)
    github_url = models.URLField(verbose_name="GitHub URL", blank=True)
    mastodon_url = models.URLField(verbose_name="Mastodon URL", blank=True)

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("twitter_url"),
                FieldPanel("github_url"),
                FieldPanel("mastodon_url"),
            ],
            "Social settings",
        )
    ]

@register_snippet
class FooterText(
    DraftStateMixin,
    RevisionMixin,
    PreviewableMixin,
    TranslatableMixin,
    models.Model,
):

    body = RichTextField()

    panels = [
        FieldPanel("body"),
        PublishingPanel(),
    ]

    def __str__(self):
        return "Footer text"

    def get_preview_template(self, request, mode_name):
        return "base.html"

    def get_preview_context(self, request, mode_name):
        return {"footer_text": self.body}

    class Meta(TranslatableMixin.Meta):
        verbose_name_plural = "Footer Text"


class FormField(AbstractFormField):
    """
    Wagtailforms is a module to introduce simple forms on a Wagtail site. It
    isn't intended as a replacement to Django's form support but as a quick way
    to generate a general purpose data-collection form or contact form
    without having to write code. We use it on the site for a contact form. You
    can read more about Wagtail forms at:
    https://docs.wagtail.org/en/stable/reference/contrib/forms/index.html
    """
    page = ParentalKey("FormPage", related_name="form_fields", on_delete=models.CASCADE)



class FormPage(WagtailCaptchaEmailForm):
  
  
    intro = RichTextField(blank=True)
    body = StreamField(BaseStreamBlock(), use_json_field=True, null=True)
    
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro'),

        InlinePanel("form_fields", heading="Form fields", label="Field"),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]


class StandardPage(Page):

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
        FieldPanel("body"),

    ]




