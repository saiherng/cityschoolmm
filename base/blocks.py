from wagtail.blocks import (
    CharBlock,
    ChoiceBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    TextBlock,
)
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail import blocks



class CardsBlock(StructBlock):

    title = blocks.CharBlock(required=True, help_text="Section Title")
    subtitle = blocks.TextBlock(required=True, help_text="Section Subtitle")

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ('image', ImageChooserBlock(required=True, help_text="Card Image")),
                ('name', CharBlock(required=True, help_text="Input Name")),
                ('subtitle', CharBlock(required=True, help_text="Card Subtitle")),
            ]
        )
    )

    class Meta:
        template = "blocks/cards_block.html"
        icon= "placeholder"
        label = "Add Cards Section "

class FaqsBlock(StructBlock):
    """ AccordionBlock"""

    title = blocks.CharBlock(required=True, help_text="FAQ Section Title")
    subtitle = blocks.TextBlock(required=False, help_text="FAQ Section Subtitle")

    faqs = blocks.ListBlock(
        blocks.StructBlock(
            [
                ('question', TextBlock(required=True, help_text="Input Question")),
                ('answer', TextBlock(required=True, help_text="Input Question"))
            ]
        )
    )
   

    class Meta:
        template = "blocks/faqs_block.html"
        icon= "placeholder"
        label = "Add FAQ "

class LocationDetailsBlock(StructBlock):
    """Information of School"""

    school_branch = blocks.CharBlock(required=True, help_text="CitySchool Branch ex: 'Yangon', 'Taunggyi'")
    image= ImageChooserBlock(required=True, help_text="Campus Image")
    image_caption = blocks.CharBlock(required=False, help_text="Campus Image Caption")
    phone_number = blocks.CharBlock(required=False, help_text="Input Phone Number")
    email = blocks.EmailBlock(required=False, help_text="Input School Email")
    location = blocks.TextBlock(required=True, help_text="Address of School")
    social_media_url = blocks.URLBlock(required=False, help="Social Media URL")
    
    background = blocks.ChoiceBlock( choices=[
        ('#ffffff','Light'),
        ('#10335b', 'Dark')
    ], required=True, help="Select background theme"
    )

    class Meta:
        template = "blocks/location_details_block.html"
        icon= "placeholder"
        label = "Add New School Location Details"

class HeroFeaturesBlock(StructBlock):

    row_align = blocks.ChoiceBlock( choices=[
        ('flex-row','Row Left'),
        ('flex-row-reverse', 'Row Right'),
    ], required=True, help="Select Row Align"
    
    ) 
    title = blocks.CharBlock(required=True, help_text="Block Section Title")
    title_text_align = blocks.ChoiceBlock( choices=[
        ('text-start','Text Left'),
        ('text-center', 'Text Center'),
        ('text-end', 'Text Right')
    ], required=True, help="Select Text Alignment"
    
    )
    subtitle = blocks.TextBlock(required=True, help_text="Block Section Subtitle")
    image = ImageChooserBlock(required=True)


    features = blocks.ListBlock(
        blocks.StructBlock(
            [   
                ('title', TextBlock(required=True, help_text="Input Feature Title")),
                ('description', TextBlock(required=True, help_text="Input Feature Description")),
                ('icon', ImageChooserBlock(required=False))
            ],  max_num=4
        )
    )

    

    class Meta:
        template = "blocks/hero_features_block.html"
        icon= "placeholder"
        label = "Add New Feature Block"

class ImageBlock(StructBlock):
    """
    Custom `StructBlock` for utilizing images with associated caption and
    attribution data
    """

    image = ImageChooserBlock(required=True)
    caption = CharBlock(required=False)
    attribution = CharBlock(required=False)

    class Meta:
        icon = "image"
        template = "blocks/image_block.html"

class HeadingBlock(StructBlock):
    """
    Custom `StructBlock` that allows the user to select h2 - h4 sizes for headers
    """

    heading_text = CharBlock(classname="title", required=True)
    size = ChoiceBlock(
        choices=[
            ("", "Select a header size"),
            ("h1", "H1"),
            ("h2", "H2"),
            ("h3", "H3"),
            ("h4", "H4"),
        ],
        blank=True,
        required=False,
    )

    class Meta:
        icon = "title"
        template = "blocks/heading_block.html"

class BlockQuote(StructBlock):
    """
    Custom `StructBlock` that allows the user to attribute a quote to the author
    """

    text = TextBlock()
    attribute_name = CharBlock(blank=True, required=False, label="e.g. Mary Berry")

    class Meta:
        icon = "openquote"
        template = "blocks/blockquote.html"

class ButtonBlock(StructBlock):

    """
    Custom button block that allows users to add a link to another page.
    """
    
    title = blocks.CharBlock(required=True, help_text="Button Title")
    
    button_url = blocks.PageChooserBlock(required=True, help="Choose Link To Internal Page")

    class Meta:
        icon = "edit"
        template = "blocks/button_block.html"

# StreamBlocks
class BaseStreamBlock(StreamBlock):
    """
    Define the custom blocks that `StreamField` will utilize
    """

    heading_block = HeadingBlock()
    paragraph_block = RichTextBlock(
        icon="pilcrow", template="blocks/paragraph_block.html"
    )
    image_block = ImageBlock()
    block_quote = BlockQuote()
    embed_block = EmbedBlock(max_width=800, max_height=400,
        help_text="Insert an embed URL e.g https://www.youtube.com/watch?v=SGJFWirQ3ks",
        icon="media",
        template="blocks/embed_block.html",
    )
    button_block = ButtonBlock()


class ImageGalleryBlock(StructBlock):

    title = blocks.CharBlock(required=True, help_text="Gallery title")
    subtitle = blocks.CharBlock(required=False, help_text="Gallery Subittle")
    images = blocks.ListBlock(ImageChooserBlock(), help_text="Select images for the gallery")

    class Meta:
        template = "blocks/image_gallery_block.html"
        icon = "image"
        label = "Image Gallery"




