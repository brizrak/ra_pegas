from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField


class HomePage(Page):
    cat_image = RichTextField(
        blank=True,
        null=True,
    )
    cats_image = RichTextField(
        blank=True,
        null=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel('cat_image'),
        FieldPanel('cats_image'),
    ]
