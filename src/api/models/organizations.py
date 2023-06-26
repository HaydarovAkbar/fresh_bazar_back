from django.db import models
from django.utils.translation import gettext_lazy as _
from api.models.info import State

class Organization(models.Model):
    name = models.CharField(_("Organization Name"), max_length=50)
    description = models.TextField(_("Organization Description"))
    date_of_created = models.DateTimeField(auto_now_add=True)
    image_url = models.ImageField(_("Organization Logo Image URL"), upload_to="organization")
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Organization")
        verbose_name_plural = _("Organizations")
        ordering = ("id",)
        db_table = "organization"