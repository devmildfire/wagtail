from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.snippets.models import register_snippet


@register_snippet
class Footer(models.Model):

    bodyText = RichTextField()

    panels = [
        FieldPanel('bodyText')
    ]

    class Meta:
        verbose_name = 'Футер'
        verbose_name_plural = 'Футеры'

    def __str__(self):
        return "Футер"


class NewsPage(Page):

    # template = 'home'

    pass


class HomePage(Page):

    # subpage_types = ['home.NewsPage']
    # parent_page_types = []

    # Поля в базе данных
    subtitle = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Подзаголовок'
    )

    rtfbody = RichTextField(
        blank=True,
        null=True,
        verbose_name='Расширенное текстовое поле'
    )

    bg_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    # поля для ввода данных в интерфейсе администратора

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('rtfbody'),
        FieldPanel('bg_image'),
    ]
