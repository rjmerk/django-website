from django.db import models


class BaseModel(models.Model):
    created = models.DateTimeField(
        auto_now_add=True)
    modified = models.DateTimeField(
        auto_now=True)

    class Meta:
        abstract = True


class Article(BaseModel):
    title = models.CharField(
        max_length=100,
        unique=True)
    slug = models.SlugField(
        max_length=100,
        unique=True)
    content = models.TextField()
    publish_date = models.DateTimeField(
        db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-publish_date"]
