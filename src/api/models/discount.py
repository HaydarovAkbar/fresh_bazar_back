from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _
from api.models.info import State


class Discount(models.Model):
    name = models.CharField(_("Discount Name"), max_length=50)
    description = models.TextField(_("Discount Description"))
    discount_percent = models.DecimalField(_("Discount Percent"), max_digits=5, decimal_places=2)
    date_of_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Discount")
        verbose_name_plural = _("Discounts")
        ordering = ("id",)
        db_table = "discount"

    def delete(self, *args):
        self.deleted_at = timezone.now()
        self.save()
        return True
