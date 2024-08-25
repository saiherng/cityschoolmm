from django.db import models
from django import forms

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField, StreamField

from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel, PageChooserPanel

from wagtail.search import index
from wagtail.snippets.models import register_snippet

from base import blocks
from base.blocks import BaseStreamBlock, JumbotronBlock

from wagtail import blocks
from wagtail.blocks import PageChooserBlock

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


# keep the definition of BlogIndexPage model, and add the BlogPage model:

class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'BlogPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )


class BlogPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=322, verbose_name="intro")
    body = StreamField(
        [
        ('base', BaseStreamBlock(verbose_name="body", blank=True, use_json_field=True)),
        ('jumbotron', JumbotronBlock()),
        

        ]
    )

    authors = ParentalManyToManyField('blog.Author', blank=True, verbose_name='authors')

    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
        index.SearchField('authors'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('authors', widget=forms.CheckboxSelectMultiple),
            FieldPanel('tags'),

        ], heading="Blog information"),
        FieldPanel('intro'),
        FieldPanel('body'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]


class BlogPageGalleryImage(Orderable):
    page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True,null=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]

class BlogTagIndexPage(Page):
    def get_context(self, request):

        # Filter by tag
        tag = request.GET.get('tag')
        blogpages = BlogPage.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context['blogpages'] = blogpages
        return context


@register_snippet
class Author(models.Model):
    name = models.CharField(max_length=255)
    author_image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('author_image'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Authors'



class BlogIndexPage(Page):

    header_title = models.CharField(max_length=100, null=True, blank=True)
    header_subtitle = models.CharField(max_length=100, null=True, blank=True)
    header_image = models.ImageField(null=True,blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('header_title'),
        FieldPanel('header_subtitle'),
        FieldPanel('header_image'),
        InlinePanel('featured_blogs', label="Featured Blogs"),
    ]

    subpage_types = [ 'blog.BlogPage'
       
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        
         #paginator
        paginator = Paginator(blogpages, 3)
        # Try to get the ?page=x value
        page = request.GET.get("page")
        try:
            # If the page exists and the ?page=x is an int
            blogpages = paginator.page(page)
        except PageNotAnInteger:
            # If the ?page=x is not an int; show the first page
            blogpages = paginator.page(1)
        except EmptyPage:
            # If the ?page=x is out of range (too high most likely)
            # Then return the last page
            blogpages = paginator.page(paginator.num_pages)

        # "posts" will have child pages; you'll need to use .specific in the template
        # in order to access child properties, such as youtube_video_id and subtitle
        
        context['blogpages'] = blogpages
        return context
    



class FeaturedBlogs(Orderable):

   page = ParentalKey(BlogIndexPage, on_delete=models.CASCADE, related_name='featured_blogs')

   featured_blog = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
   panels = [
        PageChooserPanel('featured_blog','blog.BlogPage'),
    ]