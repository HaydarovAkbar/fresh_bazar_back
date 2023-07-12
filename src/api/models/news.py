from django.conf import settings
from django.db import models
from api.models.info import State


class News(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_of_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    image = models.ImageField(upload_to="news")
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"
        ordering = ("id",)
        db_table = "news"
        indexes = [
            models.Index(fields=["title"], name="news_title_idx"),
            models.Index(fields=["description"], name="news_description_idx"),
        ]

    @property
    def get_image_url(self):
        # "Returns the image url."
        try:
            return '%s%s' % (settings.HOST, self.image.url)
        except ValueError:
            return ''


class Banner(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_of_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    image = models.ImageField(upload_to="banner")
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    configuration = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Banners"
        ordering = ("id",)
        db_table = "banner"
        indexes = [
            models.Index(fields=["title"], name="banner_title_idx"),
            models.Index(fields=["description"], name="banner_description_idx"),
        ]

    @property
    def get_image_url(self):
        # "Returns the image url."
        try:
            return '%s%s' % (settings.HOST, self.image.url)
        except ValueError:
            return ''