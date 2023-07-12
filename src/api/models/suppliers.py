from django.db import models
from django.utils.translation import gettext_lazy as _
from api.models.info import State, UnitOfMeasure


class Suppliers(models.Model):
    name = models.CharField(max_length=50, help_text=_("Suppliers Name"))
    brand = models.CharField(max_length=50, help_text=_("Suppliers Name"))
    image = models.ImageField(upload_to='suppliers/', null=True, blank=True)
    weight = models.CharField(max_length=50, help_text=_("Weight"))
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text=_("Price"))
    supply_date = models.CharField(max_length=25, help_text=_("Supply Date"))
    bar_code = models.CharField(max_length=50, help_text=_("Bar Code"))
    certificate = models.ImageField(upload_to='certificate/', null=True, blank=True, help_text=_("Certificate"))
    market_share = models.IntegerField(help_text=_("Market Share"))
    applied = models.BooleanField(default=False, help_text=_("Applied"))
    partnership = models.BooleanField(default=False, help_text=_("Partnership"))
    date_of_created = models.DateTimeField(auto_now_add=True, help_text=_("Date of Created"))

    state = models.ForeignKey(State, on_delete=models.CASCADE, help_text=_("State"))
    unit_of_measure = models.ForeignKey(UnitOfMeasure, on_delete=models.CASCADE, help_text=_("Unit of Measure"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Supplier")
        verbose_name_plural = _("Suppliers")
        db_table = "supplier"

    @property
    def get_image_url(self):
        if self.image:
            return self.image.url
        return None

    @property
    def get_certificate_url(self):
        if self.certificate:
            return self.certificate.url
        return None
