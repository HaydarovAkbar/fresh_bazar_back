from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from api.models.info import State


class ProductCategory(models.Model):
    name = models.CharField(_("Product Category Name"), max_length=50)
    description = models.TextField(_("Product Category Description"))
    date_of_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    image_url = models.ImageField(_("Product Category Image URL"), upload_to="product_category")
    deleted_at = models.DateTimeField(null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Product Category")
        verbose_name_plural = _("Product Categories")
        ordering = ("id",)
        db_table = "product_category"
        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["description"]),
        ]

    def delete(self, *args):
        self.deleted_at = timezone.now()
        self.save()
        return True

    @property
    def get_image_url(self):
        # "Returns the image url."
        try:
            return '%s%s' % (settings.HOST, self.image_url.url)
        except ValueError:
            return ''