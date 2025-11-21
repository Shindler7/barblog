from typing import Optional

from django.db import models
from modelcluster.fields import ParentalKey
from wagtail import blocks
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField, StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.models import Image
from wagtail.models import Page, Orderable
from wagtailcodeblock.blocks import CodeBlock


class HomePage(Page):
    """
    Заглавная страница блога.
    """

    intro = RichTextField(blank=True)

    def get_context(self, request, *args, **kwargs):
        """Уточнение контекста по выдаче информации."""

        context = super().get_context(request)
        blogpages = (self
                     .get_children()
                     .live()
                     .order_by('-first_published_at', '-id'))
        context['blogpages'] = blogpages

        return context


class ArticlePage(Page):
    """
    Отдельная страница записи в блоге.
    """

    date = models.DateField("дата")
    intro = models.CharField(max_length=250)

    body = StreamField([
        ('rich_text', blocks.RichTextBlock(
            features=[
                'h2', 'h3', 'h4',
                'bold', 'italic', 'underline',
                'code', 'blockquote',
                'ol', 'ul',
                'link', 'image',
                'hr',
            ],
            label='Текст'
        )),
        ('code', CodeBlock(label='Блок кода')),
        ('image', ImageChooserBlock(label='Изображение')),
        ('quote', blocks.BlockQuoteBlock(label='Цитата')),
    ], blank=True, use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body'),
        'gallery_images',
    ]

    def hero_image(self) -> Optional[Image]:
        """ Возвращает главную иллюстрацию, при наличии """

        gallery_item = self.gallery_images.first()  # noqa: F821
        if gallery_item:
            return gallery_item.image

    def has_hero_image(self) -> bool:
        """ Есть хотя бы одна главная иллюстрация записи? """

        return self.gallery_images.exists()  # noqa: F821


class ArticlePageGalleryImage(Orderable):
    """
    Представление изображений в записях.
    """

    page = ParentalKey(ArticlePage,
                       related_name='gallery_images',
                       on_delete=models.CASCADE)
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+')
    caption = models.CharField(max_length=250, blank=True)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]
