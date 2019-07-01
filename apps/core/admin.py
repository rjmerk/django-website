from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ["preview_link"]

    def preview_link(self, instance):
        if instance.slug:
            url = reverse("article-preview", kwargs={"slug": instance.slug})
            html = '<a href="{}">{}</a>'.format(url, instance.title)
        else:
            html = ''
        return mark_safe(html)
