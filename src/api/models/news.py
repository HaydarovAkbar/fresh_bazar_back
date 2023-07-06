from django.conf import settings
from django.db import models
from api.models.info import State


class News(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_of_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    image_url = models.ImageField(upload_to="news")
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

    def get_image_url(self):
        # "Returns the image url."
        try:
            return '%s%s' % (settings.HOST, self.image_url.url)
        except ValueError:
            return ''
